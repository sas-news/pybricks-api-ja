# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2022 The Pybricks Authors

"""LEGO® MINDSTORMS® EV3 のモーターとセンサー。"""

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _common
from .parameters import Direction

if TYPE_CHECKING:
    from ._common import (
        MaybeAwaitableBool,
        MaybeAwaitableInt,
        MaybeAwaitableSet,
        MaybeAwaitableTuple,
    )
    from .parameters import Button, Port


class Motor(_common.Motor):
    """LEGO® MINDSTORMS® EV3 Motor."""


class TouchSensor:
    """LEGO® MINDSTORMS® EV3 Touch Sensor."""

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


class ColorSensor(_common.CommonColorSensor):
    """LEGO® MINDSTORMS® EV3 Color Sensor."""

    def __init__(self, port: Port):
        """ColorSensor(port)

        Arguments:
            port (Port): センサーを接続するポート。
        """

    def rgb(self) -> MaybeAwaitableTuple[int, int, int]:
        """rgb() -> tuple[int, int, int]

        赤、緑、青の順に光を当てて、表面の反射率を測定します。

        Returns:
            赤、緑、青それぞれの光に対する反射率のタプル。各値は
            0.0% (反射なし) から 100.0% (高い反射) まで。
        """


class InfraredSensor:
    """LEGO® MINDSTORMS® EV3 赤外線センサーとビーコン。"""

    def __init__(self, port: Port):
        """InfraredSensor(port)

        Arguments:
            port (Port): センサーを接続するポート。

        """

    def distance(self) -> MaybeAwaitableInt:
        """distance() -> int: %

        赤外線を使って、センサーと物体の間の相対的な距離を測定します。

        Returns:
            0% (最も近い) から 100% (最も遠い) までの相対距離。

        """

    def beacon(self, channel: int) -> MaybeAwaitableTuple[int | None, int | None]:
        """
        beacon(channel) -> tuple[int, int]
        beacon(channel) -> tuple[None, None]

        リモコンと赤外線センサーの間の相対的な距離と角度を測定します。

        Arguments:
            channel (int): リモコンのチャンネル番号。

        Returns:
            リモコンと赤外線センサーの間の相対距離 (0% から 100%) と
            おおよその角度 (-75 から 75 度) のタプル。リモコンが
            検出されない場合は (``None``, ``None``) 。
        """

    def buttons(self, channel: int) -> MaybeAwaitableSet[Button]:
        """buttons(channel) -> set[Button]

        赤外線リモコンのどのボタンが押されているかを確認します。

        このメソッドは一度に最大2つのボタンを検出できます。それ以上の
        ボタンを押しても、検出されるのは2つだけです。

        Arguments:
            channel (int): リモコンのチャンネル番号。

        Returns:
            選択したチャンネルのリモコンで押されているボタンのセット。

        """

    def keypad(self) -> MaybeAwaitableSet[Button]:
        """keypad() -> set[Button]

        赤外線リモコンのどのボタンが押されているかを確認します。

        このメソッドは4つの上下ボタンをすべて個別に検出できますが、
        ビーコンボタンは検出できません。

        このメソッドはチャンネル1のリモコンでのみ動作します。

        Returns:
            押されているボタンのセット。
        """


class GyroSensor:
    """LEGO® MINDSTORMS® EV3 Gyro Sensor."""

    def __init__(self, port: Port, direction: Direction = Direction.CLOCKWISE):
        """GyroSensor(port)

        Arguments:
            port (Port): センサーを接続するポート。
            direction (Direction):
                センサー上部の赤い点を見たときの正の回転方向。

        """

    def speed(self) -> int:
        """speed() -> int: deg/s

        センサーの速度 (角速度) を取得します。

        Returns:
            角速度。

        """

    def angle(self) -> int:
        """angle() -> int: deg

        センサーの累積角度を取得します。

        Returns:
            回転角度。

        """

    def reset_angle(self, angle: int) -> None:
        """reset_angle(angle)

        センサーの回転角度を任意の値に設定します。

        Arguments:
            angle (Number, deg): 角度をリセットする値。
        """


class UltrasonicSensor:
    """LEGO® MINDSTORMS® EV3 Ultrasonic Sensor."""

    def __init__(self, port: Port):
        """UltrasonicSensor(port)

        Arguments:
            port (Port): センサーを接続するポート。

        """

    def distance(self, silent: bool = False) -> MaybeAwaitableInt:
        """distance(silent=False) -> int: mm

        超音波を使って、センサーと物体の間の距離を測定します。

        Arguments:
            silent (bool): ``True`` を選択すると、距離の測定後に
                           センサーをオフにします。他の超音波センサーとの
                           干渉を減らせます。ただし頻繁に行いすぎると
                           センサーがフリーズすることがあります。
                           その場合は一度抜いて差し直してください。

        Returns:
            測定された距離。

        """

    def presence(self) -> MaybeAwaitableBool:
        """presence() -> bool

        超音波を検出することで、他の超音波センサーの存在を確認します。

        他の超音波センサーがサイレントモードで動作している場合、その
        センサーが測定を行っている間だけ存在を検出できます。

        Returns:
            超音波が検出されれば ``True`` 、されなければ ``False`` 。
        """


# Hide type-only names from jedi completions in the module namespace.
if TYPE_CHECKING:
    del Button
    del Direction
    del MaybeAwaitableBool
    del MaybeAwaitableInt
    del MaybeAwaitableSet
    del MaybeAwaitableTuple
    del Port
