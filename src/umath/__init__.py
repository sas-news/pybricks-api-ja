# SPDX-License-Identifier: MIT
# SPDX-License-Identifier: PSF-2.0
# Copyright (c) 2021 The Pybricks Authors
#
# Portions of the documentation copied and adapted from:
# https://docs.python.org/3/library/math.html
# Copyright (c) 2001-2021 Python Software Foundation


"""
数学関数。
"""

e = 2.718282
"""数学定数 e。"""


pi = 3.141593
"""数学定数 π。"""


def sin(x: float) -> float:
    """sin(x) -> float

    角度の正弦を取得します。

    Arguments:
        x (float): ラジアン単位の角度。

    Returns:
        ``x`` の正弦。
    """


def asin(x: float) -> float:
    """asin(x) -> float

    逆正弦演算を適用します。

    Arguments:
        x (float): 対辺 / 斜辺。

    Returns:
        ``x`` の逆正弦（ラジアン単位）。
    """


def cos(x: float) -> float:
    """cos(x) -> float

    角度の余弦を取得します。

    Arguments:
        x (float): ラジアン単位の角度。

    Returns:
        ``x`` の余弦。
    """


def acos(x: float) -> float:
    """acos(x) -> float

    逆余弦演算を適用します。

    Arguments:
        x (float): 隣辺 / 斜辺。

    Returns:
        ``x`` の逆余弦（ラジアン単位）。
    """


def tan(x: float) -> float:
    """tan(x) -> float

    角度の正接を取得します。

    Arguments:
        x (float): ラジアン単位の角度。

    Returns:
        ``x`` の正接。
    """


def atan(x: float) -> float:
    """atan(x) -> float

    逆正接演算を適用します。

    Arguments:
        x (float): 対辺 / 隣辺。

    Returns:
        ``x`` の逆正接（ラジアン単位）。
    """


def atan2(b: float, a: float) -> float:
    """atan2(b, a) -> float

    ``b / a`` に対して逆正接演算を適用し、``b`` と ``a`` の符号を考慮して
    期待される角度を生成します。

    Arguments:
        b (float): 三角形の対辺。
        a (float): 三角形の隣辺。

    Returns:
        ``b / a`` の逆正接（ラジアン単位）。
    """


def degrees(x: float) -> float:
    """degrees(x) -> float

    角度をラジアンから度に変換します。

    Arguments:
        x (float): ラジアン単位の角度。

    Returns:
        度単位の角度。
    """


def radians(x: float) -> float:
    """radians(x) -> float

    角度を度からラジアンに変換します。

    Arguments:
        x (float): 度単位の角度。

    Returns:
        ラジアン単位の角度。
    """


def pow(x: float, y: float) -> float:
    """pow(x, y) -> float

    ``x`` の ``y`` 乗を取得します。

    Arguments:
        x (float): 底。
        y (float): 指数。

    Returns:
        ``x`` の ``y`` 乗。
    """


def exp(x: float) -> float:
    """exp(x) -> float

    :attr:`e` の ``x`` 乗を取得します。

    Arguments:
        x (float): 指数。

    Returns:
        :attr:`e` の ``x`` 乗。
    """


def log(x: float) -> float:
    """log(x) -> float

    自然対数を取得します。

    Arguments:
        x (float): 値。

    Returns:
        ``x`` の自然対数。
    """


def sqrt(x: float) -> float:
    """sqrt(x) -> float

    平方根を取得します。

    Arguments:
        x (float): 値 ``x``。

    Returns:
        ``x`` の平方根。
    """


def ceil(x: float) -> int:
    """ceil(x) -> int

    切り上げます。

    Arguments:
        x (float): 丸める対象の値。

    Returns:
        正の無限大方向に丸めた値。
    """


def floor(x: float) -> int:
    """floor(x) -> int

    切り捨てます。

    Arguments:
        x (float): 丸める対象の値。

    Returns:
        負の無限大方向に丸めた値。
    """


def trunc(x: float) -> int:
    """trunc(x) -> int

    小数を切り捨てて値の整数部分を取得します。

    これは ``0`` 方向への丸めと同じです。

    Arguments:
        x (float): 切り捨てる対象の値。

    Returns:
        値の整数部分。
    """


def fmod(x: float, y: float) -> float:
    """fmod(x, y) -> float

    ``x / y`` の剰余を取得します。

    :func:`modf` と混同しないでください。

    Arguments:
        x (float): 分子。
        y (float): 分母。

    Returns:
        除算後の剰余。
    """


def fabs(x: float) -> float:
    """fabs(x) -> float

    絶対値を取得します。

    Arguments:
        x (float): 値。

    Returns:
        ``x`` の絶対値。
    """


def modf(x: float) -> tuple[float, float]:
    """modf(x) -> tuple[float, float]

    ``x`` の小数部分と整数部分を取得します。いずれも ``x`` と同じ符号
    になります。

    :func:`fmod` と混同しないでください。

    Arguments:
        x (float): 分解する値。

    Returns:
        小数部分と整数部分のタプル。
    """


def frexp(x: float) -> tuple[float, int]:
    """frexp(x) -> tuple[float, float]

    値 ``x`` を ``x == m * (2 ** p)`` となるようなタプル ``(m, p)``
    に分解します。

    Arguments:
        x (float): 分解する値。

    Returns:
        ``m`` と ``p`` のタプル。
    """


def ldexp(m: float, p: int) -> float:
    """ldexp(m, p) -> float

    ``m * (2 ** p)`` を計算します。

    Arguments:
        m (float): 値。
        p (float): 指数。

    Returns:
        ``m * (2 ** p)`` の結果。
    """


def copysign(x: float, y: float) -> float:
    """copysign(x, y) -> float

    ``y`` の符号を持つ ``x`` を取得します。

    Arguments:
        x (float): 戻り値の大きさを決定します。
        y (float): 戻り値の符号を決定します。

    Returns:
        ``y`` の符号を持つ ``x``。
    """


def isfinite(x: float) -> bool:
    """isfinite(x) -> bool

    値が有限かどうかを確認します。

    Arguments:
        x (float): 確認する値。

    Returns:
        ``x`` が有限なら ``True``、そうでなければ ``False``。
    """


def isinfinite(x: float) -> bool:
    """isinfinite(x) -> bool

    値が無限かどうかを確認します。

    Arguments:
        x (float): 確認する値。

    Returns:
        ``x`` が無限なら ``True``、そうでなければ ``False``。
    """


def isnan(x: float) -> bool:
    """isnan(x) -> bool

    値が非数かどうかを確認します。

    Arguments:
        x (float): 確認する値。

    Returns:
        ``x`` が非数なら ``True``、そうでなければ ``False``。
    """
