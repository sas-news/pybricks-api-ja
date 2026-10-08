# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2023 The Pybricks Authors

"""汎用入出力デバイス。"""

from __future__ import annotations

from typing import TYPE_CHECKING, overload

from . import _common

if TYPE_CHECKING:
    from ._common import MaybeAwaitable, MaybeAwaitableBytes, MaybeAwaitableTuple
    from .parameters import Number, Port


class PUPDevice:
    """Powered Upモーターまたはセンサー。"""

    def __init__(self, port: Port):
        """PUPDevice(port)

        Arguments:
            port (Port): デバイスが接続されているポート。
        """

    def info(self) -> dict:
        """info() -> dict

        デバイスに関する情報を取得します。

        DCモーターやライトなどのパッシブデバイスの場合は、 ``id`` キーのみを
        持つ辞書を返します。

        UARTデバイスの場合は、 ``id`` キーと ``modes`` キーを持つ辞書を
        返します。 ``modes`` の値はモードごとに1つのタプルを持つタプルの
        タプルで、それぞれにモード名、値の個数、データ型が含まれます。

        Returns:
            デバイス情報を格納した辞書。
        """

    def read(self, mode: int) -> MaybeAwaitableTuple:
        """read(mode) -> tuple

        指定したモードから値を読み取ります。

        パッシブタッチセンサーの場合は、 ``mode`` 引数に関わらず、センサーが
        押されているかどうかを示す単一の真偽値を返します。

        DCモーターやライトなど、読み取りをサポートしない他のパッシブ
        デバイスではエラーが発生します。

        Arguments:
            mode (int): デバイスのモード。

        Returns:
            デバイスから読み取った値。

        Raises:
            OSError: 読み取りをサポートしないパッシブデバイス
                （DCモーターやライトなど）の場合。
        """

    def write(self, mode: int, data: tuple) -> MaybeAwaitable:
        """write(mode, data)

        デバイスに値を書き込みます。一部のUARTデバイスとモードのみが
        これをサポートします。

        Arguments:
            mode (int): デバイスのモード。
            data (tuple): 書き込む値。値の個数と型は、指定したモードで
                デバイスが期待するものと一致しなければなりません。

        Raises:
            OSError: 書き込みをサポートしないパッシブデバイスの場合。
            ValueError: モードが無効、モードが書き込み不可、値の個数が
                一致しない、または値がデータ型の範囲外の場合。
        """

    def reset(self) -> None:
        """reset()

        UARTデバイスをリセットします。その後、デバイスは自動的に同期し、
        数秒後に使用可能になります。この種のセンサーが接続時に行う処理を
        強制的に再実行させたい場合に便利です。

        Raises:
            OSError: リセットをサポートしないパッシブデバイスの場合。
        """


class LUMPDevice(PUPDevice):
    """LEGO UART Messaging Protocolを使用するデバイス。

    使用可能なメソッドの説明については、同等の
    :class:`PUPDevice() <pybricks.iodevices.PUPDevice>` を参照してください。

    EV3では、このクラスはUARTデバイスへのアクセスのみを提供します。
    パッシブデバイスを操作するには、他のクラスを使用してください。
    """


class DCMotor(_common.DCMotor):
    """LEGO® MINDSTORMS EV3用のDCモーター。"""


class AnalogSensor:
    """汎用またはカスタムのアナログセンサー。"""

    def __init__(self, port: Port, custom: bool = False):
        """AnalogSensor(port, custom=False)

        Arguments:
            port (Port): センサーが接続されているポート。
            custom (bool): カスタムのアナログセンサーを使用している場合は
                ``True`` に設定します。

        Raises:
            OSError: 標準のLEGOアナログセンサーがポートで検出されなかった
                場合。 ``custom=False`` の場合にのみ適用されます。
        """

    def voltage(self) -> int:
        """voltage() -> int: mV

        アナログ電圧を測定します。

        Returns:
            アナログ電圧。
        """

    def resistance(self) -> int:
        """resistance() -> int: Ω

        抵抗を測定します。

        この値は、アナログデバイスが抵抗器やサーミスタなどのパッシブ負荷
        である場合にのみ意味を持ちます。10 kΩの内部プルアップ抵抗で
        分圧回路を構成していると仮定して計算されます。

        回路がオープン（負荷が接続されていない）の場合は、整数の最大値が
        返されます。

        Returns:
            アナログデバイスの抵抗値。回路がオープンの場合は整数の最大値。
        """

    def active(self) -> None:
        """active()

        センサーをアクティブモードに設定します。これによりセンサーポートの
        ピン5が `high` になります。

        一部のアナログセンサーでは、スイッチの制御に使用されます。
        たとえば、NXTライトセンサーをカスタムアナログセンサーとして使用する
        場合、このメソッドはライトを点灯します。それ以降、 ``voltage()`` は
        反射光の生の値を返します。
        """

    def passive(self) -> None:
        """passive()

        センサーをパッシブモードに設定します。これによりセンサーポートの
        ピン5が `low` になります。

        一部のアナログセンサーでは、スイッチの制御に使用されます。
        たとえば、NXTライトセンサーをカスタムアナログセンサーとして使用する
        場合、このメソッドはライトを消灯します。それ以降、 ``voltage()`` は
        環境光の生の値を返します。
        """


class I2CDevice:
    """汎用またはカスタムのI2Cデバイス。

    注意: ``power_pin`` オプションは自己責任で使用してください。不用意に
    ピンへ電源を供給すると、ハブやデバイスを損傷する可能性があります。
    このオプションを使用する場合、リスクを理解したかどうかの確認が
    求められます。
    """

    def __init__(
        self,
        port: Port,
        address: int,
        custom: bool = False,
        power_pin: int = 0,
        nxt_quirk: bool = False,
    ):
        """I2CDevice(port, address, custom=False, power_pin=0, nxt_quirk=False)

        Arguments:
            port (Port): デバイスが接続されているポート。
            address (int): クライアントデバイスのI2Cアドレス。
                :ref:`I2Cアドレス <i2caddress>` を参照してください。
            custom (bool): カスタムのI2Cデバイスを使用している場合は
                ``True`` に設定します。
            power_pin (int): デバイスの電源要件。ピンに電源を供給しない場合は
                ``0`` （デフォルト）を使用します。NXTとEV3では、 ``1`` を
                使用してバッテリー電源をピン1に供給します。他のピンは
                サポートされていません。
            nxt_quirk (bool): 確実に通信するために低速の互換タイミングを
                必要とする古いNXT I2Cセンサー（旧型のNXT超音波センサーなど）
                には ``True`` に設定します。
        """

    @overload
    def read(self, reg: int | None = None, length: int = 1) -> MaybeAwaitableBytes: ...

    @overload
    def read(
        self, reg: int | None = None, length: int = 1, map: callable = ...
    ) -> MaybeAwaitable: ...

    def read(
        self, reg: int | None = None, length: int = 1, map=None
    ) -> MaybeAwaitableBytes:
        """read(reg=None, length=1) -> bytes
        read(reg=None, length=1, map=callable) -> Any

        指定したレジスタからバイトを読み取ります。

        Arguments:
            reg (int): 読み取りを開始するレジスタ: 0--255または
                0x00--0xFF。 ``None`` を使用すると、先にレジスタアドレスを
                書き込まずに読み取ります。
            length (int): 読み取るバイト数。
            map (callable): 返されたバイトを変換するオプションの
                呼び出し可能オブジェクト。指定された場合、バイトを引数として
                呼び出され、その戻り値が代わりに返されます。

        Returns:
            デバイスから返されたバイト。呼び出し可能オブジェクトが指定された
            場合は ``map`` の戻り値。
        """

    def write(
        self, reg: int | None = None, data: bytes | None = None
    ) -> MaybeAwaitable:
        """write(reg=None, data=None)

        バイトを書き込みます。オプションで指定したレジスタから書き込みを
        開始できます。

        Arguments:
            reg (int): 書き込みを開始するレジスタ: 0--255または
                0x00--0xFF。 ``None`` を使用すると、レジスタプレフィックス
                なしで書き込みます。
            data (bytes): 書き込むバイト。 ``None`` を使用すると、レジスタの
                後に何も書き込みません。

        Raises:
            ValueError: ``reg`` が指定されていて ``data`` が32バイトを超える
                場合。より多くのデータを書き込むには、 ``reg`` 引数を省略し、
                ``data`` の最初のバイトとしてレジスタを含めてください。
        """


class UARTDevice:
    """汎用UARTデバイス。

    注意: ``power_pin`` オプションは自己責任で使用してください。不用意に
    ピンへ電源を供給すると、ハブやデバイスを損傷する可能性があります。
    このオプションを使用する場合、リスクを理解したかどうかの確認が
    求められます。
    """

    def __init__(
        self,
        port: Port,
        baudrate: int = 115200,
        timeout: int | None = None,
        power_pin: int = 0,
    ):
        """UARTDevice(port, baudrate=115200, timeout=None, power_pin=0)

        Arguments:
            port (Port): デバイスが接続されているポート。Powered UPハブでは
                すべてのポートがサポートされます。EV3ではセンサーポートのみが
                サポートされます。
            baudrate (int): UARTデバイスのボーレート。
            timeout (Number, ms): ``read`` と ``write`` の実行中に待機する
                時間。 ``None`` を選択すると、無期限に待機します。
            power_pin (int): デバイスの電源要件。ピンに電源を供給しない
                場合は ``0`` （デフォルト）を使用します。Powered UPハブでは、
                ピン1または2にはそれぞれ ``1`` または ``2`` を使用します。
                これはモーターへの給電と同等に、バッテリー電源をそのピンに
                供給します。EV3では、 ``1`` を使用してバッテリー電源をピン1に
                供給しますが、わずかな電流しか利用できません。

        Raises:
            ValueError: ``timeout`` が0または負の場合。
        """

    def read(self, length: int = 1) -> MaybeAwaitableBytes:
        """read(length=1) -> bytes

        バッファから指定したバイト数を読み取ります。

        要求したバイト数が受信されるまで、プログラムは待機します。
        ``timeout`` より長くかかる場合は、 ``ETIMEDOUT`` 例外が発生します。

        Arguments:
            length (int): 読み取るバイト数。1以上でなければなりません。

        Returns:
            デバイスから返されたバイト。

        Raises:
            ValueError: ``length`` が1未満の場合。
            OSError: 読み取りが ``timeout`` より長くかかる場合。
        """

    def read_all(self) -> bytes:
        """read_all() -> bytes

        バッファ内の現在のすべてのバイトを読み取ります。バッファが空の
        場合でも、待機せずに即座に戻ります。

        Returns:
            バッファ内の現在のバイト。読み取るものがない場合は空のバイト列。
        """

    def write(self, data: bytes) -> MaybeAwaitable:
        """write(data)

        デバイスにバイトを書き込みます。

        Arguments:
            data (bytes): 書き込むバイト。

        Raises:
            TypeError: ``data`` が ``bytes`` 、 ``bytearray`` 、 ``str`` の
                いずれでもない場合。
            OSError: 書き込みが ``timeout`` より長くかかる場合。
        """

    def waiting(self) -> int:
        """waiting() -> int

        読み取り待ちのバイト数を取得します。

        Returns:
            バッファ内のバイト数。
        """

    def set_baudrate(self, baudrate: int) -> None:
        """set_baudrate(baudrate)

        UARTデバイスのボーレートを変更します。

        Arguments:
            baudrate (int): すべての値がサポートされるとは限りません。

        Raises:
            ValueError: ``baudrate`` が1未満の場合。
        """

    def wait_until(self, pattern: bytes) -> MaybeAwaitable:
        """wait_until(pattern)

        特定のバイトシーケンスが受信されるまで待機します。パターンに
        一致しないバイトは破棄されます。

        Arguments:
            pattern (bytes): 待機するバイトシーケンス。空であっては
                なりません。

        Raises:
            ValueError: ``pattern`` が空の場合。
            OSError: このメソッドがすでに実行中の場合。
        """

    def clear(self) -> None:
        """clear()

        受信バッファを空にします。"""


class LWP3Device:
    """
    `LEGO Wireless Protocol v3`_ を使用して、公式のLEGOファームウェアを
    実行しているハブに接続します。

    .. _`LEGO Wireless Protocol v3`:
        https://lego.github.io/lego-ble-wireless-protocol-docs/
    """

    def __init__(
        self,
        hub_kind: int,
        name: str | None = None,
        timeout: int = 10000,
        pair: bool = False,
        num_notifications: int = 8,
        connect: bool = True,
    ):
        """LWP3Device(hub_kind, name=None, timeout=10000, pair=False, num_notifications=8, connect=True)

        Arguments:
            hub_kind (int):
                接続するハブの `hub type identifier`_ 。
            name (str):
                接続するハブの名前。 ``None`` を指定すると、任意のハブに
                接続します。
            timeout (int):
                例外が発生するまで接続を待機する時間（ミリ秒）。
            pair (bool): セキュアな接続のためにペアリングを試みるかどうか。
                一部の新しいハブでは必須です。
            num_notifications (int): 古いメッセージを破棄するまでに保持する
                リモートハブからの受信メッセージ数。
            connect (bool): 接続をスキップする場合は ``False`` を選択します。
                ``connect()`` を後で呼び出して接続できます。

        .. versionchanged:: 3.6

            ``pair`` パラメータを追加しました。

        .. versionchanged:: 3.7

            ``num_notifications`` パラメータを追加しました。

        .. _`hub type identifier`:
            https://github.com/pybricks/technical-info/blob/master/assigned-numbers.md#hub-type-ids
        """

    def connect(self) -> MaybeAwaitable:
        """connect()

        デバイスに接続します。切断した場合、または ``connect=False`` で
        初期化した場合にのみ必要です。

        Raises:
            OSError: 接続の試行が失敗したかタイムアウトした場合。
        """

    @overload
    def name(self, name: str) -> MaybeAwaitable: ...

    @overload
    def name(self) -> str: ...

    def name(self, *args):
        """name(name)
        name() -> str

        デバイスのBluetooth名を設定または取得します。

        Arguments:
            name (str): デバイスの新しいBluetooth名。名前が指定されない場合、
                このメソッドは現在の名前を返します。

        Raises:
            OSError: デバイスが接続されていない場合。
        """

    def write(self, buf: bytes) -> MaybeAwaitable:
        """write(buf)

        リモートハブにメッセージを送信します。

        Arguments:
            buf (bytes): 送信する生のバイナリメッセージ。最大20バイト。

        Raises:
            ValueError: メッセージが20バイトを超える場合。
            OSError: デバイスが接続されていない、または書き込みに失敗した
                場合。
        """

    def read(self) -> bytes | None:
        """read() -> bytes | None

        リモートハブから受信した最も古いバッファ内のメッセージを取得します。

        バッファ内のすべてのメッセージがすでに読み取られている場合は、
        ``None`` を返します。

        Returns:
            最も古い生のバイナリメッセージ。メッセージがない場合は ``None``。

        .. versionchanged:: 3.7

            新しいメッセージが1つ受信されるまでブロックする代わりに、
            バッファ内の複数のメッセージを読み取れるようになりました。
        """

    def disconnect(self) -> MaybeAwaitable:
        """disconnect()

        デバイスを切断します。

        Raises:
            OSError: 切断に失敗した場合。
        """


class XboxController:
    """Microsoft® Xbox®コントローラーをセンサーとして使用し、プロジェクトを
    リモートで操作します。

    ハブはコントローラーをスキャンして接続します。プログラムが終了すると
    切断されます。

    接続とペアリングに関するヒントについては、 :ref:`以下 <xbox-controller-pairing>` を参照してください。
    """

    buttons = _common.Keypad([])

    def __init__(
        self,
        joystick_deadzone: int = 10,
        name: str | None = None,
        timeout: int = 10000,
        connect: bool = True,
    ):
        """__init__(joystick_deadzone=10, name=None, timeout=10000, connect=True)

        Arguments:
            joystick_deadzone (Number, %): ジョイスティックのデッドゾーン
                （0から100）。両軸でこのしきい値を下回る値は、スティックの
                ドリフトを防ぐために0として報告されます。
            name (str): 接続するXboxコントローラーのBluetooth名。
                ``None`` を指定すると、利用可能な任意のコントローラーに
                接続します。
            timeout (Number, ms): 接続をあきらめるまでの待機時間。
                ``None`` を選択すると、無期限に待機します。
            connect (bool): コントローラーへの接続をスキップする場合は
                ``False`` を選択します。 ``connect()`` を後で呼び出して
                接続できます。
        """

    def connect(self) -> MaybeAwaitable:
        """connect()

        Xboxコントローラーに接続します。切断した場合、またはコントローラーを
        ``connect=False`` で初期化した場合にのみ必要です。
        """

    def disconnect(self) -> MaybeAwaitable:
        """disconnect()

        Xboxコントローラーを切断します。
        """

    def name(self) -> str:
        """name() -> str

        接続されているコントローラーのBluetooth名を取得します。

        Returns:
            コントローラーのBluetooth名。

        Raises:
            OSError: コントローラーが接続されていない場合。
        """

    def state(self) -> tuple:
        """state() -> tuple

        すべての生のコントローラー入力値を1つのタプルとして取得します。
        これにより、他のメソッドでは公開されていない値にアクセスできます。

        ジョイスティック軸（x、y、z、rz）は0を中心としています。トリガー軸は
        生の10ビット値（0-1023）です。

        Returns:
            ``(x, y, z, rz, left_trigger, right_trigger, dpad,
            buttons, upload, profile, trigger_switches, paddles)`` のタプル。

        Raises:
            OSError: コントローラーが接続されていない場合。
        """

    def joystick_left(self) -> tuple[int, int]:
        """joystick_left() -> tuple

        左ジョイスティックの位置を-100%から100%のパーセント値として
        取得します。中心位置は(0, 0)です。正方形のデッドゾーンが適用
        されます: 両軸がデッドゾーン内にある場合、両方とも0として
        報告されます。

        Returns:
            X（水平）とY（垂直）の位置のタプル。

        Raises:
            OSError: コントローラーが接続されていない場合。
        """

    def joystick_right(self) -> tuple[int, int]:
        """joystick_right() -> tuple

        右ジョイスティックの位置を-100%から100%のパーセント値として
        取得します。中心位置は(0, 0)です。正方形のデッドゾーンが適用
        されます: 両軸がデッドゾーン内にある場合、両方とも0として
        報告されます。

        Returns:
            X（水平）とY（垂直）の位置のタプル。

        Raises:
            OSError: コントローラーが接続されていない場合。
        """

    def triggers(self) -> tuple[int, int]:
        """triggers() -> tuple

        左右のトリガー位置を0%から100%のパーセント値として取得します。

        Returns:
            左右のトリガー位置のタプル。

        Raises:
            OSError: コントローラーが接続されていない場合。
        """

    def dpad(self) -> int:
        """dpad() -> int

        方向パッドの値を取得します。 ``1`` は上、 ``2`` は右上、 ``3`` は右、
        ``4`` は右下、 ``5`` は下、 ``6`` は左下、 ``7`` は左、 ``8`` は左上、
        ``0`` は押されていないことを示します。

        これは ``Button.UP`` 、 ``Button.RIGHT`` 、 ``Button.DOWN`` 、
        ``Button.LEFT`` ボタンの状態を読み取るのと本質的に同じですが、
        このメソッドは方向を示す数値を便利に返します。

        Returns:
            方向を示す方向パッドの位置。

        Raises:
            OSError: コントローラーが接続されていない場合。
        """

    def profile(self) -> int:
        """profile() -> int

        コントローラーの現在のプロファイルを取得します。
        Xbox Elite Controller Series 2でのみ利用可能です。

        Returns:
            プロファイル番号。

        Raises:
            OSError: コントローラーが接続されていない場合。
        """

    def rumble(
        self,
        power: Number | tuple[Number, Number, Number, Number] = 100,
        duration: int = 200,
        count: int = 1,
        delay: int = 100,
    ) -> MaybeAwaitable:
        """rumble(power=100, duration=200, count=1, delay=100)

        内蔵アクチュエーターを振動させ、フォースフィードバックを生成します。

        単一の ``power`` 値を指定すると、左右のメインアクチュエーターがともに
        その強さで振動し、トリガーアクチュエーターはオフのままになります。
        より細かく制御するには、 ``power`` に4つの値のタプルを設定します。
        それぞれ左メインアクチュエーター、右メインアクチュエーター、左トリガー
        アクチュエーター、右トリガーアクチュエーターを制御します。たとえば、
        ``power=(0, 0, 100, 0)`` は左トリガーを最大強度で振動させます。

        プログラムが続行する間、振動はバックグラウンドで実行されます。
        プログラムを待機させるには、対応する時間だけプログラムを一時停止
        してください。1回の振動の場合、これは ``duration`` に等しくなります。
        複数回の場合は ``count * (duration + delay)`` に等しくなります。

        すべてのアクチュエーターの強さが0の場合、 ``duration`` が0の場合、
        または ``count`` が1未満の場合、このメソッドは何もしません。

        Arguments:
            power (Number, % or tuple): 振動の強さ。単一の値は両方のメイン
                アクチュエーターに適用されます（0-100%）。タプルは（左ハンドル、
                右ハンドル、左トリガー、右トリガー）に個別に適用されます。
            duration (Number, ms): 各振動の時間。上限2500 ms。
            count (int): 振動の回数（0-100）。
            delay (Number, ms): 各振動の前の遅延。 ``count > 1`` の場合にのみ
                使用されます。上限2500 ms。
        """


# Hide type-only names from jedi completions in the module namespace.
if TYPE_CHECKING:
    del MaybeAwaitable
    del MaybeAwaitableBytes
    del MaybeAwaitableTuple
    del Number
    del Port
