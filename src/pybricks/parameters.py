# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2022 The Pybricks Authors

"""Pybricks API の定数パラメータと引数。"""

from __future__ import annotations

import os
from enum import Enum
from typing import TYPE_CHECKING, overload

from .tools import Matrix as _Matrix
from .tools import vector as _vector

if TYPE_CHECKING:
    from typing import Any, Literal

if TYPE_CHECKING or os.environ.get("SPHINX_BUILD") == "True":
    Number = int | float
    """
    数値は整数または浮動小数点値で表されます:

        * 整数 (:class:`int <ubuiltins.int>`) は ``15`` や ``-123`` のような
          小数点以下を持たない数値です。
        * 浮動小数点値 (:class:`float <ubuiltins.float>`) は ``3.14`` や
          ``-123.45`` のような小数を含む数値です。

    引数の型として :class:`Number` と書かれている場合は、
    :class:`int <ubuiltins.int>` と :class:`float <ubuiltins.float>`
    のどちらも使用できます。

    たとえば、:func:`wait(15) <pybricks.tools.wait>` と
    :func:`wait(15.75) <pybricks.tools.wait>` はどちらも有効です。
    ただし、ほとんどの関数では入力した値は整数に切り捨てられます。
    この例では、どちらのコマンドでもプログラムは15ミリ秒だけ
    一時停止します。

    .. note::
        BOOST Move ハブはシステムリソースの制約により浮動小数点数を
        サポートしていません。そのハブでは整数のみ使用できます。
    """


class _PybricksEnumMeta(type(Enum)):
    @classmethod
    def __dir__(cls):
        yield "__class__"
        yield "__name__"
        for member in cls:
            yield member.name


class _PybricksEnum(Enum, metaclass=_PybricksEnumMeta):
    def __dir__(self):
        yield "__class__"
        for member in type(self):
            yield member.name

    def __str__(self):
        return f"{type(self).__name__}.{self.name}"

    def __repr__(self):
        return str(self)


class Axis:
    """座標系の単位軸。"""

    X: _Matrix = _vector(1, 0, 0)

    Y: _Matrix = _vector(0, 1, 0)

    Z: _Matrix = _vector(0, 0, 1)


class Color:
    """ライトまたは物体表面の色。"""

    NONE: Color = ...
    BLACK: Color = ...
    GRAY: Color = ...
    WHITE: Color = ...
    RED: Color = ...
    ORANGE: Color = ...
    BROWN: Color = ...
    YELLOW: Color = ...
    GREEN: Color = ...
    CYAN: Color = ...
    BLUE: Color = ...
    VIOLET: Color = ...
    MAGENTA: Color = ...

    def __init__(self, h: Number, s: Number = 100, v: Number = 100):
        """Color(h, s=100, v=100)

        Arguments:
            h (Number, deg): 色相。
            s (Number, %): 彩度。
            v (Number, %): 輝度。
        """

        self.h = int(h) % 360
        """
        色相。
        """

        self.s = max(0, min(int(s), 100))
        """
        彩度。
        """

        self.v = max(0, min(int(v), 100))
        """
        輝度。
        """

    def __setattr__(self, key, value):
        if key not in ("h", "s", "v"):
            raise AttributeError("Can't modify unknown attribute: " + key)
        if hasattr(self, key):  # immutable after __init__
            raise AttributeError("Can't modify immutable attribute: " + key)
        super().__setattr__(key, value)

    def __iter__(self):
        """``Color`` インスタンスを ``h`` 、 ``s`` 、 ``v`` にアンパックできるようにします。"""
        return iter((self.h, self.s, self.v))

    def __repr__(self):
        return f"Color(h={self.h}, s={self.s}, v={self.v})"

    def __eq__(self, other: Color) -> bool:
        return self.h == other.h and self.s == other.s and self.v == other.v

    def __hash__(self) -> int:
        return hash((self.h, self.s, self.v))

    def __mul__(self, scale: float) -> Color:
        v = max(0, min(self.v * scale, 100))
        return Color(self.h, self.s, int(v))

    def __rmul__(self, scale: float) -> Color:
        return self.__mul__(scale)

    def __truediv__(self, scale: float) -> Color:
        return self.__mul__(1 / scale)

    def __floordiv__(self, scale: int) -> Color:
        return self.__mul__(1 / scale)

    def __lshift__(self, shift: int) -> Color:
        return self.__rshift__(-shift)

    def __rshift__(self, shift: int) -> Color:
        return Color((self.h + shift) % 360, self.s, self.v)


Color.NONE = Color(0, 0, 0)
Color.BLACK = Color(0, 0, 10)
Color.GRAY = Color(0, 0, 50)
Color.WHITE = Color(0, 0, 100)
Color.RED = Color(0, 100, 100)
Color.ORANGE = Color(30, 100, 100)
Color.BROWN = Color(30, 100, 50)
Color.YELLOW = Color(60, 100, 100)
Color.GREEN = Color(120, 100, 100)
Color.CYAN = Color(180, 100, 100)
Color.BLUE = Color(240, 100, 100)
Color.VIOLET = Color(270, 100, 100)
Color.MAGENTA = Color(300, 100, 100)


class Port(_PybricksEnum):
    """プログラマブルブロックまたはハブのポート。"""

    # Generic motor/sensor ports
    A: Port = ord("A")
    B: Port = ord("B")
    C: Port = ord("C")
    D: Port = ord("D")
    E: Port = ord("E")
    F: Port = ord("F")

    # NXT/EV3 sensor ports
    S1: Port = ord("1")
    S2: Port = ord("2")
    S3: Port = ord("3")
    S4: Port = ord("4")


class Stop(_PybricksEnum):
    """モーターが停止したとき、または目標に到達したときの動作。"""

    COAST: Stop = 0
    """モーターを自由に回転できる状態にします。"""

    COAST_SMART: Stop = 4
    """
    モーターを自由に回転できる状態にします。次の相対角度操作では、
    （現在の角度ではなく）最後の目標角度を新しい開始点として使用します。
    これにより累積誤差が減少します。現在の角度が設定された位置許容誤差の
    2倍未満の場合にのみ適用されます。
    """

    BRAKE: Stop = 1
    """小さな外力に受動的に抵抗します。"""

    HOLD: Stop = 2
    """モーターの制御を続け、指令された角度に保持します。"""

    NONE: Stop = 3
    """
    目標位置に近づいても減速しません。複数のモーターやドライブベースの
    操作を停止せずに連結するために使用できます。これ以上コマンドが
    与えられない場合、モーターは指定された速度で無限に回転し続けます。
    """


class Direction(_PybricksEnum):
    """正の速度または角度の値に対する回転方向。"""

    CLOCKWISE: Direction = 0
    """正の速度値でモーターが時計回りに回転します。"""

    COUNTERCLOCKWISE: Direction = 1
    """正の速度値でモーターが反時計回りに回転します。"""


class Button(_PybricksEnum):
    """ハブまたはリモコンのボタン。"""

    LEFT_DOWN: Button = 1
    LEFT_MINUS: Button = 1
    DOWN: Button = 2
    RIGHT_DOWN: Button = 3
    RIGHT_MINUS: Button = 3
    LEFT: Button = 4
    CENTER: Button = 5
    RIGHT: Button = 6
    LEFT_UP: Button = 7
    LEFT_PLUS: Button = 7
    UP: Button = 8
    BEACON: Button = 8
    RIGHT_UP: Button = 9
    RIGHT_PLUS: Button = 9
    BLUETOOTH: Button = 9
    A: Button = 0
    B: Button = 0
    X: Button = 0
    Y: Button = 0
    LB: Button = 0
    RB: Button = 0
    LJ: Button = 0
    RJ: Button = 0
    P1: Button = 0
    P2: Button = 0
    P3: Button = 0
    P4: Button = 0
    GUIDE: Button = 0
    MENU: Button = 0
    UPLOAD: Button = 0
    VIEW: Button = 0


class Side(_PybricksEnum):
    """ハブまたはセンサーの面。"""

    RIGHT: Side = 6
    FRONT: Side = 0
    TOP: Side = 8
    LEFT: Side = 4
    BACK: Side = 5
    BOTTOM: Side = 2


class Icon:
    """ライトマトリクスに表示するアイコン。

    以下の各属性はマトリクスです。つまり、アイコンをスケーリングして
    輝度を調整したり、アイコンを加算して合成したりできます。
    """

    UP: _Matrix = ...
    """
    | ⬜⬜🟨⬜⬜
    | ⬜🟨🟨🟨⬜
    | 🟨🟨🟨🟨🟨
    | ⬜🟨🟨🟨⬜
    | ⬜🟨🟨🟨⬜
    """
    DOWN: _Matrix = ...
    """
    | ⬜🟨🟨🟨⬜
    | ⬜🟨🟨🟨⬜
    | 🟨🟨🟨🟨🟨
    | ⬜🟨🟨🟨⬜
    | ⬜⬜🟨⬜⬜
    """
    LEFT: _Matrix = ...
    """
    | ⬜⬜🟨⬜⬜
    | ⬜🟨🟨🟨🟨
    | 🟨🟨🟨🟨🟨
    | ⬜🟨🟨🟨🟨
    | ⬜⬜🟨⬜⬜
    """
    RIGHT: _Matrix = ...
    """
    | ⬜⬜🟨⬜⬜
    | 🟨🟨🟨🟨⬜
    | 🟨🟨🟨🟨🟨
    | 🟨🟨🟨🟨⬜
    | ⬜⬜🟨⬜⬜
    """
    ARROW_RIGHT_UP: _Matrix = ...
    """
    | ⬜⬜🟨🟨🟨
    | ⬜⬜⬜🟨🟨
    | ⬜⬜🟨⬜🟨
    | ⬜🟨⬜⬜⬜
    | 🟨⬜⬜⬜⬜
    """
    ARROW_RIGHT_DOWN: _Matrix = ...
    """
    | 🟨⬜⬜⬜⬜
    | ⬜🟨⬜⬜⬜
    | ⬜⬜🟨⬜🟨
    | ⬜⬜⬜🟨🟨
    | ⬜⬜🟨🟨🟨
    """
    ARROW_LEFT_UP: _Matrix = ...
    """
    | 🟨🟨🟨⬜⬜
    | 🟨🟨⬜⬜⬜
    | 🟨⬜🟨⬜⬜
    | ⬜⬜⬜🟨⬜
    | ⬜⬜⬜⬜🟨
    """
    ARROW_LEFT_DOWN: _Matrix = ...
    """
    | ⬜⬜⬜⬜🟨
    | ⬜⬜⬜🟨⬜
    | 🟨⬜🟨⬜⬜
    | 🟨🟨⬜⬜⬜
    | 🟨🟨🟨⬜⬜
    """
    ARROW_UP: _Matrix = ...
    """
    | ⬜⬜🟨⬜⬜
    | ⬜🟨🟨🟨⬜
    | 🟨⬜🟨⬜🟨
    | ⬜⬜🟨⬜⬜
    | ⬜⬜🟨⬜⬜
    """
    ARROW_DOWN: _Matrix = ...
    """
    | ⬜⬜🟨⬜⬜
    | ⬜⬜🟨⬜⬜
    | 🟨⬜🟨⬜🟨
    | ⬜🟨🟨🟨⬜
    | ⬜⬜🟨⬜⬜
    """
    ARROW_LEFT: _Matrix = ...
    """
    | ⬜⬜🟨⬜⬜
    | ⬜🟨⬜⬜⬜
    | 🟨🟨🟨🟨🟨
    | ⬜🟨⬜⬜⬜
    | ⬜⬜🟨⬜⬜
    """
    ARROW_RIGHT: _Matrix = ...
    """
    | ⬜⬜🟨⬜⬜
    | ⬜⬜⬜🟨⬜
    | 🟨🟨🟨🟨🟨
    | ⬜⬜⬜🟨⬜
    | ⬜⬜🟨⬜⬜
    """
    HAPPY: _Matrix = ...
    """
    | 🟨🟨⬜🟨🟨
    | 🟨🟨⬜🟨🟨
    | ⬜⬜⬜⬜⬜
    | 🟨⬜⬜⬜🟨
    | ⬜🟨🟨🟨⬜
    """
    SAD: _Matrix = ...
    """
    | 🟨🟨⬜🟨🟨
    | 🟨🟨⬜🟨🟨
    | ⬜⬜⬜⬜⬜
    | ⬜🟨🟨🟨⬜
    | 🟨⬜⬜⬜🟨
    """
    EYE_LEFT: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | 🟨🟨⬜⬜⬜
    | 🟨🟨⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    EYE_RIGHT: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜🟨🟨
    | ⬜⬜⬜🟨🟨
    | ⬜⬜⬜⬜⬜
    """
    EYE_LEFT_BLINK: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | 🟨🟨⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    EYE_RIGHT_BLINK: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜🟨🟨
    | ⬜⬜⬜⬜⬜
    """
    EYE_RIGHT_BROW: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜🟨🟨
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    EYE_LEFT_BROW: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | 🟨🟨⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    EYE_LEFT_BROW_UP: _Matrix = ...
    """
    | 🟨🟨⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    EYE_RIGHT_BROW_UP: _Matrix = ...
    """
    | ⬜⬜⬜🟨🟨
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    HEART: _Matrix = ...
    """
    | ⬜🟨⬜🟨⬜
    | 🟨🟨🟨🟨🟨
    | 🟨🟨🟨🟨🟨
    | ⬜🟨🟨🟨⬜
    | ⬜⬜🟨⬜⬜
    """
    PAUSE: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜🟨⬜🟨⬜
    | ⬜🟨⬜🟨⬜
    | ⬜🟨⬜🟨⬜
    | ⬜⬜⬜⬜⬜
    """
    EMPTY: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    FULL: _Matrix = ...
    """
    | 🟨🟨🟨🟨🟨
    | 🟨🟨🟨🟨🟨
    | 🟨🟨🟨🟨🟨
    | 🟨🟨🟨🟨🟨
    | 🟨🟨🟨🟨🟨
    """
    SQUARE: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜🟨🟨🟨⬜
    | ⬜🟨🟨🟨⬜
    | ⬜🟨🟨🟨⬜
    | ⬜⬜⬜⬜⬜
    """
    TRIANGLE_RIGHT: _Matrix = ...
    """
    | ⬜🟨⬜⬜⬜
    | ⬜🟨🟨⬜⬜
    | ⬜🟨🟨🟨⬜
    | ⬜🟨🟨⬜⬜
    | ⬜🟨⬜⬜⬜
    """
    TRIANGLE_LEFT: _Matrix = ...
    """
    | ⬜⬜⬜🟨⬜
    | ⬜⬜🟨🟨⬜
    | ⬜🟨🟨🟨⬜
    | ⬜⬜🟨🟨⬜
    | ⬜⬜⬜🟨⬜
    """
    TRIANGLE_UP: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜⬜🟨⬜⬜
    | ⬜🟨🟨🟨⬜
    | 🟨🟨🟨🟨🟨
    | ⬜⬜⬜⬜⬜
    """
    TRIANGLE_DOWN: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | 🟨🟨🟨🟨🟨
    | ⬜🟨🟨🟨⬜
    | ⬜⬜🟨⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    CIRCLE: _Matrix = ...
    """
    | ⬜🟨🟨🟨⬜
    | 🟨🟨🟨🟨🟨
    | 🟨🟨🟨🟨🟨
    | 🟨🟨🟨🟨🟨
    | ⬜🟨🟨🟨⬜
    """
    CLOCKWISE: _Matrix = ...
    """
    | 🟨🟨🟨🟨⬜
    | 🟨⬜⬜🟨⬜
    | 🟨⬜⬜🟨⬜
    | 🟨⬜🟨🟨🟨
    | ⬜⬜⬜🟨⬜
    """
    COUNTERCLOCKWISE: _Matrix = ...
    """
    | ⬜🟨🟨🟨🟨
    | ⬜🟨⬜⬜🟨
    | ⬜🟨⬜⬜🟨
    | 🟨🟨🟨⬜🟨
    | ⬜🟨⬜⬜⬜
    """
    TRUE: _Matrix = ...
    """
    | ⬜⬜⬜⬜🟨
    | ⬜⬜⬜🟨⬜
    | 🟨⬜🟨⬜⬜
    | ⬜🟨⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    FALSE: _Matrix = ...
    """
    | 🟨⬜⬜⬜🟨
    | ⬜🟨⬜🟨⬜
    | ⬜⬜🟨⬜⬜
    | ⬜🟨⬜🟨⬜
    | 🟨⬜⬜⬜🟨
    """


class Image:
    """グラフィック画像を表すオブジェクト。画像のメモリ内コピー、または
    スクリーンに表示されている画像のどちらでもあり得ます。"""

    # Documentation note: This class is also treated as the `screen` object
    # on EV3 so we use |this image| when it would make sense to say "the screen"
    # in that context and it is automatically replaced when the documentation
    # is generated.

    @overload
    def __init__(self, /, source: Image | ImageFile): ...

    @overload
    def __init__(
        self, /, source: Image, sub: Literal[False], x1: int, y1: int, x2: int, y2: int
    ): ...

    def __init__(self, *args):
        """Image(source, sub=False)


        Arguments:
            source (Image):
                ソース画像。新しいオブジェクトには ``source`` 画像
                オブジェクトのコピーが含まれます。

            sub (bool):
                ``sub`` が ``True`` の場合、画像オブジェクトは
                ``source`` 画像のサブ画像として動作します。

                ``sub=True`` の場合は追加のキーワード引数 ``x1`` 、 ``y1`` 、
                ``x2`` 、 ``y2`` が必要です。これらはサブ画像の範囲として
                使用される ``source`` 画像内の左上と右下の座標を
                指定します。
        """

    @property
    def width(self) -> int:
        """|this image| の幅をピクセル単位で取得します。"""
        return 0

    @property
    def height(self) -> int:
        """|this image| の高さをピクセル単位で取得します。"""
        return 0

    def clear(self) -> None:
        """clear()

        |this image| をクリアします。|this image| のすべてのピクセルが
        :attr:`Color.WHITE <pybricks.parameters.Color.WHITE>` に
        設定されます。
        """

    def draw_pixel(self, x: int, y: int, color: Color = Color.BLACK) -> None:
        """draw_pixel(x, y, color=Color.BLACK)

        |this image| に1ピクセルを描画します。

        Arguments:
            x (int): ピクセルのx座標。
            y (int): ピクセルのy座標。
            color (Color): ピクセルの色。
        """

    def draw_line(
        self,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        width: int = 1,
        color: Color = Color.BLACK,
    ) -> None:
        """draw_line(x1, y1, x2, y2, width=1, color=Color.BLACK)

        |this image| に直線を描画します。

        Arguments:
            x1 (int): 直線の始点のx座標。
            y1 (int): 直線の始点のy座標。
            x2 (int): 直線の終点のx座標。
            y2 (int): 直線の終点のy座標。
            width (int): 直線の幅（ピクセル）。
            color (Color): 直線の色。
        """

    def draw_box(
        self,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        r: int = 0,
        fill: bool = False,
        color: Color = Color.BLACK,
    ) -> None:
        """draw_box(x1, y1, x2, y2, r=0, fill=False, color=Color.BLACK)

        |this image| に矩形を描画します。

        Arguments:
            x1 (int): 矩形の左辺のx座標。
            y1 (int): 矩形の上辺のy座標。
            x2 (int): 矩形の右辺のx座標。
            y2 (int): 矩形の下辺のy座標。
            r (int): 矩形の角の半径。
            fill (bool): ``True`` の場合、矩形が ``color`` で塗りつぶされます。
                それ以外の場合は矩形の輪郭のみが描画されます。
            color (Color): 矩形の色。
        """

    def draw_circle(
        self, x: int, y: int, r: int, fill: bool = False, color: Color = Color.BLACK
    ) -> None:
        """draw_circle(x, y, r, fill=False, color=Color.BLACK)

        |this image| に円を描画します。

        Arguments:
            x (int): 円の中心のx座標。
            y (int): 円の中心のy座標。
            r (int): 円の半径。
            fill (bool): ``True`` の場合、円が ``color`` で塗りつぶされます。
                それ以外の場合は円周のみが描画されます。
            color (Color): 円の色。
        """

    def draw_image(
        self,
        x: int,
        y: int,
        source: Image | ImageFile,
        transparent: Color | None = None,
    ) -> None:
        """draw_image(x, y, source, transparent=None)

        ``source`` 画像を |this image| に描画します。

        Arguments:
            x (int):
                画像の左端が開始されるx軸の値。
            y (int):
                画像の上端が開始されるy軸の値。
            source (Image):
                ソースの :class:`Image <pybricks.parameters.Image>`。
            transparent (Color):
                ``image`` 内で透明として扱う色。透明にしない場合は
                ``None`` 。
        """

    def load_image(self, source: Image | ImageFile) -> None:
        """load_image(source)

        この画像をクリアしてから、 ``source`` 画像を |this image| の
        中央に描画します。

        Arguments:
            source (Image):
                ソースの :class:`Image <pybricks.parameters.Image>`。
        """

    def draw_text(
        self,
        x: int,
        y: int,
        text: str,
        text_color: Color = Color.BLACK,
        background_color: Color | None = None,
    ) -> None:
        """draw_text(x, y, text, text_color=Color.BLACK, background_color=None)

        |this image| にテキストを描画します。

        :meth:`.set_font` で直近に設定されたフォントが使用されます。
        フォントがまだ設定されていない場合は
        :data:`Font.DEFAULT <pybricks.parameters.Font.DEFAULT>` が
        使用されます。

        Arguments:
            x (int):
                テキストの左端が開始されるx軸の値。
            y (int):
                テキストの上端が開始されるy軸の値。
            text (str):
                描画するテキスト。
            text_color (Color):
                テキストの描画に使用する色。
            background_color (Color):
                テキストの背後の矩形を塗りつぶす色。透明な背景にする場合は
                ``None`` 。
        """

    def print(self, *args: Any, sep: str = " ", end: str = "\n") -> None:
        """print(*args, sep=" ", end="\\n")

        |this image| に1行のテキストを出力します。

        このメソッドは組み込みの ``print()`` 関数と同様に動作しますが、
        代わりに |this image| に書き込みます。

        :meth:`.set_font` でフォントを設定できます。フォントが設定
        されていない場合は
        :data:`Font.DEFAULT <pybricks.parameters.Font.DEFAULT>` が
        使用されます。テキストは常に白背景の黒文字で出力されます。

        組み込みの ``print()`` とは異なり、テキストが |this image| に
        収まらないほど長くても折り返されません。単に切り捨てられます。
        ただし、テキストが |this image| の下端を超える場合は、画像全体が
        上にスクロールされ、 |this image| の下部の新しい空白領域に
        テキストが出力されます。

        Arguments:
            args (Any): 出力する0個以上のオブジェクト。
            sep (str): 出力される各オブジェクトの間に挟まれる区切り文字。
            end (str): 最後のオブジェクトの後に出力される行末文字。
        """

    def set_font(self, font: Font) -> None:
        """set_font(font)

        |this image| への描画に使用するフォントを設定します。

        このフォントは :meth:`.draw_text` と :meth:`.print` の両方で
        使用されます。

        Arguments:
            font (Font):
                使用するフォント。
        """

    @staticmethod
    def empty(width: int = 178, height: int = 128) -> Image:
        """empty(width=178, height=128) -> Image

        新しい空の :class:`Image` オブジェクトを作成します。

        Arguments:
            width (int):
                画像の幅（ピクセル）。
            height (int):
                画像の高さ（ピクセル）。

        Returns:
            すべてのピクセルが
            :attr:`Color.WHITE <pybricks.parameters.Color.WHITE>` に
            設定された新しい画像。

        Raises:
            TypeError:
                ``width`` または ``height`` が数値でない場合。
            ValueError:
                ``width`` または ``height`` が1未満の場合。
            RuntimeError:
                新しい画像の割り当てに問題があった場合。
        """


class Font:
    """テキストの描画に使用するフォントを表すオブジェクト。"""

    DEFAULT: Font = ...
    """デフォルトのフォント。"""

    TERMINUS_16: Font = ...
    """高さ16ピクセルのTerminusフォント。"""

    LIBERATIONSANS_14: Font = ...
    """高さ14ピクセルのLiberation Sansレギュラーフォント。"""

    MONO_8X5_8: Font = ...
    """高さ8ピクセル、幅5ピクセルの等幅フォント。"""

    @property
    def family(self) -> str:
        """フォントのファミリー名を取得します。"""
        return "Lucida"

    @property
    def style(self) -> str:
        """style -> str

        フォントスタイルを表す文字列を取得します。

        "Regular" または "Bold" になり得ます。
        """
        return "Regular"

    @property
    def width(self) -> int:
        """フォントの最も幅の広い文字の幅を取得します。"""
        return 0

    @property
    def height(self) -> int:
        """フォントの高さを取得します。"""
        return 0

    def text_width(self, text: str) -> int:
        """text_width(text)

        このフォントを使ってテキストを描画したときの幅を取得します。

        Arguments:
            text (str):
                テキスト。

        Returns:
            int:
                幅（ピクセル）。
        """
        return 0

    def text_height(self, text: str) -> int:
        """text_height(text)

        このフォントを使ってテキストを描画したときの高さを取得します。

        Arguments:
            text (str):
                テキスト。

        Returns:
            int:
                高さ（ピクセル）。
        """
        return 0


class ImageFile:
    """標準のEV3画像へのパス。"""

    _BASE_PATH: str = "/usr/share/images/ev3dev/mono/"
    RIGHT: str = _BASE_PATH + "information/right.png"
    FORWARD: str = _BASE_PATH + "information/forward.png"
    ACCEPT: str = _BASE_PATH + "information/accept.png"
    QUESTION_MARK: str = _BASE_PATH + "information/question_mark.png"
    STOP_1: str = _BASE_PATH + "information/stop_1.png"
    LEFT: str = _BASE_PATH + "information/left.png"
    DECLINE: str = _BASE_PATH + "information/decline.png"
    THUMBS_DOWN: str = _BASE_PATH + "information/thumbs_down.png"
    BACKWARD: str = _BASE_PATH + "information/backward.png"
    NO_GO: str = _BASE_PATH + "information/no_go.png"
    WARNING: str = _BASE_PATH + "information/warning.png"
    STOP_2: str = _BASE_PATH + "information/stop_2.png"
    THUMBS_UP: str = _BASE_PATH + "information/thumbs_up.png"
    EV3: str = _BASE_PATH + "lego/ev3.png"
    EV3_ICON: str = _BASE_PATH + "lego/ev3_icon.png"
    TARGET: str = _BASE_PATH + "objects/target.png"
    BOTTOM_RIGHT: str = _BASE_PATH + "eyes/bottom_right.png"
    BOTTOM_LEFT: str = _BASE_PATH + "eyes/bottom_left.png"
    EVIL: str = _BASE_PATH + "eyes/evil.png"
    CRAZY_2: str = _BASE_PATH + "eyes/crazy_2.png"
    KNOCKED_OUT: str = _BASE_PATH + "eyes/knocked_out.png"
    PINCHED_RIGHT: str = _BASE_PATH + "eyes/pinched_right.png"
    WINKING: str = _BASE_PATH + "eyes/winking.png"
    DIZZY: str = _BASE_PATH + "eyes/dizzy.png"
    DOWN: str = _BASE_PATH + "eyes/down.png"
    TIRED_MIDDLE: str = _BASE_PATH + "eyes/tired_middle.png"
    MIDDLE_RIGHT: str = _BASE_PATH + "eyes/middle_right.png"
    SLEEPING: str = _BASE_PATH + "eyes/sleeping.png"
    MIDDLE_LEFT: str = _BASE_PATH + "eyes/middle_left.png"
    TIRED_RIGHT: str = _BASE_PATH + "eyes/tired_right.png"
    PINCHED_LEFT: str = _BASE_PATH + "eyes/pinched_left.png"
    PINCHED_MIDDLE: str = _BASE_PATH + "eyes/pinched_middle.png"
    CRAZY_1: str = _BASE_PATH + "eyes/crazy_1.png"
    NEUTRAL: str = _BASE_PATH + "eyes/neutral.png"
    AWAKE: str = _BASE_PATH + "eyes/awake.png"
    UP: str = _BASE_PATH + "eyes/up.png"
    TIRED_LEFT: str = _BASE_PATH + "eyes/tired_left.png"
    ANGRY: str = _BASE_PATH + "eyes/angry.png"
