# SPDX-License-Identifier: MIT
# Copyright (c) 2021 The Pybricks Authors
#
# Documentation copied from:
# https://raw.githubusercontent.com/micropython/micropython/master/docs/library/micropython.rst
# Copyright (c) 2014-2021, Damien P. George, Paul Sokolovsky, and contributors

"""
MicroPythonの内部機能へのアクセスと制御を行います。
"""

from typing import Any, overload


@overload
def const(value: int) -> int: ...


@overload
def const(value: str) -> str: ...


@overload
def const(value: float) -> float: ...


@overload
def const(value: tuple) -> tuple: ...


def const(value):
    """
    const(value) -> Any

    値を定数として宣言し、コードをより効率的にします。

    メモリ使用量をさらに減らすには、名前の前にアンダースコアを
    付けます（``_ORANGES``）。この定数は同じファイル内でのみ
    使用できます。

    値を別のモジュールからインポートしたい場合は、アンダースコアを
    付けない名前を使います（``APPLES``）。この場合、メモリを
    少し多く使用します。

    Arguments:
        value (int or float or str or tuple): 定数にするリテラル。

    Returns:
        定数の値。
    """


@overload
def opt_level() -> int: ...


@overload
def opt_level(level: int) -> None: ...


def opt_level(*args):
    """
    ハブ上でコンパイルされるコードの最適化レベルを設定します。

    0. アサーション文が有効になります。組み込みの ``__debug__`` 変数は
       ``True`` になります。スクリプトの行番号が保存されるため、
       例外が発生したときに報告できます。
    1. アサーションは無視され、``__debug__`` は ``False`` になります。
       スクリプトの行番号は保存されます。
    2. アサーションは無視され、``__debug__`` は ``False`` になります。
       スクリプトの行番号は保存されます。
    3. アサーションは無視され、``__debug__`` は ``False`` になります。
       スクリプトの行番号は保存「されません」。

    これはREPLで実行するコードにのみ適用されます。通常のスクリプトは
    ハブに送信される前にすでにコンパイルされているためです。

    Arguments:
        level (int): 設定するレベル。

    Returns:
        引数を指定しない場合、現在の最適化レベルを返します。

    """


@overload
def mem_info() -> None: ...


@overload
def mem_info(verbose: Any) -> None: ...


def mem_info(*args):
    """
    mem_info()
    mem_info(verbose)

    スタックとヒープのメモリ使用量に関する情報を出力します。

    Arguments:
        verbose: 任意の値を指定すると、ヒープ全体も出力します。
            どのブロックが使用中で、どれが空きかを示します。
    """


@overload
def qstr_info() -> None: ...


@overload
def qstr_info(verbose: Any) -> None: ...


def qstr_info(*args):
    """
    qstr_info()
    qstr_info(verbose)

    インターンされた文字列の数と、それらが使用するRAMの量を出力します。

    MicroPythonは文字列のインターンによりRAMとROMの両方を節約します。
    これにより、同じ文字列の重複コピーを保持せずに済みます。

    Arguments:
        verbose: 任意の値を指定すると、RAMにインターンされたすべての
            文字列の名前も出力します。
    """


def stack_use() -> int:
    """
    stack_use() -> int

    使用中のスタック量を確認します。スクリプト内の異なる地点での
    スタック使用量の差を計算するために使用できます。

    Returns:
        現在使用中のスタック量。
    """


def heap_lock() -> None:
    """
    heap_lock()

    ヒープをロックします。ロック中はメモリ割り当てができません。
    ヒープの割り当てが試みられると ``MemoryError`` が発生します。
    """


def heap_unlock() -> int:
    """
    heap_unlock() -> int

    ヒープのロックを解除します。メモリ割り当てが再び許可されます。

    :func:`heap_lock()` を複数回呼び出した場合、ヒープを再び使用可能にするには
    :func:`heap_unlock()` を同じ回数呼び出す必要があります。

    Returns:
        ロック解除後のロック深さ。ロックが解除されると ``0`` になります。
    """


def kbd_intr(chr: int) -> None:
    """
    kbd_intr(chr)

    入力ウィンドウで入力したときに ``KeyboardInterrupt`` 例外を
    発生させる文字を設定します。デフォルトでは ``3`` に設定されており、
    これは :kbd:`Ctrl` :kbd:`C` を押すことに相当します。

    Arguments:
        chr (int): ``KeyboardInterrupt`` を発生させる文字。
            この機能を無効にするには ``-1`` を選択します。
    """
