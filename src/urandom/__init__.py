# SPDX-License-Identifier: MIT
# SPDX-License-Identifier: PSF-2.0
# Copyright (c) 2021 The Pybricks Authors
#
# Portions of the documentation copied from:
# https://docs.python.org/3/library/random.html
# Copyright (c) 2001-2021 Python Software Foundation

"""
このモジュールは擬似乱数生成器を実装しています。

このモジュールのすべての関数は位置引数で使用する必要があります。キーワード
引数はサポートされていません。
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, overload

if TYPE_CHECKING:
    from collections.abc import Sequence


def seed(a: int | None = None) -> None:
    """
    seed(value=None)

    乱数生成器を初期化します。

    これはモジュールがインポートされるときに呼び出されるため、通常は
    呼び出す必要はありません。

    Arguments:
        value: シード値。 ``None`` を使用すると、システムタイマーが使用されます。
    """


@overload
def randrange(stop: int) -> int: ...


@overload
def randrange(start: int, stop: int) -> int: ...


@overload
def randrange(start: int, stop: int, step: int) -> int: ...


def randrange(start, stop, step):
    """
    randrange(stop) -> int
    randrange(start, stop) -> int
    randrange(start, stop, step) -> int

    ``range(start, stop, step)`` からランダムに選択された要素を返します。

    たとえば、``randrange(1, 7, 2)`` は ``1`` から ``7`` まで（``7`` を除く）
    ``2`` 刻みの乱数を返します。つまり、``1``、``3``、``5`` のいずれかを
    返します。


    Arguments:
        start (int): 最小値。引数が1つだけの場合は ``0`` が既定です。
        stop (int): 最大値。この値は範囲に *含まれません*。
        step (int): 値と値の間の増分。引数が1つまたは2つだけの場合は ``1``
            が既定です。

    Returns:
        乱数。
    """


def randint(a: int, b: int) -> int:
    """
    randint(a, b) -> int

    a ≤ N ≤ b を満たすランダムな整数 N を取得します。

    Arguments:
        a (int): 最小値。この値は範囲に *含まれます*。
        b (int): 最大値。この値は範囲に *含まれます*。

    Returns:
        ランダムな整数。
    """


def getrandbits(k: int) -> int:
    """
    getrandbits(k) -> int

    0 ≤ N < ``2**k`` を満たすランダムな整数 N を取得します。

    Arguments:
        k (int): 結果に使用するビット数。
    """


def choice(seq: Sequence[Any]) -> Any:
    """
    choice(sequence) -> Any

    タプルやリストなどのシーケンスからランダムな要素を取得します。

    Arguments:
        sequence: ランダムな要素を選択するシーケンス。

    Returns:
        ランダムに選択された要素。

    Raises:
        ``IndexError``: シーケンスが空の場合。
    """


def random() -> float:
    """
    random() -> float

    0 ≤ x < 1 を満たすランダムな値 x を取得します。

    Returns:
        ランダムな値。
    """


def uniform(a: float, b: float) -> float:
    """
    uniform(a, b) -> float

    a ≤ x ≤ b を満たすランダムな浮動小数点値 x を取得します。

    Arguments:
        a (float): 最小値。
        b (float): 最大値。

    Returns:
        ランダムな値。
    """


# Hide type-only names from jedi completions in the module namespace.
if TYPE_CHECKING:
    del Sequence
