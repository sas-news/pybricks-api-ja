# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2023 The Pybricks Authors

"""LEGO® Powered Up のモーター、センサー、ライト。"""

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _common
from .iodevices import LWP3Device
from .parameters import Button, Direction

if TYPE_CHECKING:
    from collections.abc import Collection

    from ._common import (
        MaybeAwaitable,
        MaybeAwaitableBool,
        MaybeAwaitableFloat,
        MaybeAwaitableInt,
        MaybeAwaitableTuple,
    )
    from .parameters import Color, Number, Port


class DCMotor(_common.DCMotor):
    """LEGO® Powered Up 回転センサーなしモーター。"""

    # HACK: jedi can't find inherited __init__ so we have to duplicate docs
    def __init__(self, port: Port, positive_direction: Direction = Direction.CLOCKWISE):
        """__init__(port, positive_direction=Direction.CLOCKWISE)

        Arguments:
            port (Port): モーターを接続するポート。
            positive_direction (Direction): 正のデューティサイクル値を
                与えたときにモーターが回転する方向。
        """


class Motor(_common.Motor):
    """LEGO® Powered Up 回転センサー付きモーター。"""

    # HACK: jedi can't find inherited __init__ so we have to duplicate docs
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
            port (Port): モーターを接続するポート。
            positive_direction (Direction): 正の速度値や角度を与えたときに
                モーターが回転する方向。
            gears (list):
                モーターに連結されたギアのリスト。モーターに接続された
                ギアが先頭で、出力側に接続されたギアが最後になります。

                たとえば ``[12, 36]`` は、モーターに12歯のギア、出力側に
                36歯のギアが接続されたギア列を表します。複数のギア列には
                ``[[12, 36], [20, 16, 40]]`` のようなリストのリストを
                使います。

                ギア列を指定すると、すべてのモーターコマンドと設定は
                ギア比を考慮して自動的に調整されます。これによって
                モーターの回転方向が変わることはありません。
            reset_angle (bool):
                ``True`` を選択すると、回転センサーの値を絶対マーカー角度
                (-180から179まで) にリセットします。
                ``False`` を選択すると現在の値を維持するため、前回
                プログラムが終了した位置から続けられます。
            profile (Number, deg): 精度プロファイル。アプリケーションで
                許容できる位置の誤差を度単位で表した概算値です。
                小さい値ほど正確ですが動きが不安定になり、大きい値ほど
                精度は下がりますが滑らかな動きになります。値を指定しない
                場合は、このモータータイプに適したプロファイルが自動的に
                選択されます (約11度) 。
        """

    def reset_angle(self, angle: Number | None = None) -> None:
        """reset_angle(angle=None)

        モーターの累積回転角度を任意の値に設定します。

        このモーターがドライブベースでも使われている場合は、ドライブベースの
        距離と角度の値にも影響します。代わりに
        :meth:`reset <pybricks.robotics.DriveBase.reset>`
        メソッドを使うとよいでしょう。

        Arguments:
            angle (Number, deg): 角度をリセットする値。
                                 ``None`` を選択すると、モーターの
                                 絶対値にリセットします。
        """


class Remote(LWP3Device):
    """LEGO® Powered Up Bluetoothリモートコントロール。"""

    light = _common.ExternalColorLight()
    buttons = _common.Keypad(
        (
            Button.LEFT_MINUS,
            Button.RIGHT_MINUS,
            Button.LEFT,
            Button.CENTER,
            Button.RIGHT,
            Button.LEFT_PLUS,
            Button.RIGHT_PLUS,
        )
    )
    address: str | None

    def __init__(
        self,
        name: str | None = None,
        timeout: int = 10000,
        connect: bool = True,
    ):
        """Remote(name=None, timeout=10000, connect=True)

        Arguments:
            name (str): リモコンのBluetooth名。名前を指定しない場合、
                ハブは最初に見つかったリモコンに接続します。
            timeout (Number, ms): リモコンを検索する時間。
                ``None`` を選択すると、無制限に待ち続けます。
            connect (bool): ``False`` を選択すると接続をスキップします。
                後で ``connect()`` を呼び出して接続できます。

        Raises:
            OSError: 接続に失敗したかタイムアウトした場合。
        """


class TechnicMoveHub(LWP3Device):
    """LEGO® Technic Move Hub (set 42176, 42214, 42239).

    この新しいハブは、最新のTechnic Control+セットに搭載されています。
    ファームウェアの更新には特別なパスワードが必要なため、このハブには
    Pybricksをインストールできません。ただし、Pybricksが動作する対応
    ハブをこのハブに接続すれば、そのモーターを制御できます。
    """

    def __init__(
        self,
        name: str | None = None,
        timeout: int = 10000,
        connect: bool = True,
    ):
        """TechnicMoveHub(name=None, timeout=10000, connect=True)

        Arguments:
            name (str): ハブのBluetooth名。名前を指定しない場合、
                最初に見つかったTechnic Move Hubに接続します。
            timeout (Number, ms): ハブを検索する時間。
                ``None`` を選択すると、無制限に待ち続けます。
            connect (bool): ``False`` を選択すると接続をスキップします。
                後で ``connect()`` を呼び出して接続できます。

        Raises:
            OSError: 接続に失敗したかタイムアウトした場合。
        """

    def drive(self, speed: int, steering: int) -> MaybeAwaitable:
        """drive(speed, steering)

        指定した速度とステアリングでハブのモーター出力を駆動します。

        Arguments:
            speed (int): 駆動速度。パーセント (-100から100) で指定します。
            steering (int): ステアリング。パーセント (-100から100) で
                指定します。正の値で右に曲がります。±97を超える値は、
                機構上の制約に押し付けないよう ±97 に丸められます。

        Raises:
            OSError: ハブが接続されていない場合。
        """


class MarioHub(LWP3Device):
    """LEGO® Super Mario hub (sets 71360, 71387, 71441 and similar).

    Pybricksが動作する対応ハブを、LEGOのマリオ、ルイージ、ピーチの
    フィギュアに接続し、そのカラーセンサーを読み取ります。
    """

    def __init__(
        self,
        name: str | None = None,
        timeout: int = 10000,
        connect: bool = True,
    ):
        """MarioHub(name=None, timeout=10000, connect=True)

        Arguments:
            name (str): ハブのBluetooth名。名前を指定しない場合、
                最初に見つかったマリオハブに接続します。
            timeout (Number, ms): ハブを検索する時間。
                ``None`` を選択すると、無制限に待ち続けます。
            connect (bool): ``False`` を選択すると接続をスキップします。
                後で ``connect()`` を呼び出して接続できます。

        Raises:
            OSError: 接続に失敗したかタイムアウトした場合。
        """

    def color(self) -> Color:
        """color() -> Color

        最新に受信した通知から、カラーセンサーが検出した色を読み取ります。

        Returns:
            検出された色。

        Raises:
            OSError: ハブが接続されていない場合。
        """

    def hsv(self) -> Color:
        """hsv() -> Color

        最新に受信した通知から、カラーセンサーが検出した色の色相、彩度、
        輝度を :class:`Color <.parameters.Color>` オブジェクトとして
        読み取ります。

        Returns:
            測定された色。

        Raises:
            OSError: ハブが接続されていない場合。
        """

    def detectable_colors(self, colors: Collection[Color] | None = None) -> None:
        """detectable_colors(colors)

        :meth:`color` が返しうる色のリストを設定します。

        このリストに含まれる色だけが返されます。特定の色のサブセットだけを
        扱いたい場合に、誤検出を減らすのに役立ちます。

        Arguments:
            colors (list): 検出する :class:`Color <.parameters.Color>`
                オブジェクトのリスト。``None`` を選択すると、デフォルトの
                リストに戻します。
        """


class DuploTrain(LWP3Device):
    """LEGO® Duplo Train hub (sets 10874, 10875, 10427, 10428 similar).

    Duploハブはファームウェアを更新できないため、このハブにPybricksを
    インストールすることはできません。ただし、Pybricksが動作する対応
    ハブをDuploハブに接続して、トレインを制御できます。

    モーター、サウンド、ヘッドライトを制御し、速度センサーとカラー
    センサーを読み取ることができます。
    """

    def __init__(
        self,
        name: str | None = None,
        timeout: int = 10000,
        connect: bool = True,
    ):
        """DuploTrain(name=None, timeout=10000, connect=True)

        Arguments:
            name (str): ハブのBluetooth名。名前を指定しない場合、
                最初に見つかったDuplo Trainハブに接続します。
            timeout (Number, ms): ハブを検索する時間。
                ``None`` を選択すると、無制限に待ち続けます。
            connect (bool): ``False`` を選択すると接続をスキップします。
                後で ``connect()`` を呼び出して接続できます。

        Raises:
            OSError: 接続に失敗したかタイムアウトした場合。
        """

    def drive(self, speed: int) -> MaybeAwaitable:
        """drive(speed)

        指定した速度でトレインのモーターを駆動します。

        Arguments:
            speed (int): 速度。パーセント (-100から100) で指定します。
                負の値で後進します。

        Raises:
            OSError: ハブが接続されていない場合。
        """

    def headlights(self, color: Color) -> MaybeAwaitable:
        """headlights(color)

        トレインのヘッドライトの色を設定します。すべての色に対応している
        わけではないため、ハブは生成できる最も近い色を選びます。

        Arguments:
            color (Color): ヘッドライトの色。

        Raises:
            OSError: ハブが接続されていない場合。
        """

    def sound(self, sound: str) -> MaybeAwaitable:
        """sound(sound)

        内蔵のトレインサウンドを1つ再生します。

        新しい (濃紺の) トレインでは、正しいサウンドコードがまだ解明
        されていません。やり方をご存じの方は、discussionやプルリクエストを
        開いていただけると幸いです。

        Arguments:
            sound (str): 再生するサウンド名。 ``"brake"`` 、 ``"depart"`` 、
                ``"water"`` 、 ``"horn"`` 、 ``"steam"`` から選択します。

        Raises:
            OSError: ハブが接続されていない場合。
        """

    def speed(self) -> int:
        """speed() -> int: %

        最新に受信した通知から、トレインの速度を読み取ります。

        Returns:
            パーセント (-100から100) で表した速度。

        Raises:
            OSError: ハブが接続されていない場合。
        """

    def color(self) -> Color:
        """color() -> Color

        最新に受信した通知から、カラーセンサーが検出した色を読み取ります。

        Returns:
            検出された色。

        Raises:
            OSError: ハブが接続されていない場合。
        """


class TiltSensor:
    """LEGO® Powered Up 傾きセンサー。"""

    def __init__(self, port: Port):
        """TiltSensor(port)

        Arguments:
            port (Port): センサーを接続するポート。
        """

    def tilt(self) -> MaybeAwaitableTuple[int, int]:
        """tilt() -> tuple[int, int]: deg

        水平面に対する傾きを測定します。

        Returns:
            ピッチ角とロール角のタプル。
        """


class ColorDistanceSensor(_common.CommonColorSensor):
    """LEGO® Powered Up カラー・距離センサー。"""

    light = _common.ExternalColorLight()

    # HACK: jedi can't find inherited __init__ so docs have to be duplicated
    def __init__(self, port: Port):
        """__init__(port)

        Arguments:
            port (Port): センサーを接続するポート。
        """

    def distance(self) -> MaybeAwaitableInt:
        """distance() -> int: %

        赤外線を使って、センサーと物体の間の相対的な距離を測定します。

        Returns:
            0% (最も近い) から 100% (最も遠い) までの距離。
        """


class PFMotor:
    """:class:`ColorDistanceSensor <pybricks.pupdevices.ColorDistanceSensor>` の
    赤外線機能を使ってPower Functionsモーターを制御します。"""

    def __init__(
        self,
        sensor: ColorDistanceSensor,
        channel: int,
        color: Color,
        positive_direction: Direction = Direction.CLOCKWISE,
    ):
        """PFMotor(sensor, channel, color, positive_direction=Direction.CLOCKWISE)

        Arguments:
            sensor (ColorDistanceSensor):
                センサーオブジェクト。
            channel (int):
                レシーバーのチャンネル番号: ``1``、``2``、``3``、``4`` のいずれか。
            color (Color):
                レシーバーの色マーカー:
                :class:`Color.BLUE <.parameters.Color>` または
                :class:`Color.RED <.parameters.Color>`
            positive_direction (Direction): 正のデューティサイクル値を
                与えたときにモーターが回転する方向。
        """

    def dc(self, duty: Number) -> MaybeAwaitable:
        """dc(duty)

        指定したデューティサイクル (「パワー」とも呼ばれます) でモーターを
        回転させます。

        Arguments:
            duty (Number, %): デューティサイクル (-100.0から100) 。
        """

    def stop(self) -> MaybeAwaitable:
        """stop()

        モーターを停止し、自由に回転できるようにします。

        モーターは摩擦により徐々に停止します。
        """

    def brake(self) -> MaybeAwaitable:
        """brake()

        モーターに受動的なブレーキをかけます。

        モーターは摩擦に加え、まだ動いている間に発生する電圧によって
        停止します。
        """


class ColorSensor(_common.AmbientColorSensor):
    """LEGO® SPIKE カラーセンサー。"""

    lights = _common.LightArray3()

    # HACK: jedi can't find inherited __init__ so docs have to be duplicated
    def __init__(self, port: Port):
        """__init__(port)

        Arguments:
            port (Port): センサーを接続するポート。
        """


class UltrasonicSensor:
    """LEGO® SPIKE 超音波センサー。"""

    lights = _common.LightArray4()

    def __init__(self, port: Port):
        """UltrasonicSensor(port)

        Arguments:
            port (Port): センサーを接続するポート。

        """

    def distance(self) -> MaybeAwaitableInt:
        """distance() -> int: mm

        超音波を使って、センサーと物体の間の距離を測定します。

        Returns:
            測定された距離。有効な距離が測定できなかった場合は
            2000 mm を返します。

        """

    def presence(self) -> MaybeAwaitableBool:
        """presence() -> bool

        超音波を検出することで、他の超音波センサーの存在を確認します。

        Returns:
            超音波が検出されれば ``True``、されなければ ``False``。
        """


class ForceSensor:
    """LEGO® SPIKE フォースセンサー。"""

    def __init__(self, port: Port):
        """ForceSensor(port)

        Arguments:
            port (Port): センサーを接続するポート。
        """

    def force(self) -> MaybeAwaitableFloat:
        """force() -> float: N

        センサーに加えられた力を測定します。

        Returns:
            測定された力 (最大約10.00 N) 。
        """

    def distance(self) -> MaybeAwaitableFloat:
        """distance() -> float: mm

        センサーボタンがどれだけ動いたかを測定します。

        Returns:
            最大約8.00 mmの動き。
        """

    def pressed(self, force: Number = 3) -> MaybeAwaitableBool:
        """pressed(force=3) -> bool

        センサーボタンが押されているかを確認します。

        Arguments:
            force (Number, N): 押されたとみなす最小の力。

        Returns:
            センサーが押されていれば ``True``、そうでなければ ``False``。
        """

    def touched(self) -> MaybeAwaitableBool:
        """touched() -> bool

        センサーが触れられているかを確認します。

        これは :meth:`pressed` に似ていますが、測定された力がまだゼロと
        みなされる場合でも、ボタンのわずかな動きを検出します。

        Returns:
            センサーが触れられているか押されていれば ``True``、
            そうでなければ ``False``。
        """


class ColorLightMatrix:
    """
    LEGO® SPIKE 3x3カラーライトマトリクス。
    """

    def __init__(self, port: Port):
        """ColorLightMatrix(port)

        Arguments:
            port (Port): デバイスを接続するポート。

        """

    def on(self, color: Color | Collection[Color]) -> MaybeAwaitable:
        """on(colors)

        ライトを点灯します。

        Arguments:
            colors (Color or list):
                単一の :class:`.Color` を指定すると、9個すべてのライトが
                その色に設定されます。色のリストを指定すると、それぞれの
                ライトに対応する色が設定されます。
        """

    def off(self) -> MaybeAwaitable:
        """off()

        すべてのライトを消灯します。
        """


class InfraredSensor:
    """LEGO® Powered Up 赤外線センサー。"""

    def __init__(self, port: Port):
        """InfraredSensor(port)

        Arguments:
            port (Port): センサーを接続するポート。
        """

    def reflection(self) -> MaybeAwaitableInt:
        """reflection() -> int: %

        赤外線を使って、表面の反射を測定します。

        Returns:
            測定された反射。0% (反射なし) から 100% (高い反射) まで。
        """

    def distance(self) -> MaybeAwaitableInt:
        """distance() -> int: %

        赤外線を使って、センサーと物体の間の相対的な距離を測定します。

        Returns:
            0% (最も近い) から 100% (最も遠い) までの距離。
        """

    def count(self) -> MaybeAwaitableInt:
        """count() -> int

        センサーの前を通過した物体の数をカウントします。

        Returns:
            カウントされた物体の数。
        """


class Light:
    """LEGO® Powered Up ライト。"""

    def __init__(self, port: Port):
        """Light(port)

        Arguments:
            port (Port): デバイスを接続するポート。
        """

    def on(self, brightness: Number = 100) -> None:
        """on(brightness=100)

        指定した輝度でライトを点灯します。

        Arguments:
            brightness (Number, %):
                ライトの輝度。
        """

    def off(self) -> None:
        """off()

        ライトを消灯します。"""


# Hide type-only names from jedi completions in the module namespace.
if TYPE_CHECKING:
    del Button
    del Collection
    del Color
    del Direction
    del LWP3Device
    del MaybeAwaitable
    del MaybeAwaitableBool
    del MaybeAwaitableFloat
    del MaybeAwaitableInt
    del MaybeAwaitableTuple
    del Number
    del Port
