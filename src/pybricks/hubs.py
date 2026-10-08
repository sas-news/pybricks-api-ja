# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2023 The Pybricks Authors

"""LEGO® プログラムハブ。"""

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _common
from .parameters import Axis
from .parameters import Button as _Button
from .parameters import Image as _Image


class EV3Brick:
    """LEGO® MINDSTORMS® EV3ブリック。"""

    # これらのクラス属性は、自動ドキュメント化のためにここにあります。
    # 実際には、__init__で作成されるインスタンス属性です。
    buttons = _common.Keypad(
        [
            _Button.LEFT,
            _Button.RIGHT,
            _Button.CENTER,
            _Button.UP,
            _Button.DOWN,
        ]
    )
    screen = _Image("_screen_")
    speaker = _common.Speaker()
    battery = _common.Battery()
    light = _common.ColorLight()
    system = _common.System()


class NXTBrick:
    """LEGO® MINDSTORMS® NXTブリック。"""

    # これらのクラス属性は、自動ドキュメント化のためにここにあります。
    # 実際には、__init__で作成されるインスタンス属性です。
    buttons = _common.Keypad(
        [
            _Button.LEFT,
            _Button.RIGHT,
            _Button.CENTER,
            _Button.DOWN,
        ]
    )
    screen = _Image("_screen_")
    speaker = _common.Speaker()
    battery = _common.Battery()
    system = _common.System()


class MoveHub:
    """LEGO® BOOST Moveハブ。"""

    # これらのクラス属性は、自動ドキュメント化のためにここにあります。
    # 実際には、__init__で作成されるインスタンス属性です。
    battery = _common.Battery()
    light = _common.ColorLight()
    imu = _common.SimpleAccelerometer()
    system = _common.System()
    buttons = _common.Keypad([_Button.CENTER])

    def __init__(
        self,
        top_side: Axis = Axis.Z,
        front_side: Axis = Axis.X,
    ):
        """MoveHub(top_side=Axis.Z, front_side=Axis.X)

        Arguments:
            top_side (Axis): ハブの *上面* を通る軸。
            front_side (Axis): ハブの *前面* を通る軸。
        """


class CityHub:
    """LEGO® Cityハブ。"""

    # これらのクラス属性は、自動ドキュメント化のためにここにあります。
    # 実際には、__init__で作成されるインスタンス属性です。
    battery = _common.Battery()
    light = _common.ColorLight()
    system = _common.System()
    buttons = _common.Keypad([_Button.CENTER])

    def __init__(self):
        """CityHub()"""


class TechnicHub:
    """LEGO® Technicハブ。"""

    # これらのクラス属性は、自動ドキュメント化のためにここにあります。
    # 実際には、__init__で作成されるインスタンス属性です。
    battery = _common.Battery()
    light = _common.ColorLight()
    imu = _common.IMU()
    system = _common.System()
    buttons = _common.Keypad([_Button.CENTER])

    def __init__(
        self,
        top_side: Axis = Axis.Z,
        front_side: Axis = Axis.X,
    ):
        """TechnicHub(top_side=Axis.Z, front_side=Axis.X)

        ハブの初期化を行います。
        任意でハブの上面（ボタンがある方）と前面（ライトがある方）の向きを指定し、
        :ref:`ハブをデザインにどのように配置するか <robotframe>` を指定することができます。

        Arguments:
            top_side (Axis): ハブの *上面* を通る軸。
            front_side (Axis): ハブの *前面* を通る軸。
        """


class EssentialHub:
    """LEGO® SPIKE Essentialハブ。"""

    # これらのクラス属性は、自動ドキュメント化のためにここにあります。
    # 実際には、__init__で作成されるインスタンス属性です。
    battery = _common.Battery()
    buttons = _common.Keypad([_Button.CENTER])
    charger = _common.Charger()
    light = _common.ColorLight()
    imu = _common.IMU()
    system = _common.System()

    def __init__(
        self,
        top_side: Axis = Axis.Z,
        front_side: Axis = Axis.X,
    ):
        """EssentialHub(top_side=Axis.Z, front_side=Axis.X)

        ハブの初期化を行います。
        任意でハブの上面（ボタンがある方）と前面（USBポートとI/OポートA・Bがある方）の向きを指定し、
        :ref:`ハブをデザインにどのように配置するか <robotframe>` を指定することができます。

        Arguments:
            top_side (Axis): ハブの *上面* を通る軸。
            front_side (Axis): ハブの *前面* を通る軸。
        """


class PrimeHub:
    """LEGO® SPIKE Primeハブ。"""

    # これらのクラス属性は、自動ドキュメント化のためにここにあります。
    # 実際には、__init__で作成されるインスタンス属性です。
    battery = _common.Battery()
    buttons = _common.Keypad(
        [
            _Button.LEFT,
            _Button.RIGHT,
            _Button.CENTER,
            _Button.BLUETOOTH,
        ]
    )
    charger = _common.Charger()
    light = _common.ColorLight()
    display = _common.LightMatrix(5, 5)
    speaker = _common.Speaker()
    imu = _common.IMU()
    system = _common.System()

    def __init__(
        self,
        top_side: Axis = Axis.Z,
        front_side: Axis = Axis.X,
    ):
        """PrimeHub(top_side=Axis.Z, front_side=Axis.X)

        Hubの初期化を行います。
        任意でハブの上面（ボタンがある方）と前面（USBポートがある方）の向きを指定し、
        :ref:`ハブをデザインにどのように配置するか <robotframe>` を指定することができます。

        Arguments:
            top_side (Axis): Hubの上面を通る軸。
            front_side (Axis): Hubの前面を通る軸。
        """


class InventorHub(PrimeHub):
    """LEGO® MINDSTORMS Inventorハブ。"""


# 型専用の名前をモジュール名前空間のjedi補完から隠します。
if TYPE_CHECKING:
    del Axis
