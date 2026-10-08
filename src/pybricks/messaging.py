# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2026 The Pybricks Authors

"""
他のデバイスとメッセージを送受信するためのクラス。
"""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, Generic, Self, TypeVar, overload

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable, Sequence

    from ._common import MaybeAwaitable

T = TypeVar("T")


class BLERadio:
    """
    Bluetooth Low Energyを使用して、接続せずにメッセージを送受信します。

    .. versionadded:: 4.0

        以前は各Hubクラスの一部として提供されていました。
    """

    def __init__(
        self,
        broadcast_channel: int | None = None,
        observe_channels: Sequence[int] = [],
    ):
        """BLERadio(broadcast_channel=None, observe_channels=[])

        Arguments:
            broadcast_channel:
                データのブロードキャストに使用するチャンネル番号（0～255）。
                ブロードキャストを使用しない場合は ``None`` を選択します。
            observe_channels:
                ``hub.ble.observe()`` が呼び出されたときにリッスンする
                チャンネルのリスト。リッスンするチャンネルが多いほど、より
                多くのメモリが必要です。デフォルトは空のリスト（チャンネル
                なし）です。
        """

    @overload
    def broadcast(self, data: None) -> MaybeAwaitable: ...

    @overload
    def broadcast(
        self, data: Iterable[bool | int | float | str | bytes]
    ) -> MaybeAwaitable: ...

    @overload
    def broadcast(self, data: bool | float | str | bytes) -> MaybeAwaitable: ...

    def broadcast(self, data: object) -> MaybeAwaitable:
        """broadcast(data)

        事前に選択した ``broadcast_channel`` で、指定したデータの
        ブロードキャストを開始します。

        データの型は ``int``、``float``、``str``、``bytes``、``True``、
        ``False`` のいずれかです。また、これらの値のリストやタプルも指定
        できます。

        ``None`` を指定するとブロードキャストを停止します。ブロードキャスト
        機能が不要な場合、特に同時に観測を行う場合は、パフォーマンスの向上に
        役立ちます。

        データの合計サイズはかなり制限されています（26バイト）。``True`` と
        ``False`` はそれぞれ1バイト、``float`` は5バイトを使用します。
        ``int`` は数値の大きさに応じて2～5バイトを使用します。``str`` と
        ``bytes`` はオブジェクトのバイト数に1バイトを加えたサイズを使用
        します。

        マルチタスク時は、一度に1つのタスクのみがブロードキャストできます。
        複数のタスク（またはブロックスタック）から情報をブロードキャスト
        するには、1つ以上の変数が変化したときに新しい値をブロードキャスト
        する専用の別タスクを使用するとよいでしょう。

        Args:
            data: ブロードキャストする値。

        Raises:
            RuntimeError: ``broadcast_channel`` が設定されていない場合。
            ValueError: エンコードされたデータが26バイトを超える場合。
            TypeError: ``data`` に ``bool``、``int``、``float``、``str``、
                ``bytes`` 以外の値が含まれている場合。
        """

    def observe(
        self, channel: int
    ) -> (
        tuple[bool | int | float | str | bytes, ...]
        | bool
        | int
        | float
        | str
        | bytes
        | None
    ):
        """observe(channel) -> bool | int | float | str | bytes | tuple | None

        指定したチャンネルで最後に観測されたデータを取得します。

        Hubがコンピューターや他のデバイスに同時に接続されていない場合、
        データの受信がより確実になります。

        Args:
            channel (int): 観測するチャンネル。このオブジェクトの作成時に
                ``observe_channels`` で指定したチャンネルの1つである必要が
                あります。

        Returns:
            送信時と同じ形式で受信したデータ。直近1秒以内にデータを受信
            していない場合は ``None``。

        Raises:
            ValueError: ``channel`` が ``observe_channels`` に含まれていない
                場合。
        """

    def signal_strength(self, channel: int) -> int:
        """signal_strength(channel) -> int: dBm

        指定したチャンネルの平均信号強度をdBm単位で取得します。

        これはブロードキャストしているデバイスの近さを示します。近くの
        デバイスの信号強度は約-40 dBm、遠くのデバイスは約-70 dBmになります。

        Args:
            channel (int): チャンネル番号。このオブジェクトの作成時に
                ``observe_channels`` で指定したチャンネルの1つである必要が
                あります。

        Returns:
            信号強度。直近1秒以内にデータを受信していない場合は ``-128``。

        Raises:
            ValueError: ``channel`` が ``observe_channels`` に含まれていない
                場合。
        """

    def version(self) -> str:
        """version() -> str

        Bluetoothチップのファームウェアバージョンを取得します。
        """


class HubNetwork:
    """
    Bluetoothを使用して、対応するHub間でメッセージを送受信します。

    ネットワークに参加するすべてのプログラムでこのオブジェクトを作成します。
    そのうち *manager* と呼ばれる1台のHubが、アドレスで識別される他のHubに
    接続します。例: :meth:`connect('00:16:53:12:34:56') <connect>`。
    その後はすべてのHubが対等になり、それぞれが他のどのBrickにもメッセージを
    送信できます。

    各HubのアドレスはEV3の設定メニューで確認できるほか、:meth:`address`
    メソッドで表示することもできます。接続はプログラムを再起動しても維持
    されます。

    このプロトコルはメッセージの配信を保証します。ただし、十分な空き容量が
    ある場合にのみプログラムで受信できます。マネージャーはバックグラウンドで
    メッセージの中継を処理しますが、これはマネージャーのプログラムが実行中の
    間のみ機能します。

    .. versionadded:: 4.1
    """

    def __init__(self, inbox_size: int = 1024):
        """HubNetwork(inbox_size=1024)

        Arguments:
            inbox_size (int): 送信元の各Brickについて、メッセージを保存する
                バイト数。

        Raises:
            RuntimeError: ``HubNetwork`` オブジェクトがすでに存在する場合、
                またはマルチタスク開始後に使用された場合。
            OSError: このBrickのBluetoothが動作しない場合。
            ValueError: ``inbox_size`` が1件のメッセージを保持するには
                小さすぎる場合。
        """

    def address(self) -> str:
        """address() -> str

        このBrickのBluetoothアドレスを取得します。

        これはBrickの画面に表示されるアドレスと同じです。これを表示して、
        他のBrickのプログラムに入力するアドレスを確認できます。

        Returns:
            このBrickのアドレス。
            ``'00:16:53:AB:CD:EF'`` のような形式で、文字は常に大文字です。
        """
        return ""

    def connect(self, address: str) -> MaybeAwaitable:
        """connect(address)

        ネットワークを構築するために、別の1台のHub（EV3 Brick）に接続します。

        ネットワーク内でこの操作を行うのは1台のHubだけです。そのHubは
        マネージャーと呼ばれます。他のHubはまだプログラムを実行していなくても
        構いませんが、プログラムが実行されるまでメッセージは受信されません。

        接続には時間がかかります。Brick1台につき最大で約15秒かかり、一度で
        成功するとは限らないため、あきらめるまでに数回再試行します。このため、
        通常はプログラムの開始時にこの操作を行います。

        すでに接続済みのBrickはすぐに準備できるため、後で再度使用しても安全
        です。これにより、2回目の実行は非常に速く開始できます。

        Arguments:
            address (str): 接続先のBrickのBluetoothアドレス
                （例: ``'00:16:53:12:34:56'``）。最大7台の他のBrickに接続
                できます。

        Raises:
            OSError: Brickに接続できなかった場合。ValueError: ``address`` が
                有効なBluetoothアドレスでない場合、またはこのBrick自身の
                アドレスの場合。
        """

    def is_connected(self, address: str | None = None) -> bool:
        """
        is_connected() -> bool
        is_connected(address) -> bool

        Brickがネットワークに参加しているかどうかを確認します。

        これは待機する側のBrickで便利です。ネットワークの構築にかかる時間を
        推測する代わりに、マネージャーのBrickが接続してくるまで
        ``is_connected()`` を確認し続けることができます。

        個々のBrickを確認するための ``address`` 引数は、マネージャーのBrick
        のみが使用できます。

        Arguments:
            address (str): 確認するHubのBluetoothアドレス。

        Returns:
            Hubがネットワークに参加していれば ``True``、そうでなければ
            ``False``。アドレスを指定しない場合は、いずれかのHubが接続
            されていれば ``True``。

        Raises:
            ValueError: ``address`` が有効なBluetoothアドレスでない場合。
        """
        return False

    def send(
        self,
        data: bool
        | float
        | str
        | bytes
        | None
        | tuple[bool | int | float | str | bytes | None, ...],
        address: str | None = None,
    ) -> MaybeAwaitable:
        """
        send(data) send(data, address)

        ネットワーク上のすべてのHub、または特定の1台のHubにメッセージを
        送信します。

        メッセージは1つのオブジェクト、またはオブジェクトのタプルです。
        オブジェクトの型は ``int``、``float``、``str``、``bytes``、
        ``True``、``False``、``None`` のいずれかです。受信側のBrickは同じ
        オブジェクトを受け取るので、``(60, "left")`` を送信すると
        ``(60, "left")`` として届きます。

        ``bytes`` のみのメッセージはそのまま送信されます。これは独自の
        メッセージを組み立てる場合に適しています。このようなメッセージは
        255バイトまで格納できます。それ以外のメッセージには、含まれる
        オブジェクトの短い説明も付随するため、格納できるサイズは少し小さく
        なります。``True``、``False``、``None`` はそれぞれ2バイト、``int``
        と ``float`` はそれぞれ5バイト、``str`` と ``bytes`` はオブジェクトの
        バイト数に2～4バイトを加えたサイズを使用します。1つのメッセージには
        最大32個のオブジェクトを格納できます。

        このBrickから別の1台のBrickへのメッセージは、送信した順序で届きます。

        Arguments:
            data: 送信するメッセージ。
            address (str): 送信先のBrickのBluetoothアドレス。
                省略するとネットワーク上の他のすべてのBrickに送信します。
                Brickは自分自身が送信したメッセージを受信しません。

        Raises:
            ValueError: ``address`` が有効なBluetoothアドレスでない場合、
                またはメッセージが大きすぎて送信できない場合。
            TypeError: メッセージに送信できないオブジェクトが含まれている
                場合。
        """

    def inbox(
        self, latest: bool = False
    ) -> tuple[
        tuple[
            str,
            bool
            | int
            | float
            | str
            | bytes
            | None
            | tuple[bool | int | float | str | bytes | None, ...],
        ],
        ...,
    ]:
        """inbox(latest=False) -> tuple

        前回読み取ってから届いたメッセージを取得します。

        このメソッドは待機しません。何も届いていない場合は空の結果を返すため、
        それに対する ``for`` ループは何も行いません。読み取るとこのBrickの
        メモリからメッセージが削除されるため、各メッセージは一度しか受け取れ
        ません。

        あなたに送信する各Brickには、内部にそれぞれ専用の受信ボックスが
        あります。1台のBrickが受信ボックスに収まりきらない量を送信した場合、
        最も古いメッセージが破棄されます。常時送信しているBrickが他のBrickの
        メッセージを押し出すことはありません。

        プログラムは開始前に送信されたメッセージを受信しません。メッセージは
        どのBrickから送信されたかに関係なく、届いた順に受け取ります。

        Arguments:
            latest (bool): ``True`` を選択すると、各Brickからの最新の
                メッセージのみを保持し、それより古いメッセージは破棄します。
                センサーの読み取り値のように、Brickが最新の値を送り続け、
                最新のものだけが有用な場合に適しています。

        Returns:
            ``(address, data)`` のペアのタプル。``address`` はメッセージを
            送信したBrickのBluetoothアドレス、``data`` は送信時と同じ形式の
            メッセージです。``latest`` を使用した場合、各Brickにつき最大1組
            のペアになります。

        Raises:
            ValueError: メッセージがそれに付随する説明と一致しない場合。
                これはメッセージが途中で破損したことを意味します。
        """
        return ()


class Connection:
    @abstractmethod
    def read_from_mailbox(self, name: str) -> bytes: ...

    @abstractmethod
    def send_to_mailbox(self, name: str, data: bytes) -> None: ...

    @abstractmethod
    def wait_for_mailbox_update(self, name: str) -> None: ...


class Mailbox(Generic[T]):
    def __init__(
        self,
        name: str,
        connection: Connection,
        encode: Callable[[T], bytes] | None = None,
        decode: Callable[[bytes], T] | None = None,
    ):
        """Mailbox(name, connection, encode=None, decode=None)

        データを保持するメールボックスを表すオブジェクトです。

        他のEV3 Brickから配信されたデータを読み取ったり、同じメールボックスを
        持つ他のBrickにデータを送信したりできます。

        デフォルトでは、メールボックスはバイト列のみを読み取り・送信します。
        他のデータを送信するには、Pythonオブジェクトをバイト列にエンコード
        する ``encode`` 関数と、バイト列をPythonオブジェクトに戻す ``decode``
        関数を指定できます。

        Arguments:
            name (str):
                このメールボックスの名前。
            connection:
                :class:`BluetoothMailboxClient` などの接続オブジェクト。
            encode (callable):
                Pythonオブジェクトをバイト列にエンコードする関数。
            decode (callable):
                バイト列から新しいPythonオブジェクトを作成する関数。
        """

    def read(self) -> T:
        """read()

        メールボックスの現在の値を取得します。

        Returns:
            現在の値。メールボックスが空の場合は ``None``。
        """
        return ""

    def send(self, value: T, brick: str | None = None) -> None:
        """send(value, brick=None)

        接続されたデバイス上のこのメールボックスに値を送信します。

        Arguments:
            value:
                メールボックスに配信される値。
            brick (str):
                Brickの名前またはBluetoothアドレス。接続されているすべての
                デバイスにブロードキャストする場合は ``None``。

        Raises:
            OSError:
                接続に問題がある場合。
        """

    def wait(self) -> None:
        """wait()

        リモートデバイスによってメールボックスが更新されるまで待機します。"""

    def wait_new(self) -> T:
        """wait_new()

        メールボックスの現在の値と等しくない新しい値が配信されるまで
        待機します。

        Returns:
            新しい値。
        """
        return object()


class LogicMailbox(Mailbox[bool]):
    def __init__(self, name: str, connection: Connection):
        """LogicMailbox(name, connection)

        ブール値データを保持するメールボックスを表すオブジェクトです。

        通常の :class:`Mailbox` と同じように動作しますが、値は ``True`` または
        ``False`` である必要があります。

        これはEV3-Gの "logic" メールボックス型と互換性があります。

        Arguments:
            name (str):
                このメールボックスの名前。
            connection:
                :class:`BluetoothMailboxClient` などの接続オブジェクト。
        """


class NumericMailbox(Mailbox[float]):
    def __init__(self, name: str, connection: Connection):
        """NumericMailbox(name, connection)

        数値データを保持するメールボックスを表すオブジェクトです。

        通常の :class:`Mailbox` と同じように動作しますが、値は ``15`` や
        ``12.345`` などの数値である必要があります。

        これはEV3-Gの "numeric" メールボックス型と互換性があります。

        Arguments:
            name (str):
                このメールボックスの名前。
            connection:
                :class:`BluetoothMailboxClient` などの接続オブジェクト。
        """


class TextMailbox(Mailbox[str]):
    def __init__(self, name: str, connection: Connection):
        """TextMailbox(name, connection)

        テキストデータを保持するメールボックスを表すオブジェクトです。

        通常の :class:`Mailbox` と同じように動作しますが、データは
        ``'hello!'`` などの文字列である必要があります。

        これはEV3-Gの "text" メールボックス型と互換性があります。

        Arguments:
            name (str):
                このメールボックスの名前。
            connection:
                :class:`BluetoothMailboxClient` などの接続オブジェクト。
        """


class BluetoothMailboxServer:
    """1台以上のリモートEV3からのBluetooth接続を表すオブジェクトです。

    リモートのEV3は、MicroPythonまたは標準のEV3ファームウェアのいずれかを
    実行できます。

    "server" は "client" からの接続を待ちます。
    """

    def __enter__(self) -> Self:
        return self

    def __exit__(self, type, value, traceback) -> None:
        self.server_close()

    def wait_for_connection(self, count: int = 1) -> None:
        """wait_for_connection(count=1)

        リモートデバイス上の :class:`BluetoothMailboxClient` が接続するのを
        待ちます。

        Arguments:
            count (int):
                待機するリモート接続の数。

        Raises:
            OSError:
                接続の確立に問題があった場合。
        """

    def server_close(self) -> None:
        """server_close()

        すべての接続を閉じます。"""


class BluetoothMailboxClient:
    """1台以上のリモートEV3へのBluetooth接続を表すオブジェクトです。

    リモートのEV3は、MicroPythonまたは標準のEV3ファームウェアのいずれかを
    実行できます。

    "client" は待機中の "server" への接続を開始します。
    """

    def __enter__(self) -> Self:
        return self

    def __exit__(self, type, value, traceback) -> None:
        self.close()

    def connect(self, brick: str) -> None:
        """connect(brick)

        別のデバイス上の :class:`BluetoothMailboxServer` に接続します。

        リモートデバイスはペアリング済みで、接続を待機している必要があります。
        :meth:`BluetoothMailboxServer.wait_for_connection` を参照してください。

        Arguments:
            brick (str):
                接続先のリモートEV3の名前またはBluetoothアドレス。

        Raises:
            OSError:
                接続の確立に問題があった場合。
        """

    def close(self) -> None:
        """close()

        すべての接続を閉じます。"""


class AppData:
    """
    USBまたはBluetooth経由でPybricks Codeのホストアプリケーションと生データを
    やり取りします。これはビジョンプロセッサーなどのスマートセンサー機能で
    使用されます。

    各プロセッサーは1つのモードを持ち、決まった量のデータを生成します。
    これらは変化するたびに継続的にHubへ送信されます。ユーザーコードは
    ブロックせずにいつでもこれらのバッファ済みの値を読み取れます。すべての
    値は初期状態ではゼロです。

    Hubの観点からは、ホストへの書き戻しはawaitableな操作です。モードや
    モード設定の構成に使用できます。

    同時に存在できるインスタンスは1つだけです。プログラムの初期化中に作成
    する必要があります。その後は、マルチタスク実行中にすべてのメソッドを
    使用できます。
    """

    def __init__(self, modes: list[tuple[int, int]]):
        """AppData(modes)

        Arguments:
            modes:
                ``(mode, size)`` タプルのリスト。``mode`` はモード番号
                （0～255）、``size`` はそのモードの受信バッファに割り当てる
                バイト数です。モード番号は一意である必要があります。リストは
                モード番号順に自動的にソートされます。

        Raises:
            RuntimeError: ``AppData`` インスタンスがすでに存在する場合。
            TypeError: ``modes`` がリストでない場合、またはいずれかの要素が
                モード値0～255の ``(mode, size)`` タプルでない場合。
            ValueError: いずれかのモード番号が複数回出現する場合。
        """

    def get_bytes(self, mode: int, index: int | None = None) -> bytes | int:
        """get_bytes(mode, index=None) -> bytes | int

        指定したモードでホストから受信したデータを取得します。

        Args:
            mode (int): 読み取るモード番号。
            index (int): 指定した場合、モードのバッファ内のこの位置にある
                単一のバイトを整数として返します。それ以外の場合は、モードの
                バッファ全体を ``bytes`` として返します。

        Returns:
            そのモードで受信したすべてのバイト。``index`` を指定した場合は
            整数としての単一のバイト。

        Raises:
            ValueError: ``mode`` が設定されていない場合、または ``index`` が
                範囲外の場合。
        """

    def write_bytes(self, data: bytes) -> MaybeAwaitable:
        """write_bytes(data)

        ホストアプリケーションに生のバイト列を送信します。

        Args:
            data (bytes): 送信するデータ。
        """

    def configure(self, mode: int, parameter: int, value: bytes) -> MaybeAwaitable:
        """configure(mode, parameter, value)

        指定したモードの設定コマンドをホストに送信します。

        これは :meth:`write_bytes` のラッパーです。モード設定を行うために
        ``[0x01, mode, parameter]`` ヘッダーを先頭に追加します。

        Args:
            mode (int): 設定するモード番号。
            parameter (int): モード内のパラメーター識別子。
            value (bytes): 送信する設定値。
        """

    def close(self) -> None:
        """close()

        データコールバックを無効化し、受信バッファを解放します。

        オブジェクトがガベージコレクトされたときにも自動的に呼び出されます。
        """


# Hide type-only names from jedi completions in the module namespace.
if TYPE_CHECKING:
    del abstractmethod
    del Callable
    del Iterable
    del MaybeAwaitable
    del Sequence
    del T
