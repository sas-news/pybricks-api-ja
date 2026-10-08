# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2023 The Pybricks Authors

"""ライト、ディスプレイ、スピーカー、バッテリーなどの一般的なデバイス向けの
汎用クロスプラットフォームモジュール。"""

from __future__ import annotations

from typing import TYPE_CHECKING, overload

from .parameters import Direction, Stop

if TYPE_CHECKING:
    from collections.abc import Awaitable, Collection, Iterable
    from typing import Any, TypeVar

    from .parameters import Axis, Button, Color, Number, Port, Side
    from .tools import Matrix

    _T_co = TypeVar("_T_co", covariant=True)

    class MaybeAwaitable(None, Awaitable[None]): ...

    # HACK: Cannot subclass bool, so using Any instead.
    class MaybeAwaitableBool(Any, Awaitable[bool]): ...

    class MaybeAwaitableFloat(float, Awaitable[float]): ...

    class MaybeAwaitableInt(int, Awaitable[int]): ...

    class MaybeAwaitableTuple(tuple[_T_co], Awaitable[tuple[_T_co]]): ...

    class MaybeAwaitableSet(set[_T_co], Awaitable[set[_T_co]]): ...

    class MaybeAwaitableColor(Color, Awaitable[Color]): ...

    class MaybeAwaitableBytes(bytes, Awaitable[bytes]): ...


class System:
    """ハブのシステム制御アクション。"""

    def set_stop_button(self, button: Button | Iterable[Button] | None) -> None:
        """
        set_stop_button(button)

        実行中のスクリプトを停止するボタンを設定します。

        通常、中央のボタンは実行中のスクリプトを停止するために使用されます。
        この仕様を変更または無効にして、ボタンを他の目的に使用することができます。

        Arguments:
            button (Button): :attr:`Button.CENTER <pybricks.parameters.Button.CENTER>` などのボタン、またはボタンのタプルを指定します。
                ``None`` を選択すると、ボタンを無効にします。
                無効にした場合は中央のボタンを3秒間長押しして、Hubの電源をオフにしてプログラムを停止することができます。
        """

    def shutdown(self) -> None:
        """shutdown()

        プログラムを停止し、ハブをシャットダウンします。"""

    @overload
    def storage(self, offset: int, *, read: int) -> bytes: ...

    @overload
    def storage(self, offset: int, *, write: bytes) -> None: ...

    def storage(self, offset, read=None, write=None):
        """
        storage(offset, write=)
        storage(offset, read=) -> bytes

        永続ストレージに対してバイナリデータの読み書きを行います。

        次回プログラムを実行したときにも使えるデータを保存できます。

        ハブを正常にオフにすると、データはフラッシュメモリに保存されます。
        ハブが *動作している間に* バッテリーを取り外した場合は保存されません。

        一度保存されたデータは、バッテリーを取り外した後でも利用できます。

        Args:
            offset (int): ユーザーストレージメモリの先頭からのオフセット（バイト単位）。
            read (int): 読み取るバイト数。書き込む場合はこの引数を省略します。
            write (bytes): 書き込むバイト列。読み取る場合はこの引数を省略します。

        Returns:
            読み取りの場合は読み取ったバイト列、それ以外の場合は ``None`` 。

        Raises:
            ValueError:
                許可された範囲外のデータを読み書きしようとした場合。
        """

    def reset_storage(self) -> None:
        """reset_storage()

        すべてのユーザー設定をデフォルト値にリセットし、ユーザーのプログラムを消去します。
        """

    def info(self) -> dict:
        """info() -> dict

        ハブに関する情報を、以下のキーを持つ辞書として取得します。

         - ``"name"``: ハブ名。Bluetooth経由で接続するときに表示される
           名前です。
         - ``"reset_reason"``: ハブが（再）起動した理由。ハブが前回正常に
           電源オフされていた場合は ``0`` です。ファームウェア更新後など、
           ハブが自動的に再起動した場合は ``1`` です。ハブが前回
           ウォッチドッグタイムアウトによってクラッシュした場合は ``2`` で、
           これはファームウェアの問題を示します。
         - ``"host_connected_ble"``: ハブがBluetooth経由でコンピューター、
           タブレット、スマートフォンのいずれかに接続されている場合は
           ``True`` 、それ以外は ``False`` 。
         - ``"host_connected_usb"``: ハブがUSB経由でコンピューターに接続され、
           アプリでアクティブになっている場合は ``True`` 。
           それ以外は ``False`` 。
         - ``"program_start_type"``: ハブの電源投入時にプログラムが自動的に
           開始された場合は ``1`` 。ハブのボタンでプログラムが開始された
           場合は ``2`` 。接続したコンピューターからプログラムが開始された
           場合は ``3`` 。
         - `"program_id"`: 現在実行中のプログラムの（スロット）番号。

        Returns:
            システム情報を含む辞書。

        .. versionchanged:: 3.6
            名前とリセット理由は、以前は個別のメソッドとして利用できました。
            現在は ``info`` 辞書に含まれています。これらのメソッドは
            後方互換性のために引き続き利用できます。
        """


class DCMotor:
    """回転センサーのないトレインモーターなどのシンプルなモーターを制御する
    汎用クラス。"""

    def __init__(self, port: Port, positive_direction: Direction = Direction.CLOCKWISE):
        """__init__(port, positive_direction=Direction.CLOCKWISE)

        Arguments:
            port (Port): モーターが接続されているポート。
            positive_direction (Direction): 正のデューティサイクル値を与えた
                ときにモーターが回転する方向。
        """

    def dc(self, duty: Number) -> None:
        """dc(duty)

        指定したデューティサイクル（「パワー」とも呼ばれます）でモーターを
        回転させます。

        Arguments:
            duty (Number, %): デューティサイクル（-100.0から100）。
        """

    def stop(self) -> None:
        """stop()

        モーターを停止し、自由に回転できる状態にします。

        モーターは摩擦によって徐々に停止します。"""

    def brake(self) -> None:
        """brake()

        モーターに受動的なブレーキをかけます。

        モーターは摩擦と、まだ動いている間に発生する電圧によって
        停止します。"""

    @overload
    def settings(self, max_voltage: Number) -> None: ...

    @overload
    def settings(self) -> tuple[int]: ...

    def settings(self, *args):
        """
        settings(max_voltage)
        settings() -> tuple[int]

        モーターの設定を構成します。引数が指定されない場合は、
        現在の値を返します。

        Arguments:
            max_voltage (Number, mV):
                すべてのモーターコマンドでモーターに印加される最大電圧。
        """


class Control:
    """PIDコントローラーとその設定を操作するクラス。"""

    scale: int

    """
    制御対象の整数変数と物理出力との間のスケーリング係数。
    たとえば、単一のモーターの場合、これは回転1度あたりの
    エンコーダーパルス数です。
    """

    @overload
    def limits(
        self,
        speed: Number | None = None,
        acceleration: Number | None = None,
        torque: Number | None = None,
    ) -> None: ...

    @overload
    def limits(self) -> tuple[int, int, int]: ...

    def limits(self, *args):
        """
        limits(speed, acceleration, torque)
        limits() -> tuple[int, int, int]

        最大速度、加速度、トルクを設定します。

        引数が指定されない場合は、現在の値を返します。

        新しい ``acceleration`` と ``speed`` の制限は、新しいモーター
        コマンドを与えたときに有効になります。進行中の操作には
        影響しません。

        Arguments:
            speed (Number, deg/s or Number, mm/s):
                最大速度。すべての速度コマンドはこの値に制限されます。
            acceleration (Number, deg/s² or Number, mm/s²):
                加速または減速時の速度カーブの傾き。タプルを使って
                加速と減速を個別に設定できます。1つの値のみ指定した
                場合は両方に使用されます。
            torque (:ref:`torque`):
                制御中の最大フィードバックトルク。
        """

    @overload
    def pid(
        self,
        kp: Number | None = None,
        ki: Number | None = None,
        kd: Number | None = None,
        integral_deadzone: Number | None = None,
        integral_rate: Number | None = None,
    ) -> None: ...

    @overload
    def pid(self) -> tuple[int, int, int, int, int]: ...

    def pid(self, *args):
        """pid(kp, ki, kd, integral_deadzone, integral_rate)
        pid() -> tuple[int, int, int, int, int]

        位置制御と速度制御のPID値を取得または設定します。

        引数が指定されない場合は、現在の値を返します。

        Arguments:
            kp (int): 比例位置制御定数。誤差1度あたりの
                フィードバックトルク（µNm/deg）。
            ki (int): 積分位置制御定数。累積した誤差の度数あたりの
                フィードバックトルク（µNm/(deg s)）。
            kd (int): 微分位置（または比例速度）制御定数。
                速度の単位あたりのフィードバックトルク（µNm/(deg/s)）。
            integral_deadzone (Number, deg or Number, mm): 誤差積分が
                誤差を累積しない、目標周辺の領域。
            integral_rate (Number, deg/s or Number, mm/s): 誤差積分が
                増加できる最大レート。
        """

    @overload
    def target_tolerances(
        self, speed: Number | None = None, position: Number | None = None
    ) -> None: ...

    @overload
    def target_tolerances(self) -> tuple[int, int]: ...

    def target_tolerances(self, *args):
        """target_tolerances(speed, position)
        target_tolerances() -> tuple[int, int]

        操作が完了したとみなす許容誤差を取得または設定します。

        引数が指定されない場合は、現在の値を返します。

        Arguments:
            speed (Number, deg/s or Number, mm/s): 動作が完了したと
                みなされるまでの、ゼロ速度からの許容偏差。
            position (Number, deg or :ref:`distance`): 動作が完了したと
                みなされるまでの、目標からの許容偏差。
        """

    @overload
    def stall_tolerances(
        self, speed: Number | None = None, time: Number | None = None
    ) -> None: ...

    @overload
    def stall_tolerances(self) -> tuple[int, int]: ...

    def stall_tolerances(self, speed, time):
        """stall_tolerances(speed, time)
        stall_tolerances() -> tuple[int, int]

        ストール判定の許容値を取得または設定します。

        引数が指定されない場合は、現在の値を返します。

        Arguments:
            speed (Number, deg/s or Number, mm/s): 最大の駆動出力でも
                ``time`` の間この速度に達しない場合、ストールしたと
                みなされます。
            time (Number, ms): コントローラーがこの最小 ``speed`` を
                下回り続けた場合に、ストールしたとみなすまでの時間。
        """


class Model:
    """モーターの状態オブザーバーとその設定を操作するクラス。"""

    def state(self) -> tuple[float, float, float, bool]:
        """state() -> tuple[float, float, float, bool]

        実際のモーターを模倣したシミュレーションモデルを使って、
        モーターの推定角度、速度、電流、ストール状態を取得します。
        これらの推定値は実際の測定値よりも速く更新されるため、独自の
        PIDコントローラーを構築する際に便利です。

        ほとんどのアプリケーションでは、代わりに *測定された*
        :meth:`angle <pybricks.pupdevices.Motor.angle>` 、
        :meth:`speed <pybricks.pupdevices.Motor.speed>` 、
        :meth:`load <pybricks.pupdevices.Motor.load>` 、および
        :meth:`stall <pybricks.pupdevices.Motor.stalled>` の状態を
        使用する方が適しています。

        Returns:
            推定角度（deg）、速度（deg/s）、電流（mA）、ストール状態
            （``True`` または ``False`` ）のタプル。
        """

    @overload
    def settings(self, values: tuple) -> None: ...

    @overload
    def settings(self) -> tuple: ...

    def settings(self, speed, time):
        """settings(values)
        settings() -> tuple

        モデルの設定を整数のタプルとして取得または設定します。引数が
        指定されない場合は、現在の値を返します。このメソッドは主に
        モーターモデルクラスのデバッグに使用されます。ユーザープログラムで
        これらの設定を変更する必要はありません。

        .. _model settings: https://docs.pybricks.com/projects/pbio/en/latest/struct__pbio__observer__settings__t.html

        Arguments:
            values (tuple): `model settings`_ のタプル。
        """


class Motor(DCMotor):
    """回転センサーを内蔵したモーターを制御する汎用クラス。"""

    control = Control()
    """モーターはPID制御を使って、指定した速度と角度の目標を正確に
    追跡します。モーターの ``control`` 属性を通じてその動作を変更できます。
    利用可能なメソッドの概要は :ref:`control` を参照してください。"""

    model = Model()
    """モーターの状態を推定するオブザーバーを表すモデル。"""

    def __init__(
        self,
        port: Port,
        positive_direction: Direction = Direction.CLOCKWISE,
        gears: Collection[int] | Collection[Collection[int]] | None = None,
        reset_angle: bool = True,
        profile: Number = None,
    ):
        """__init__(port, positive_direction=Direction.CLOCKWISE, gears=None, reset_angle=True, profile=None)

        Arguments:
            port (Port): モーターが接続されているポート。
            positive_direction (Direction): 正の速度値や角度を与えたときに
                モーターが回転する方向。
            gears (list):
                モーターに連結されたギアのリスト。モーターに接続された
                ギアが最初に来て、出力に接続されたギアが最後に来ます。

                たとえば ``[12, 36]`` は、モーターに接続された12歯の
                ギアと出力に接続された36歯のギアからなるギア列を
                表します。複数のギア列には
                ``[[12, 36], [20, 16, 40]]`` のようなリストのリストを
                使います。

                ギア列を指定すると、すべてのモーターコマンドと設定が、
                得られるギア比を考慮して自動的に調整されます。
                モーターの回転方向はこれによって変わりません。
            reset_angle (bool):
                ``True`` を選択すると、回転センサー値を絶対マーカー角度
                （-180から179の間）にリセットします。
                ``False`` を選択すると、現在の値を維持するため、
                プログラムは前回停止した位置を認識できます。
            profile (Number, deg): 精度プロファイル。アプリケーションで
                許容できるおおよその位置許容誤差（度）です。値が小さい
                ほど正確ですが動作が不安定になり、値が大きいほど精度は
                下がりますが動作が滑らかになります。値を指定しない場合は、
                このモータータイプに適したプロファイルが自動的に
                選択されます（約11度）。
        """

    def angle(self) -> int:
        """angle() -> int: deg

        モーターの回転角を取得します。

        Returns:
            モーターの角度。
        """

    def speed(self, window: Number = 100) -> int:
        """speed(window=100) -> int: deg/s

        モーターの速度を取得します。

        速度は、指定された時間ウィンドウ内でのモーター角度の変化として
        測定されます。ウィンドウが短いと速度値はモーターの動きに敏感に
        なりますが、安定しにくくなります。ウィンドウが長いと速度値の
        応答性は下がりますが、より安定します。

        Arguments:
            window (Number, ms): 速度を求めるために使用する時間ウィンドウ。

        Returns:
            モーターの速度。

        """

    def stalled(self) -> bool:
        """stalled() -> bool

        モーターが現在ストールしているかどうかを確認します。

        最大の駆動信号を与えても目標速度または目標位置に到達できない
        場合に、ストールしているとみなされます。

        Returns:
            モーターがストールしている場合は ``True`` 、そうでなければ
            ``False`` 。
        """

    def load(self) -> int:
        """load() -> int: mNm

        モーターが動こうとするときに、それを妨げる負荷を推定します。

        Returns:
            負荷トルク。
        """

    def reset_angle(self, angle: Number | None) -> None:
        """
        reset_angle(angle)

        モーターの累積回転角を目的の値に設定します。

        このモーターがドライブベースでも使用されている場合、その距離と
        角度の値も影響を受けます。代わりに
        :meth:`reset <pybricks.robotics.DriveBase.reset>` メソッドを
        使うとよいでしょう。

        Arguments:
            angle (Number, deg): 角度をリセットする値。
        """

    def hold(self) -> None:
        """hold()

        モーターを停止し、現在の角度で能動的に保持します。"""

    def run(self, speed: Number) -> None:
        """run(speed)

        モーターを一定速度で回転させます。

        モーターは指定された速度まで加速し、新しいコマンドを与えるまで
        その速度で回転し続けます。

        Arguments:
            speed (Number, deg/s): モーターの速度。
        """

    def run_time(
        self, speed: Number, time: Number, then: Stop = Stop.HOLD, wait: bool = True
    ) -> MaybeAwaitable:
        """run_time(speed, time, then=Stop.HOLD, wait=True)

        モーターを指定された時間だけ一定速度で回転させます。

        モーターは指定された速度まで加速し、その速度で回転を維持した後、
        減速します。操作全体は、指定された ``time`` ちょうどの時間
        続きます。

        Arguments:
            speed (Number, deg/s): モーターの速度。
            time (Number, ms): 操作の継続時間。
            then (Stop): 静止した後に行う動作。
            wait (bool): 操作が完了するまで待ってからプログラムの残りを
                続行します。
        """

    def run_angle(
        self,
        speed: Number,
        rotation_angle: Number,
        then: Stop = Stop.HOLD,
        wait: bool = True,
    ) -> MaybeAwaitable:
        """run_angle(speed, rotation_angle, then=Stop.HOLD, wait=True)

        モーターを一定速度で指定された角度だけ回転させます。

        Arguments:
            speed (Number, deg/s): モーターの速度。
            rotation_angle (Number, deg): モーターが回転する角度。
            then (Stop): 静止した後に行う動作。
            wait (bool): 操作が完了するまで待ってからプログラムの残りを
                続行します。
        """

    def run_target(
        self,
        speed: Number,
        target_angle: Number,
        then: Stop = Stop.HOLD,
        wait: bool = True,
    ) -> MaybeAwaitable:
        """run_target(speed, target_angle, then=Stop.HOLD, wait=True)

        モーターを一定速度で指定された目標角度に向かって回転させます。

        回転方向は目標角度に基づいて自動的に選択されます。
        ``speed`` が正か負かは関係ありません。

        Arguments:
            speed (Number, deg/s): モーターの速度。
            target_angle (Number, deg): モーターが回転する目標角度。
            then (Stop): 静止した後に行う動作。
            wait (bool): モーターが目標に到達するまで待ってから
                プログラムの残りを続行します。
        """

    def run_until_stalled(
        self,
        speed: Number,
        then: Stop = Stop.COAST,
        duty_limit: Number | None = None,
    ) -> MaybeAwaitableInt:
        """
        run_until_stalled(speed, then=Stop.COAST, duty_limit=None) -> int: deg

        モーターをストールするまで一定速度で回転させます。

        Arguments:
            speed (Number, deg/s): モーターの速度。
            then (Stop): 静止した後に行う動作。
            duty_limit (Number, %): このコマンド実行中のデューティ
                サイクル制限。ギア機構やレバー機構にモーターの最大
                トルクをかけないようにするのに便利です。``None`` の
                場合、このコマンド実行中にデューティ制限は変更されません。

        Returns:
            モーターがストールしたときの角度。
        """

    def done(self) -> bool:
        """done() -> bool

        進行中のコマンドまたは操作が完了したかどうかを確認します。

        Returns:
            コマンドが完了していれば ``True`` 、そうでなければ
            ``False`` 。
        """

    def track_target(self, target_angle: Number) -> None:
        """track_target(target_angle)

        目標角度を追跡します。これは :meth:`.run_target` と
        似ていますが、通常の滑らかな加速はスキップされ、可能な限り速く
        目標角度に移動します。このメソッドは、目標角度を連続的に
        変更したい場合に便利です。

        Arguments:
            target_angle (Number, deg): モーターが回転する目標角度。
        """

    def close(self) -> None:
        """close()

        モーターオブジェクトを閉じて、再度 ``Motor`` を呼び出して
        新しいオブジェクトを初期化できるようにします。

        これにより、上級ユーザーはプログラムの途中でギアなどの
        プロパティを変更できます。取り外し可能なアタッチメントに
        便利です。
        """


class Speaker:
    """スピーカーを使ってビープ音やサウンドを再生します。"""

    @overload
    def volume(self, volume: Number) -> None: ...

    @overload
    def volume(self) -> int: ...

    def volume(self, *args):
        """volume(volume)
        volume() -> int: %

        スピーカーの音量を取得または設定します。

        音量を指定しない場合、このメソッドは現在の音量を返します。

        Arguments:
            volume (Number, %): 0から100の範囲のスピーカーの音量。
        """

    def beep(self, frequency: Number = 500, duration: Number = 100) -> MaybeAwaitable:
        """beep(frequency=500, duration=100)

        ビープ音/トーンを再生します。

        Arguments:
            frequency (Number, Hz):
                64から24000 Hzの範囲のビープ音の周波数。
            duration (Number, ms):
                ビープ音の長さ。長さが0未満の場合、このメソッドは
                直ちに戻り、その周波数の再生が無期限に続きます。
        """

    def play_notes(self, notes: Iterable[str], tempo: Number = 120) -> MaybeAwaitable:
        """play_notes(notes, tempo=120)

        一連の音符を再生します。例：
        ``["C4/4", "C4/4", "G4/4", "G4/4"]`` 。

        各音符は次の形式の文字列です。

            - 最初の文字は音名で、 ``A`` から ``G`` 、または休符を表す
              ``R`` です。
            - 音名にはシャープの ``#`` やフラットの ``b`` の臨時記号を
              含めることもできます。``B#`` / ``Cb`` と ``E#`` / ``Fb``
              は使用できません。
            - 音名の後には ``2`` から ``8`` のオクターブ番号が続きます。
              たとえば ``C4`` は中央のCです。オクターブは音Cで次の番号に
              変わります。たとえば ``B3`` は中央のC（ ``C4`` ）のすぐ
              下の音です。
            - オクターブの後には ``/`` と音符の長さを示す数字が続きます。
              たとえば ``/4`` は4分音符、 ``/8`` は8分音符、という具合です。
            - オプションで ``.`` を続けて付点音符にできます。付点音符は
              点のない音符の1.5倍の長さです。
            - オプションで音符の末尾に ``_`` を付けると、タイまたは
              スラーになります。これにより、この音符と次の音符の間に
              休止が入らなくなります。

        Arguments:
            notes (iter):
                再生する音符のシーケンス。
            tempo (int):
                1分あたりの拍数。4分音符が1拍です。
        """


class ColorLight:
    """多色ライトを制御します。"""

    def on(self, color: Color) -> None:
        """on(color)

        指定した色でライトを点灯します。

        Arguments:
            color (Color): ライトの色
        """

    def off(self) -> None:
        """off()

        ライトを消します。
        """

    def blink(self, color: Color, durations: Collection[Number]) -> None:
        """blink(color, durations)

        ライトを一定時間、指定した色で点滅させます。

        ライトはプログラム実行中、バックグラウンドでずっと点滅し続けます。

        このメソッドでは、簡単で便利な点滅パターンを作成できます。
        より複雑なパターンを作成するには、代わりに ``animate()`` を使用してください。

        Arguments:
            color (Color): ライトの色
            durations (list): ``[on_1, off_1, on_2, off_2, ...]`` といった形式で時間値を指定します。
        """

    def animate(self, colors: Collection[Color], interval: Number) -> None:
        """animate(colors, interval)

        指定された間隔で1つずつ表示される色のシーケンスでライトをアニメーション化します。

        アニメーションはバックグラウンドで実行されます。
        アニメーションが完了すると最初に戻り、繰り返されます。

        Arguments:
            colors (list): :class:`Color <.parameters.Color>` のシーケンス
            interval (Number, ms): 色の更新間隔
        """


class ExternalColorLight:
    """多色ライトを制御します。"""

    def on(self, color: Color) -> MaybeAwaitable:
        """on(color)

        指定した色でライトを点灯します。

        Arguments:
            color (Color): ライトの色。
        """

    def off(self) -> MaybeAwaitable:
        """off()

        ライトを消します。
        """


class LightArray3:
    """3つの単色ライトの配列を制御します。"""

    def on(self, brightness: Number | tuple[Number, Number, Number]) -> MaybeAwaitable:
        """on(brightness)

        指定した輝度でライトを点灯します。

        Arguments:
            brightness (Number or tuple, %):
                単一の値ですべてのライトの輝度を同時に設定します。
                3つの値のタプルで各ライトの輝度を個別に設定します。
        """

    def off(self) -> MaybeAwaitable:
        """off()

        すべてのライトを消します。
        """


class LightArray4(LightArray3):
    """4つの単色ライトの配列を制御します。"""

    def on(
        self, brightness: Number | tuple[Number, Number, Number, Number]
    ) -> MaybeAwaitable:
        """on(brightness)

        指定した輝度でライトを点灯します。

        Arguments:
            brightness (Number or tuple, %):
                単一の値ですべてのライトの輝度を同時に設定します。
                4つの値のタプルで各ライトの輝度を個別に設定します。
                ライトの順序は上の画像に示されています。
        """


class LightMatrix:
    """単色ライトの長方形グリッドを制御します。"""

    def __init__(self, rows: int, columns: int):
        """LightMatrix(rows, columns)

        ライトマトリクスディスプレイを初期化します。

        Arguments:
            rows (int): グリッドの行数。
            columns (int): グリッドの列数。
        """

    def orientation(self, up: Side) -> None:
        """orientation(up)

        ライトマトリクスの表示を回転させます。

        実行後、新たに表示されるピクセルだけが影響を受けます。
        既存の表示内容は変化しません。

        Arguments:
            up (Side): デザインにおいてライトマトリクスディスプレイの
                どの面が「上」になるかを指定します。``Side.TOP`` 、
                ``Side.LEFT`` 、 ``Side.RIGHT`` 、 ``Side.BOTTOM`` の
                いずれかを選択します。
        """

    def icon(self, icon: Matrix) -> None:
        """icon(icon)

        :ref:`brightness` の輝度でアイコンを表示します。

        Arguments:
            icon (Matrix): 強度のマトリクス（:ref:`brightness`）。2Dリストも受け付けます。
        """

    def animate(self, matrices: Collection[Matrix], interval: Number) -> None:
        """animate(matrices, interval)

        画像のリストを使って作られたアニメーションを表示します。

        各画像は上記と同じフォーマットです。
        それぞれの画像は与えられた間隔だけ表示されます。
        このアニメーションは、プログラムの残りの部分が動き続けている間、永遠に繰り返されます。

        Arguments:
            matrices (iter): :class:`Matrix <pybricks.tools.Matrix>` のシーケンス。
            interval (Number, ms): リスト内の各画像を表示する時間。
        """

    def pixel(self, row: Number, column: Number, brightness: Number = 100) -> None:
        """pixel(row, column, brightness=100)

        指定された明るさで1つのピクセルをオンにします。

        Arguments:
            row (Number): 垂直方向の座標。上から0で始まります。
            column (Number): 水平方向の座標。左から0で始まります。
            brightness (Number :ref:`brightness`): ピクセルの明るさ。
        """

    def off(self) -> None:
        """off()

        すべてのピクセルをオフにします。"""

    def number(self, number: Number) -> None:
        """number(number)

        -99から99の範囲の数字を表示します。

        マイナス記号（``-``）はディスプレイの中央に点で表示されます。
        99以上の数字は ``>`` 、99未満の数字は ``<`` で表示されます。

        Arguments:
            number (int): 表示する数字。
        """

    def char(self, char: str) -> None:
        """char(char)

        ライトマトリクスに文字または記号を表示します。
        任意の文字（``a`` から ``z``、``A`` から ``Z``）または以下の記号を表示できます。

        ``!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}``

        Arguments:
            char (str): 表示する文字または記号。
        """

    def text(self, text: str, on: Number = 500, off: Number = 50) -> None:
        """text(text, on=500, off=50)

        テキストを1文字ずつ表示します。
        最後の文字が表示された後にすべてのライトが消灯します。

        Arguments:
            text (str): 表示するテキスト。
            on (Number, ms): 1文字が表示される時間。
            off (Number, ms): 文字と文字の間の表示が消えている時間。
        """


class Keypad:
    """キーパッドレイアウトのボタンの状態を取得します。"""

    def __init__(self, active_buttons): ...

    def pressed(self) -> set[Button]:
        """pressed() -> set[Button]

        現在どのボタンが押されているか取得します。

        Returns:
            押されたボタンのセット。
        """


class Battery:
    """バッテリーの状態を取得します。"""

    def voltage(self) -> int:
        """voltage() -> int: mV

        バッテリーの電圧を取得します。

        Returns:
            バッテリーの電圧。
        """

    def current(self) -> int:
        """current() -> int: mA

        バッテリーから供給される電流を取得します。

        Returns:
            バッテリーの電流。
        """


class Charger:
    """バッテリー充電器の状態を取得します。"""

    def connected(self) -> bool:
        """connected() -> bool

        充電器がUSB経由で接続されているかどうかを確認します。

        Returns:
            充電器が接続されている場合は ``True`` 、そうでなければ
            ``False`` 。
        """

    def status(self) -> int:
        """status() -> int

        バッテリー充電器の状態を取得します。状態は以下のいずれかの値で
        表されます。これはUSBポートのすぐ隣にあるバッテリーライト
        インジケーターに対応しています。

            0. 充電していない（ライト消灯）。
            1. 充電中（ライトは赤）。
            2. 充電完了（ライトは緑）。
            3. 充電器に問題がある（ライトは黄）。

        Returns:
            状態値。
        """

    def current(self) -> int:
        """current() -> int: mA

        充電電流を取得します。

        Returns:
            充電電流。
        """


class SimpleAccelerometer:
    """加速度計から測定値を取得します。"""

    def acceleration(self) -> tuple[int, int, int]:
        """acceleration() -> tuple[int, int, int]: mm/s²

        デバイスの加速度を取得します。

        Returns:
            3軸すべてに沿った加速度。
        """

    def up(self) -> Side:
        """up() -> Side

        Hubのどの面が上を向いているかを取得します。

        Returns:
            ``Side.TOP``、``Side.BOTTOM``、``Side.LEFT``、``Side.RIGHT``、
            ``Side.FRONT``、``Side.BACK`` のいずれか。
        """

    def tilt(self) -> tuple[int, int]:
        """tilt() -> tuple[int, int]

        ピッチ角とロール角を取得します。これは :ref:`ユーザーが指定した方向 <robotframe>` からの相対値です。

        回転の順序は、ピッチ-ターン-ロールです。これはロボットのY軸に沿って正回転し、次にX軸に沿って正回転することに相当します。

        Returns:
            ピッチ角とロール角を度単位で表したタプル。
        """


class IMU:
    def up(self, calibrated: bool = True) -> Side:
        """up(calibrated=True) -> Side

        現在ハブのどの面が上を向いているかを確認します。

        Arguments:
            calibrated (bool): ``True`` を選択すると、キャリブレーション済みの
                ジャイロスコープと加速度計のデータを使って上方向を判定します。
                ``False`` を選択すると、生の加速度値を使用します。

        Returns:
            ``Side.TOP`` 、 ``Side.BOTTOM`` 、 ``Side.LEFT`` 、
            ``Side.RIGHT`` 、 ``Side.FRONT`` 、 ``Side.BACK`` のいずれか。
        """

    def tilt(self, calibrated: bool = True) -> tuple[int, int]:
        """tilt(calibrated=True) -> tuple[int, int]

        ピッチ角とロール角を取得します。これは
        :ref:`ユーザーが指定した方向 <robotframe>` からの相対値です。

        回転の順序は、ピッチ-ターン-ロールです。これはロボットのY軸に
        沿って正回転し、次にX軸に沿って正回転することに相当します。

        Arguments:
            calibrated (bool): ``True`` を選択すると、キャリブレーション済みの
                ジャイロスコープと加速度計のデータを使って傾きを判定します。
                ``False`` を選択すると、生の加速度値を使用します。

        Returns:
            ピッチ角とロール角を度単位で表したタプル。
        """

    @overload
    def acceleration(self, axis: Axis = None, calibrated: bool = True) -> float: ...

    @overload
    def acceleration(self, calibrated: bool = True) -> Matrix: ...

    def acceleration(self, *args):
        """
        acceleration(axis, calibrated=True) -> float: mm/s²
        acceleration(calibrated=True) -> vector: mm/s²

        :ref:`ロボットフレーム <robotframe>` における、指定された軸に沿ったデバイスの加速度を取得します。

        Arguments:
            axis (Axis): 加速度を測定する軸。``None`` の場合はすべての軸に
                沿ったベクトルを返します。
            calibrated (bool): ``True`` を選択すると、キャリブレーション済みの
                加速度値を使用します。``False`` を選択すると、生の加速度値を
                使用します。

        Returns:
            指定された軸に沿った加速度。軸を指定しない場合は、すべての軸に沿った加速度のベクトルを返します。
        """

    def ready(self) -> bool:
        """ready() -> bool

        IMUが使用可能かどうかを確認します。

        これは、ロボットが数秒間静止しているときに ``True`` になり、デバイスを再較正することができます。
        ハブが起動したばかりであったり、10分以上較正の機会がなかったりすると ``False`` になります。

        Returns:
            使用可能であれば ``True``、そうでなければ ``False``。
        """

    def stationary(self) -> bool:
        """stationary() -> bool

        現在のハブが静止しているかどうかを確認します。

        Returns:
            少なくとも1秒間静止していれば ``True``、動いていれば ``False``。
        """

    @overload
    def settings(
        self,
        *,
        angular_velocity_threshold: float | None = None,
        acceleration_threshold: float | None = None,
        heading_correction: float | None = None,
        angular_velocity_bias: tuple[float, float, float] | None = None,
        angular_velocity_scale: tuple[float, float, float] | None = None,
        acceleration_correction: tuple[float, float, float, float, float, float]
        | None = None,
    ) -> None: ...

    @overload
    def settings(
        self,
    ) -> tuple[
        float,
        float,
        float,
        tuple[float, float, float],
        tuple[float, float, float],
        tuple[float, float, float, float, float, float],
    ]: ...

    def settings(self, *args):
        """
        settings(*, angular_velocity_threshold, acceleration_threshold, heading_correction, angular_velocity_bias, angular_velocity_scale, acceleration_correction)
        settings() -> tuple

        IMUの設定を構成します。引数が指定されない場合は、現在の値を
        返します。将来のリリースで設定が追加または変更される可能性が
        あるため、正しい動作を確実にするには各値をキーワード引数で
        指定してください。

        これらのIMU設定はハブに保存されます。再度変更するまで値は
        保持されます。ハブを別のファームウェアバージョンに更新するか、
        ``hub.system.reset_storage`` メソッドを呼び出すと、値は
        デフォルト値にリセットされます。

        ``angular_velocity_threshold`` と ``acceleration_threshold``
        は、ハブが静止しているとみなされる条件を定義します。すべての
        測定値が1秒間これらのしきい値を下回り続けると、IMUは自分自身を
        再キャリブレーションします。周囲の振動が大きい騒がしい場所
        （競技会場など）では、しきい値を少し上げることで、ロボットが
        キャリブレーションする機会を与えられます。設定が期待どおりに
        機能していることを確認するには、ロボットが動いているときに
        ``stationary()`` メソッドが ``False`` を返し、静止しているときに
        ``True`` を返すことをテストしてください。

        ジャイロスコープはハブの回転速度を測定して総角度を推定します。
        製造過程のばらつきにより、各ハブは1回転に対して一貫して異なる値を
        報告します。たとえば、あるハブは `360` 度の回転ごとに常に
        `357` 度を報告するかもしれません。この値は
        ``hub.imu.rotation(-Axis.Z, calibrated=False)`` で測定でき、
        ``heading_correction`` 設定として入力できます。すると、
        ``hub.imu.heading()`` メソッドはそれ以降その値を考慮し、
        1回転を正しく360度にスケーリングします。

        Arguments:
            angular_velocity_threshold (Number, deg/s): これを下回る
                角速度の変動であれば、ハブはキャリブレーションできるほど
                静止しているとみなされるというしきい値。
                リセット後の値は2 deg/sです。
            acceleration_threshold (Number, mm/s²): これを下回る
                加速度の変動であれば、ハブはキャリブレーションできるほど
                静止しているとみなされるというしきい値。
                リセット後の値は2500 mm/s²です。
            heading_correction (Number, deg): ロボットが1回転したときに
                報告される度数。リセット後の値は360度です。これは
                ``angular_velocity_scale`` 設定によるスケーリングに
                加えて適用されます。
            angular_velocity_bias (tuple, deg/s): 起動直後のx、y、z軸に
                沿った角速度測定の初期バイアス。
                リセット後の値は(0, 0, 0) deg/sです。
            angular_velocity_scale (tuple, deg): 製造差異を考慮するための
                x、y、z回転のスケール調整。リセット後の値は
                (360, 360, 360) deg/sです。正しい値は
                `hub.imu.rotation(Axis.X, calibrated=False)` を使い、
                各軸について繰り返すことで得られます。
            acceleration_correction (tuple, mm/s²): 製造差異を考慮する
                ためのx、y、zの両方向における重力の大きさのスケール調整。
                リセット後の値は
                (9806.65, -9806.65, 9806.65, -9806.65, 9806.65, -9806.65) mm/s²です。
                正しい値は
                `hub.imu.acceleration(Axis.X, calibrated=False)` を使い、
                すべての軸の両方向について繰り返すことで得られます。
        """

    def heading(self) -> float:
        """heading() -> float: deg

        ロボットの水平面での角度(方位角)を取得します。 正の値は時計回りを意味します。

        プログラム開始時の値は0です。この値はロボットが180度以上回転しても増え続けます。-180度まで折り返すことはありません。

        Returns:
            開始方位に対するロボットの方位角。

        """

    def reset_heading(self, angle: Number) -> None:
        """reset_heading(angle)

        ロボットの方位角をリセットします。

        ドライブベースがジャイロを使って走行または位置保持を行っている間は、
        このメソッドを呼び出せません。
        代わりに :meth:`DriveBase.reset() <pybricks.robotics.DriveBase.reset>`
        を使用してください。これはロボットを停止させてから、新しい方位角を
        設定します。

        .. versionchanged:: 3.6 走行中の角度リセットは許可されていません。先に停止してください。

        Arguments:
            angle (Number, deg): 方位角をリセットする値。

        Raises:
            OSError:
                現在ジャイロを使用しているドライブベースがある場合。
        """

    @overload
    def angular_velocity(self, axis: Axis = None, calibrated: bool = True) -> float: ...

    @overload
    def angular_velocity(self, calibrated: bool = True) -> Matrix: ...

    def angular_velocity(self, *args):
        """
        angular_velocity(axis, calibrated=True) -> float: deg/s
        angular_velocity(calibrated=True) -> vector: deg/s

        :ref:`ロボットフレーム <robotframe>` における、指定された軸に沿ったデバイスの角速度を取得します。

        Arguments:
            axis (Axis): 角速度を測定する軸。``None`` の場合はすべての軸に
                沿ったベクトルを返します。
            calibrated (bool): ``True`` を選択すると、推定されたバイアスと
                設定されたジャイロスコープのスケールを補正します。
                ``False`` を選択すると、生の角速度値を取得します。

        Returns:
            指定された軸に沿った角速度。軸を指定しない場合は、すべての軸に沿った角速度のベクトルを返します。
        """

    def rotation(self, axis: Axis, calibrated: bool = True) -> float:
        """
        rotation(axis, calibrated=True) -> float: deg

        :ref:`ロボットフレーム <robotframe>` における、指定された軸に沿ったデバイスの回転を取得します。

        この値は、ロボットが要求された軸に沿ってのみ回転する場合に便利です。
        一般的な3次元モーションの場合は、代わりに ``orientation()`` メソッドを使用します。

        Arguments:
            axis (Axis): 回転を測定する軸。
            calibrated (bool): ``True`` を選択すると、設定された
                ジャイロスコープのスケールを補正します。``False`` を
                選択すると、スケールされていない値を取得します。

        Returns:
            回転した角度。
        """

    def orientation(self) -> Matrix:
        """
        orientation() -> Matrix

        :ref:`ロボットフレーム <robotframe>` における、ロボットの3次元姿勢を取得する。

        ロボットの ``X`` 軸、``Y`` 軸、``Z`` 軸を表す回転行列を返します。

        Returns:
            3x3の回転行列。
        """


class CommonColorSensor:
    """Pybricksのカラーキャリブレーションをサポートする汎用カラーセンサー。"""

    def __init__(self, port: Port):
        """__init__(port)

        Arguments:
            port (Port): センサーが接続されているポート。
        """

    def color(self) -> MaybeAwaitableColor:
        """color() -> Color

        表面の色をスキャンします。

        検出する色は ``detectable_colors()`` メソッドで選択します。
        デフォルトでは ``Color.RED`` 、 ``Color.YELLOW`` 、
        ``Color.GREEN`` 、 ``Color.BLUE`` 、 ``Color.WHITE`` 、
        ``Color.NONE`` を検出します。

        Returns:
            検出された色。
        """

    def hsv(self) -> MaybeAwaitableColor:
        """hsv() -> Color

        表面の色をスキャンします。

        このメソッドは ``color()`` に似ていますが、最も近い検出可能な色に
        丸めるのではなく、色相、彩度、輝度の全範囲の値を返します。

        Returns:
            測定された色。色は色相（0--359）、彩度（0--100）、
            輝度（0--100）で表されます。
        """

    def ambient(self) -> MaybeAwaitableInt:
        """ambient() -> int: %

        環境光の強度を測定します。

        Returns:
            0%（暗い）から100%（明るい）の範囲の環境光強度。
        """

    def reflection(self) -> MaybeAwaitableInt:
        """reflection() -> int: %

        表面がセンサーの発する光をどれだけ反射するかを測定します。

        Returns:
            測定された反射率。0%（反射なし）から100%（高反射）の範囲。
        """

    @overload
    def detectable_colors(self, colors: Collection[Color]) -> None: ...

    @overload
    def detectable_colors(self) -> Collection[Color]: ...

    def detectable_colors(self, *args):
        """
        detectable_colors(colors)
        detectable_colors() -> Collection[Color]

        ``color()`` メソッドが検出する色を設定します。

        アプリケーションで検出したい色だけを指定してください。これにより、
        フルカラー測定値は最も近い指定色に丸められ、他の色は無視されます。
        これにより信頼性が向上します。

        引数を指定しない場合は、現在選択されている色が返されます。

        ブロックでコーディングする場合は、センサーセットアップブロックで
        設定します。

        Arguments:
            colors (list or tuple): 検出したい色である
                :class:`Color <.parameters.Color>` オブジェクトのリスト。
                ``Color.MAGENTA`` のような標準色を選ぶことも、
                ``Color(h=348, s=96, v=40)`` のような独自の色を指定して
                さらに良い結果を得ることもできます。独自の色は
                ``hsv()`` メソッドで測定します。
        """


class AmbientColorSensor(CommonColorSensor):
    """``CommonColorSensor`` に似ていますが、センサーライトを消した状態でも
    周囲の色を検出します。"""

    def color(self, surface: bool = True) -> MaybeAwaitableColor:
        """color(surface=True) -> Color

        表面または外部光源の色をスキャンします。

        検出する色は ``detectable_colors()`` メソッドで選択します。
        デフォルトでは ``Color.RED`` 、 ``Color.YELLOW`` 、
        ``Color.GREEN`` 、 ``Color.BLUE`` 、 ``Color.WHITE`` 、
        ``Color.NONE`` を検出します。

        Arguments:
            surface (bool): ``true`` を選択すると、物体や表面の色を
                スキャンします。``false`` を選択すると、画面やその他の
                外部光源の色をスキャンします。

        Returns:
            検出された色。
        """

    def hsv(self, surface: bool = True) -> MaybeAwaitableColor:
        """hsv(surface=True) -> Color

        表面または外部光源の色をスキャンします。

        このメソッドは ``color()`` に似ていますが、最も近い検出可能な色に
        丸めるのではなく、色相、彩度、輝度の全範囲の値を返します。

        Arguments:
            surface (bool): ``true`` を選択すると、物体や表面の色を
                スキャンします。``false`` を選択すると、画面やその他の
                外部光源の色をスキャンします。

        Returns:
            測定された色。色は色相（0--359）、彩度（0--100）、
            輝度（0--100）で表されます。
        """
