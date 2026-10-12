# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2022 The Pybricks Authors

"""LEGO® MINDSTORMS® NXT のモーターとセンサーを EV3 ブリックで使用します。"""

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _common
from ._common import ColorLight, CommonColorSensor
from .iodevices import AnalogSensor

if TYPE_CHECKING:
    from collections.abc import Callable

    from ._common import (
        MaybeAwaitableFloat,
        MaybeAwaitableInt,
        MaybeAwaitableTuple,
    )
    from .parameters import Color, Port


class Motor(_common.Motor):
    """LEGO® MINDSTORMS® EV3 Motor."""


class TouchSensor:
    """LEGO® MINDSTORMS® NXT Touch Sensor."""

    def __init__(self, port: Port):
        """TouchSensor(port)

        Arguments:
            port (Port): センサーを接続するポート。
        """

    def pressed(self) -> bool:
        """pressed() -> bool

        センサーが押されているかを確認します。

        Returns:
            センサーが押されていれば ``True`` 、押されていなければ
            ``False`` 。
        """


class LightSensor:
    """LEGO® MINDSTORMS® NXT Color Sensor."""

    def __init__(self, port: Port):
        """LightSensor(port)

        Arguments:
            port (Port): センサーを接続するポート。
        """

    def ambient(self) -> int:
        """ambient() -> int: %

        周囲の光の強さを測定します。

        Returns:
            0% (暗い) から 100% (明るい) までの周囲の光の強さ。
        """

    def reflection(self) -> int:
        """reflection() -> int: %

        赤い光を使って、表面の反射率を測定します。

        Returns:
            0% (反射なし) から 100% (高い反射) までの反射率。
        """


class ColorSensor(CommonColorSensor):
    """LEGO® MINDSTORMS® NXT Color Sensor."""

    light = ColorLight()

    def rgb(self) -> tuple[int, int, int]:
        """赤、緑、青の順に光を当てて、表面の反射率を測定します。

        Returns:
            赤、緑、青それぞれの光に対する反射率のタプル。各値は
            0.0% (反射なし) から 100.0% (高い反射) まで。
        """

    def color(self) -> Color:
        """color() -> Color

        表面の色をスキャンします。

        検出する色は ``detectable_colors()`` メソッドで選択します。
        デフォルトでは ``Color.RED`` 、 ``Color.YELLOW`` 、
        ``Color.GREEN`` 、 ``Color.BLUE`` 、 ``Color.WHITE`` 、
        ``Color.NONE`` を検出します。

        Returns:
            検出された色。
        """

    def hsv(self) -> Color:
        """hsv() -> Color

        表面の色をスキャンします。

        このメソッドは ``color()`` に似ていますが、最も近い検出可能な色に
        丸めるのではなく、色相、彩度、輝度の全範囲の値を返します。

        Returns:
            測定された色。色は色相 (0--359) 、彩度 (0--100) 、
            輝度 (0--100) で表されます。
        """

    def ambient(self) -> int:
        """ambient() -> int: %

        周囲の光の強さを測定します。

        Returns:
            0% (暗い) から 100% (明るい) までの周囲の光の強さ。
        """

    def reflection(self) -> int:
        """reflection() -> int: %

        表面がセンサーの発する光をどれだけ反射するかを測定します。

        Returns:
            0% (反射なし) から 100% (高い反射) までの反射率。
        """


class UltrasonicSensor:
    """LEGO® MINDSTORMS® NXT Ultrasonic Sensor."""

    def __init__(self, port: Port):
        """UltrasonicSensor(port)

        Arguments:
            port (Port): センサーを接続するポート。
        """

    def distance(self) -> MaybeAwaitableInt:
        """distance() -> int: mm

        超音波を使って、センサーと物体の間の距離を測定します。

        Returns:
            測定された距離。
        """


class SoundSensor:
    """LEGO® MINDSTORMS® NXT Sound Sensor."""

    def __init__(self, port: Port):
        """SoundSensor(port)

        Arguments:
            port (Port): センサーを接続するポート。
        """

    def intensity(self, audible_only: bool = True) -> int:
        """intensity(audible_only=True) -> int: %

        周囲の音の強さ (音量) を測定します。

        Arguments:
            audible_only (bool): 可聴音のみを検出します。人間の耳に
                聞こえない周波数を除去しようとします。

        Returns:
            音の強さ。
        """


class TemperatureSensor:
    """LEGO® MINDSTORMS® NXT Temperature Sensor."""

    def __init__(self, port: Port):
        """TemperatureSensor(port)

        Arguments:
            port (Port): センサーを接続するポート。
        """

    def temperature(self) -> MaybeAwaitableFloat:
        """temperature() -> float: °C

        温度を測定します。

        Returns:
            測定された温度。
        """


class EnergyMeter:
    """LEGO® MINDSTORMS® Education NXT エネルギーメーター。"""

    def __init__(self, port: Port):
        """EnergyMeter(port)

        Arguments:
            port (Port): センサーを接続するポート。
        """

    def storage(self) -> MaybeAwaitableInt:
        """storage() -> int: J

        バッテリーに蓄えられている利用可能な総エネルギーを取得します。

        Returns:
            残りの蓄積エネルギー。
        """

    def input(self) -> MaybeAwaitableTuple[int, int, int]:
        """input() -> tuple[int, int, int]

        エネルギーメーターの入力側 (底面) の電気信号を測定します。
        印加される電圧と流れる電流を測定し、この2つの値の積が電力に
        なります。この電力値は蓄積エネルギーが増加する速さです。
        この電力は、付属のソーラーパネルや外部から駆動されるモーター
        などのエネルギー源から供給されます。

        Returns:
            入力ポートで測定された電圧 (mV) 、電流 (mA) 、電力 (mW) 。
        """

    def output(self) -> MaybeAwaitableTuple[int, int, int]:
        """output() -> tuple[int, int, int]

        エネルギーメーターの出力側 (上面) の電気信号を測定します。
        外部負荷に印加される電圧と流れる電流を測定し、この2つの値の積が
        電力になります。この電力値は蓄積エネルギーが減少する速さです。
        この電力はライトやモーターなどの負荷によって消費されます。

        Returns:
            出力ポートで測定された電圧 (mV) 、電流 (mA) 、電力 (mW) 。
        """


class VernierAdapter(AnalogSensor):
    """LEGO® MINDSTORMS® Education NXT/EV3 Vernierセンサー用アダプター。"""

    def __init__(self, port: Port, conversion: Callable[[int], float] | None = None):
        """VernierAdapter(port, conversion=None)

        Arguments:
            port (Port): センサーを接続するポート。
            conversion (callable): :meth:`.conversion` 形式の関数。
                この関数は生のアナログ電圧をセンサー固有の出力値に
                変換するために使われます。各 Vernier センサーには独自の
                変換関数があります。下記の例は Surface Temperature
                Sensor の変換を示しています。
        """

    def voltage(self) -> int:
        """voltage() -> int: mV

        センサーの生のアナログ電圧を測定します。

        Returns:
            アナログ電圧。
        """

    def conversion(self, voltage: int) -> float:
        """conversion(voltage) -> float

        生の電圧 (mV) をセンサー値に変換します。

        前もって :meth:`.conversion` 関数を指定していない場合、変換は
        適用されません。

        Arguments:
            voltage (Number, mV): アナログセンサーの電圧。

        Returns:
            変換されたセンサー値。
        """

    def value(self) -> float:
        """value() -> float

        センサーの :meth:`.voltage` を測定し、指定した
        :meth:`.conversion` を適用してセンサー値を返します。

        Returns:
            変換されたセンサー値。
        """


# Hide type-only names from jedi completions in the module namespace.
if TYPE_CHECKING:
    del AnalogSensor
    del Callable
    del Color
    del ColorLight
    del CommonColorSensor
    del MaybeAwaitableFloat
    del MaybeAwaitableInt
    del MaybeAwaitableTuple
    del Port
