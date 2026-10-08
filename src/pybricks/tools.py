# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2023 The Pybricks Authors

"""時間計測、データロギング、線形代数のための共通ツール。"""

from __future__ import annotations

from typing import TYPE_CHECKING, Self, overload

if TYPE_CHECKING:
    from collections.abc import Coroutine, Sequence
    from typing import Any

    from ._common import MaybeAwaitable, MaybeAwaitableTuple
    from .parameters import Number


def wait(time: Number) -> MaybeAwaitable:
    """wait(time)

    指定した時間だけユーザープログラムを一時停止します。

    Arguments:
        time (Number, ms): 待機する時間。
    """


class StopWatch:
    """時間間隔を測定するストップウォッチです。携帯電話の
    ストップウォッチ機能に似ています。"""

    def __init__(self): ...

    def time(self) -> int:
        """time() -> int: ms

        ストップウォッチの現在の時間を取得します。

        Returns:
            経過時間。
        """

    def pause(self) -> None:
        """pause()

        ストップウォッチを一時停止します。"""

    def resume(self) -> None:
        """resume()

        ストップウォッチを再開します。"""

    def reset(self) -> None:
        """reset()

        ストップウォッチの時間を0にリセットします。

        実行状態は影響を受けません。

        * 一時停止していた場合は、一時停止のままです（ただし0になります）。
        * 実行中だった場合は、実行中のままです（ただし0から再開します）。
        """


class DataLog:
    """ファイルを作成してデータを記録します。"""

    def __init__(
        self,
        *headers: str,
        name: str = "log",
        timestamp: bool = True,
        extension: str = "csv",
        append: bool = False,
    ):
        """DataLog(*headers, name='log', timestamp=True, extension='csv', append=False)

        Arguments:
            headers (str, str, ...): 列ヘッダー。これらはデータ列の
                名前です。たとえば ``'time'`` や ``'angle'`` を
                選びます。
            name (str): ファイル名。
            timestamp (bool): ``True`` を選択すると、ファイル名に日付と
                時刻が追加されます。これにより、ファイルは一意の名前に
                なります。 ``False`` を選択すると、タイムスタンプは
                省略されます。
            extension (str): ファイル拡張子。
            append (bool): ``True`` を選択すると、既存のデータログ
                ファイルを再度開いてデータを追記します。 ``False`` を
                選択すると、既存のデータが消去されます。ファイルが
                まだ存在しない場合は、どちらの場合も空のファイルが
                作成されます。
        """

    def log(self, *values: Any) -> None:
        """log(value1, value2, ...)

        1つ以上の値をファイルの新しい行に保存します。

        Arguments:
            values (object, object, ...): 1つ以上のオブジェクトまたは値。
        """


class Matrix:
    """行列の数学的表現です。互換性のあるサイズの行列に対して
    加算（ ``A + B`` ）、減算（ ``A - B`` ）、行列乗算（ ``A * B`` ）を
    サポートします。

    スカラー乗算（ ``c * A`` または ``A * c`` ）とスカラー除算
    （ ``A / c`` ）もサポートします。

    :class:`.Matrix` オブジェクトはイミュータブルです。"""

    def __add__(self, other) -> Matrix: ...

    def __iadd__(self, other) -> Self: ...

    def __sub__(self, other) -> Matrix: ...

    def __isub__(self, other) -> Self: ...

    def __mul__(self, other) -> Matrix: ...

    def __rmul__(self, other) -> Matrix: ...

    def __imul__(self, other) -> Self: ...

    def __truediv__(self, other) -> Matrix: ...

    def __itruediv__(self, other) -> Self: ...

    def __floordiv__(self, other) -> Matrix: ...

    def __ifloordiv__(self, other) -> Self: ...

    def __init__(self, rows: Sequence[Sequence[float]]):
        """Matrix(rows)

        Arguments:
            rows (list): 行のリスト。各行はそれ自体が数値のリストです。

        """

    @property
    def T(self) -> Matrix:
        """元の行列を転置した新しい :class:`.Matrix` を返します。"""

    @property
    def shape(self) -> tuple[int, int]:
        """タプル（ ``m`` 、 ``n`` ）を返します。
        ``m`` は行数、 ``n`` は列数です。
        """


@overload
def vector(x: float, y: float) -> Matrix:
    """
    形状が（ ``2`` 、 ``1`` ）の :class:`.Matrix` を作成する便利な
    関数です。

    Arguments:
        x (float): ベクトルのx座標。
        y (float): ベクトルのy座標。

    Returns:
        列ベクトルの形状を持つ行列。
    """


@overload
def vector(x: float, y: float, z: float) -> Matrix:
    """
    形状が（ ``3`` 、 ``1`` ）の :class:`.Matrix` を作成する便利な
    関数です。

    Arguments:
        x (float): ベクトルのx座標。
        y (float): ベクトルのy座標。
        z (float): ベクトルのz座標。

    Returns:
        列ベクトルの形状を持つ行列。
    """


def vector(*args):
    """
    vector(x, y) -> Matrix
    vector(x, y, z) -> Matrix

    形状が（ ``2`` 、 ``1`` ）または（ ``3`` 、 ``1`` ）の
    :class:`.Matrix` を作成する便利な関数です。

    Arguments:
        x (float): ベクトルのx座標。
        y (float): ベクトルのy座標。
        z (float): ベクトルのz座標（オプション）。

    Returns:
        列ベクトルの形状を持つ行列。
    """


def cross(a: Matrix, b: Matrix) -> Matrix:
    """
    cross(a, b) -> Matrix

    2つのベクトルの外積 ``a`` × ``b`` を取得します。

    Arguments:
        a (Matrix): 3次元ベクトル。
        b (Matrix): 3次元ベクトル。

    Returns:
        外積。これも3次元ベクトルです。
    """


def read_input_byte(last: bool = False, chr: bool = False) -> int | str | None:
    """
    read_input_byte() -> int | str | None

    ブロッキングせずに標準入力から1バイトを読み取り、入力バッファから
    削除します。

    Arguments:
        last (bool): ``True`` を選択すると、バッファ内の最後（最新）の
            バイトを読み取り、残りを破棄します。 ``False`` を選択すると、
            最初（最古）のバイトのみを読み取ります。
        chr (bool): ``True`` を選択すると、結果を1文字の文字列に
            変換します。

    Returns:
        読み取られたバイト。数値（ ``0`` から ``255`` ）または文字列
        （例： ``"B"`` ）として返されます。データが利用できない場合は
        ``None`` を返します。 ``chr=True`` の場合、読み取られたバイトが
        文字として表示できないときも ``None`` を返します。
    """


def hub_menu(*symbols: int | str) -> int | str:
    """
    hub_menu(symbol1, symbol2, ...) -> int | str

    ハブのディスプレイにメニューを表示し、ユーザーがボタンを使って
    項目を選択するのを待ちます。他のどのプログラムを実行するかを
    選べる、独自のメニュープログラムで使用できます。

    これは単に、ディスプレイ、ボタン、待機を組み合わせて単純なメニューを
    作る便利な関数であることに注意してください。つまり、プログラムの
    先頭だけでなく、プログラム内のどこでも使用できます。

    Arguments:
        symbol1 (int or str): メニューに表示する最初のシンボル。
        symbol2 (int or str): 2番目のシンボル、以下同様に続きます。

    Returns:
        選択されたシンボル。
    """


def multitask(*coroutines: Coroutine, race=False) -> MaybeAwaitableTuple:
    """
    multitask(coroutine1, coroutine2, ...) -> tuple

    複数のコルーチンを同時に実行します。これは新しいコルーチンを作成し、
    他の ``multitask`` 文を含む、他のコルーチンと同様に使用できます。

    Arguments:
        coroutines (coroutine, coroutine, ...): 並列に実行する
            1つ以上のコルーチン。
        race (bool): ``False`` を選択すると、すべてのコルーチンの完了を
            待ちます。 ``True`` を選択すると、1つのコルーチンが完了する
            のを待ってから他をキャンセルします。まるで「競争」のようです。

    Returns:
        各コルーチンの戻り値のタプル。完了しなかったコルーチンの
        戻り値は ``None`` になります。
    """


def run_task(coroutine: Coroutine) -> bool | None:
    """
    run_task(coroutine) -> bool | None

    プログラムの残りをブロックしながら、コルーチンを最初から最後まで
    実行します。これは主にプログラムのメインコルーチンを実行するために
    使用されます。

    この関数の呼び出しをネストすることはできません。

    Arguments:
        coroutine (coroutine): 実行するメインコルーチン。

    Returns:
        ``coroutine`` が指定されない場合、この関数は実行ループが
        現在アクティブかどうか（ ``True`` か ``False`` か）を返します。
    """


# Hide type-only names from jedi completions in the module namespace.
if TYPE_CHECKING:
    del Any
    del Coroutine
    del MaybeAwaitable
    del MaybeAwaitableTuple
    del Number
    del Sequence
