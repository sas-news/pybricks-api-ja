# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2020 The Pybricks Authors

"""Pybricks API の定数パラメータと引数。"""

from enum import Enum as _Enum


class _PybricksEnumMeta(type(_Enum)):
    def __dir__(cls):
        yield '__class__'
        yield '__name__'
        for member in cls:
            yield member.name


class _PybricksEnum(_Enum, metaclass=_PybricksEnumMeta):
    def __dir__(self):
        yield '__class__'
        for member in type(self):
            yield member.name

    def __str__(self):
        return '{}.{}'.format(type(self).__name__, self.name)

    def __repr__(self):
        return str(self)


class Color(_PybricksEnum):
    """ライトまたは物体表面の色。

    .. data:: BLACK
    .. data:: BLUE
    .. data:: GREEN
    .. data:: YELLOW
    .. data:: RED
    .. data:: WHITE
    .. data:: BROWN
    .. data:: ORANGE
    .. data:: PURPLE
    """

    BLACK = 1
    BLUE = 2
    GREEN = 3
    YELLOW = 4
    RED = 5
    WHITE = 6
    BROWN = 7
    ORANGE = 8
    PURPLE = 9


class Port(_PybricksEnum):
    """プログラマブルブロックまたはハブのポート。"""

    # Generic motor/sensor ports
    A = ord('A')
    B = ord('B')
    C = ord('C')
    D = ord('D')
    E = ord('E')
    F = ord('F')

    # NXT/EV3 sensor ports
    S1 = ord('1')
    S2 = ord('2')
    S3 = ord('3')
    S4 = ord('4')


class Stop(_PybricksEnum):
    """モーター停止後の動作: coast（惰行）、brake（ブレーキ）、hold（保持）。

    .. data:: COAST

        モーターを自由に回転できる状態にします。

    .. data:: BRAKE

        小さな外力に受動的に抵抗します。

    .. data:: HOLD

        モーターの制御を続け、指令された角度に保持します。
        これはエンコーダー付きモーターでのみ使用できます。
    """

    COAST = 0
    BRAKE = 1
    HOLD = 2


class Direction(_PybricksEnum):
    """正の速度または角度の値に対する回転方向。

    .. data:: CLOCKWISE

        正の速度値でモーターが時計回りに回転します。

    .. data:: COUNTERCLOCKWISE

        正の速度値でモーターが反時計回りに回転します。

    +--------------------------------+-------------------+-----------------+
    | ``positive_direction =``       | 正の速度:         | 負の速度:       |
    +================================+===================+=================+
    | ``Direction.CLOCKWISE``        | 時計回り          | 反時計回り      |
    +--------------------------------+-------------------+-----------------+
    | ``Direction.COUNTERCLOCKWISE`` | 反時計回り        | 時計回り        |
    +--------------------------------+-------------------+-----------------+
    """

    CLOCKWISE = 0
    COUNTERCLOCKWISE = 1


class Button(_PybricksEnum):
    """ブロックまたはリモコンのボタン:

    .. data:: LEFT_DOWN
    .. data:: DOWN
    .. data:: RIGHT_DOWN
    .. data:: LEFT
    .. data:: CENTER
    .. data:: RIGHT
    .. data:: LEFT_UP
    .. data:: UP
    .. data:: BEACON
    .. data:: RIGHT_UP

    +-----------+----------+-----------+
    |           |          |           |
    | LEFT_UP   |UP/BEACON | RIGHT_UP  |
    |           |          |           |
    +-----------+----------+-----------+
    |           |          |           |
    | LEFT      |  CENTER  | RIGHT     |
    |           |          |           |
    +-----------+----------+-----------+
    |           |          |           |
    | LEFT_DOWN |   DOWN   | RIGHT_DOWN|
    |           |          |           |
    +-----------+----------+-----------+
    """

    LEFT_DOWN = 1
    DOWN = 2
    RIGHT_DOWN = 3
    LEFT = 4
    CENTER = 5
    RIGHT = 6
    LEFT_UP = 7
    UP = 8
    BEACON = 8
    RIGHT_UP = 9
