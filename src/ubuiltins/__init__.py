# SPDX-License-Identifier: MIT
# SPDX-License-Identifier: PSF-2.0
# Copyright (c) 2021 The Pybricks Authors
#
# Portions of documentation copied from:
# https://raw.githubusercontent.com/micropython/micropython/1e6d18c915ccea0b6a19ffec9710d33dd7e5f866/docs/library/builtins.rst
# Copyright (c) 2014-2021, Damien P. George, Paul Sokolovsky, and contributors
#
# Portions of the documentation copied from:
# https://docs.python.org/3/library/builtins.html
# https://docs.python.org/3/library/constants.html
# https://docs.python.org/3/library/stdtypes.html
# https://docs.python.org/3/library/exceptions.html
# Copyright (c) 2001-2021 Python Software Foundation

"""
以下の関数と例外は、何もインポートせずに使用できます。

このモジュールのほとんどの関数とクラスは、キーワード引数を受け付けません。
"""

import builtins
from collections.abc import Callable, Hashable, Iterable, Iterator, Mapping, Sequence
from typing import (
    Any,
    Literal,
    Self,
    SupportsComplex,
    SupportsFloat,
    SupportsInt,
    overload,
)

import uio
import usys

# These get overridden later on, but we still want to use the originals
# for the purpose of typing the doc strings.
_bool = bool
_bytearray = bytearray
_bytes = bytes
_callable = callable
_classmethod = classmethod
_complex = complex
_dict = dict
_float = float
_int = int
_list = list
_str = str
_tuple = tuple
_type = type


# Functions and types


def abs(x: Any) -> Any:
    """abs(x) -> Any

    数値の絶対値を返します。

    引数には整数、浮動小数点数、または ``__abs__()`` を実装する任意の
    オブジェクトを指定できます。引数が複素数の場合は、その大きさが返されます。

    Arguments:
        x (Any): 値。

    Returns:
        ``x`` の絶対値。
    """


def all(x: Iterable) -> _bool:
    """all(x) -> bool

    イテラブルのすべての要素が真かどうかを確認します。

    以下と同等です::

        def all(x):
            for element in x:
                if not element:
                    return False
            return True

    Arguments:
        x (Iterable): 確認するイテラブル。

    Returns:
        イテラブル ``x`` が空の場合、またはすべての要素が真の場合は
        ``True`` 。それ以外は ``False`` 。
    """


def any(x: Iterable) -> _bool:
    """any(x) -> bool

    イテラブルの少なくとも1つの要素が真かどうかを確認します。

    以下と同等です::

        def any(x):
            for element in x:
                if element:
                    return True
            return False

    Arguments:
        x (Iterable): 確認するイテラブル。

    Returns:
        ``x`` の少なくとも1つの要素が真の場合は ``True`` 。
        それ以外は ``False`` 。
    """


def bin(x: Any) -> _str:
    """bin(x) -> str

    整数を2進数表現に変換します。結果は ``0b`` で始まる文字列で、
    有効なPython式です。たとえば ``bin(5)`` は ``"0b101"`` になります。

    Arguments:
        x (int): 変換する値。

    Returns:
        入力の2進数表現の文字列。
    """


class bool:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, x: Any) -> None: ...

    def __init__(self, *args) -> None:
        """
        bool(\u200b)
        bool(x)

        ``True`` または ``False`` のいずれかのブール値を作成します。

        入力値は標準の真偽テスト手順で変換されます。入力が与えられない
        場合は ``False`` とみなされます。

        Arguments:
            x: 変換する値。

        Returns:
            真偽テストの結果。
        """


class bytes:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, source: _int) -> None: ...

    @overload
    def __init__(self, source: _bytes | _bytearray | Iterable[_int]) -> None: ...

    @overload
    def __init__(self, source: _str, encoding: _str) -> None: ...

    def __init__(self, *args):
        """
        bytes(\u200b)
        bytes(integer)
        bytes(iterable)
        bytes(string, encoding)

        0 ≤ x ≤ 255 の範囲の整数のシーケンスである、新しい ``bytes``
        オブジェクトを作成します。このオブジェクトは *イミュータブル* で、
        作成後に内容を変更することは *できません* 。

        引数が与えられない場合は、空の ``bytes`` オブジェクトを作成します。

        Arguments:
            integer (int): 引数が単一の整数の場合は、ゼロの ``bytes``
              オブジェクトを作成します。この引数はゼロの個数を指定します。
            iterable (iter): 引数が ``bytearray`` 、 ``bytes``
              オブジェクト、またはその他の整数のイテラブルの場合は、引数と同じ
              バイトシーケンスを持つ ``bytes`` オブジェクトを作成します。
            string (str): 引数が文字列の場合は、エンコードされた文字列を含む
              ``bytes`` オブジェクトを作成します。
            encoding (str): ``string`` 引数に使用するエンコーディングを
              指定します。 ``"utf-8"`` のみがサポートされています。
        """


class bytearray:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, source: _int) -> None: ...

    @overload
    def __init__(self, source: _bytes | _bytearray | _str | Iterable[_int]) -> None: ...

    def __init__(self, *args):
        """
        bytearray(\u200b)
        bytearray(integer)
        bytearray(iterable)
        bytearray(string)

        0 ≤ x ≤ 255 の範囲の整数のシーケンスである、新しい ``bytearray``
        オブジェクトを作成します。このオブジェクトは *ミュータブル* で、
        作成後に内容を変更することが *できます* 。

        引数が与えられない場合は、空の ``bytearray`` オブジェクトを作成します。

        Arguments:
            integer (int): 引数が単一の整数の場合は、ゼロの ``bytearray``
              オブジェクトを作成します。この引数はゼロの個数を指定します。
            iterable (iter): 引数が ``bytearray`` 、 ``bytes``
              オブジェクト、またはその他の整数のイテラブルの場合は、引数と同じ
              バイトシーケンスを持つ ``bytearray`` オブジェクトを作成します。
            string (str): 引数が文字列の場合は、エンコードされた文字列を含む
              ``bytearray`` オブジェクトを作成します。
        """


def callable(object: Any) -> _bool:
    """
    callable(object) -> bool

    オブジェクトが呼び出し可能かどうかを確認します。

    Arguments:
        object: 確認するオブジェクト。

    Returns:
        引数が呼び出し可能とみなされる場合は ``True`` 、そうでない場合は
        ``False`` 。
    """


def chr(x: _int) -> _str:
    """chr(x) -> str

    Unicodeコードが整数 ``x`` である文字を表す文字列を返します。
    これは :meth:`ord` の逆関数です。たとえば ``chr(97)`` は
    ``"a"`` になります。

    Arguments:
        x (int): 変換する値（0-255）。

    Returns:
        指定したUnicode値に対応する、1文字の文字列。
    """


def classmethod(method: _callable) -> _callable:
    """
    メソッドをクラスメソッドに変換します。
    """


class complex:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(
        self, real: _float | SupportsFloat | _complex | SupportsComplex
    ) -> None: ...

    @overload
    def __init__(
        self,
        real: _float | SupportsFloat | _complex | SupportsComplex,
        imag: _float | SupportsFloat | _complex | SupportsComplex,
    ) -> None: ...

    @overload
    def __init__(self, value: _str) -> None: ...

    def __init__(self, *args) -> None:
        """
        complex(string)
        complex(a=0, b=0)

        文字列または数値のペアから複素数を作成します。

        文字列を指定する場合は ``'1+2j'`` の形式にする必要があります。
        数値のペアを指定する場合、結果は ``a + b * j``
        として計算されます。

        Arguments:
            string (str): ``'1+2j'`` の形式の文字列。
            a (float or complex): 実数または複素数。
            b (float or complex): 実数または複素数。

        Returns:
            結果の複素数。
        """


class dict:
    @overload
    def __init(self) -> None: ...

    @overload
    def __init(self, **kwargs) -> None: ...

    def __init__(self, *args, **kwargs) -> None:
        """
        dict(**kwargs)
        dict(mapping, **kwargs)
        dict(iterable, **kwargs)

        辞書オブジェクトを作成します。

        包括的なリファレンスと例については、標準の
        `Pythonドキュメント
        <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_
        を参照してください。
        """


@overload
def dir() -> _list[_str]: ...


@overload
def dir(object: Any) -> _list[_str]: ...


def dir(*args) -> _list[_str]:
    """
    dir() -> list[str]
    dir(object) -> list[str]

    オブジェクトの属性のリストを取得します。

    object引数が与えられない場合は、現在のローカルスコープ内の名前の
    リストを取得します。

    Arguments:
        object: 有効な属性を確認するオブジェクト。

    Returns:
        オブジェクトの属性のリスト、または現在のローカルスコープ内の
        名前のリスト。
    """


@overload
def divmod(a: _int, b: _int) -> _tuple[_int, _int]: ...


@overload
def divmod(a: _float, b: _float) -> _tuple[_float, _float]: ...


def divmod(a, b):
    """
    divmod(a, b) -> tuple[int, int]

    2つの整数を除算したときの商と余りを取得します。

    ``a`` または ``b`` が浮動小数点数の場合の期待される動作については、
    標準の `Python divmodドキュメント
    <https://docs.python.org/3/library/functions.html#divmod>`_
    を参照してください。

    Arguments:
        a (int): 分子。
        b (int): 分母。

    Returns:
        商 ``a // b`` と余り ``a % b`` のタプル。
    """


class enumerate:
    @overload
    def __init__(self, iterable: Iterable) -> None: ...

    @overload
    def __init__(self, iterable: Iterable, start: _int) -> None: ...

    def __init__(self, *args) -> None:
        """
        enumerate(iterable, start=0)

        既存のイテレーターに数値インデックスを付加して列挙します。

        この関数は以下と同等です::

            def enumerate(sequence, start=0):
                n = start
                for elem in sequence:
                    yield n, elem
                    n += 1
        """


@overload
def eval(expression: _str) -> Any: ...


@overload
def eval(expression: _str, globals: _dict) -> Any: ...


@overload
def eval(expression: _str, globals: _dict, locals: Mapping) -> Any: ...


def eval(*args):
    """
    eval(expression) -> Any
    eval(expression, globals) -> Any
    eval(expression, globals, locals) -> Any

    式の結果を評価します。

    構文エラーは例外として報告されます。

    Arguments:
        expression (str): 結果を評価する式。
        globals (dict): 指定した場合、式内で使用可能な関数を制御します。
            デフォルトではグローバルスコープにアクセスできます。
        locals (dict): 指定した場合、式内で使用可能な関数を制御します。
            デフォルトは ``globals`` と同じです。

    Returns:
        式を実行して得られた値。
    """


@overload
def exec(object: Any) -> None: ...


@overload
def exec(object: Any, globals: _dict) -> None: ...


@overload
def exec(object: Any, globals: _dict, locals: Mapping) -> None: ...


def exec(*args):
    """
    exec(expression)
    exec(expression, globals)
    exec(expression, globals, locals)

    MicroPythonコードを実行します。

    構文エラーは例外として報告されます。

    Arguments:
        expression (str): 実行するコード。
        globals (dict): 指定した場合、式内で使用可能な関数を制御します。
            デフォルトではグローバルスコープにアクセスできます。
        locals (dict): 指定した場合、式内で使用可能な関数を制御します。
            デフォルトは ``globals`` と同じです。
    """


class float:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, x: _int) -> None: ...

    @overload
    def __init__(self, x: SupportsFloat) -> None: ...

    @overload
    def __init__(self, x: _str) -> None: ...

    def __init__(self, *args) -> None:
        """float(x=0.0)

        指定したオブジェクトから浮動小数点数を作成します。

        Arguments:
            x (int or float or str): 変換する数値または文字列。
        """


@overload
def getattr(object: Any, name: _str) -> Any: ...


@overload
def getattr(object: Any, name: _str, default: Any) -> Any: ...


def getattr(*args):
    """
    getattr(object, name) -> Any
    getattr(object, name, default) -> Any

    指定した ``object`` 内の ``name`` という属性を検索します。

    Arguments:
        object: 属性を検索するオブジェクト。
        name (str): 属性の名前。
        default: 属性が見つからない場合に返すオブジェクト。

    Returns:
        指定した名前の属性の値。
    """


def globals() -> builtins.dict[_str, Any]:
    """
    globals() -> dict

    現在のグローバルシンボルテーブルを表す辞書を取得します。

    Returns:
        グローバルの辞書。
    """


def hasattr(object: Any, name: _str) -> _bool:
    """
    hasattr(object, name) -> bool

    オブジェクトに属性が存在するかどうかを確認します。

    Arguments:
        object: 属性を検索するオブジェクト。
        name (str): 属性の名前。

    Returns:
        その名前の属性が存在する場合は ``True`` 、そうでない場合は
        ``False`` 。
    """


def hash(object: Any) -> _int:
    """
    hash(object) -> int

    オブジェクトがサポートしている場合、そのハッシュ値を取得します。

    Arguments:
        object: ハッシュ値を取得するオブジェクト。

    Returns:
        ハッシュ値。
    """


@overload
def help() -> None: ...


@overload
def help(object: Any) -> None: ...


def help(*args) -> None:
    """
    help()
    help(object)

    オブジェクトに関する情報を取得します。

    引数が与えられない場合、この関数はREPLを操作する手順を表示します。
    引数が ``"modules"`` の場合は、利用可能なモジュールを表示します。

    Arguments:
        object: ヘルプ情報を表示するオブジェクト。
    """


def hex(x: int) -> _str:
    """hex(x) -> str

    整数を16進数表現に変換します。結果は ``0x`` で始まる小文字の文字列で、
    有効なPython式です。たとえば ``hex(25)`` は ``"0x19"`` になります。

    Arguments:
        x (int): 変換する値。

    Returns:
        入力の16進数表現の文字列。
    """


def id(object: Any) -> _int:
    """
    id(object) -> int

    オブジェクトの *識別子* を取得します。これは、そのオブジェクトの
    存続期間中、一意かつ不変であることが保証された整数です。

    Arguments:
        object: 識別子を取得するオブジェクト。

    Returns:
        識別子。
    """


@overload
def input() -> _str: ...


@overload
def input(prompt: _str) -> _str: ...


def input(*args) -> _str:
    """input() -> str
    input(prompt) -> str

    ターミナルウィンドウでユーザーからの入力を取得します。ユーザーが
    :kbd:`Enter` を押すまで待機します。

    Arguments:
        prompt (str): 指定した場合、最初にターミナルウィンドウに表示されます。
            ユーザーに何を入力すべきかを質問するために使用できます。

    Returns:
        ユーザーが :kbd:`Enter` を押すまでに入力したすべての内容。
    """


class int:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, x: _str) -> None: ...

    @overload
    def __init__(self, x: _str, base: _int) -> None: ...

    @overload
    def __init__(self, x: _int | SupportsInt) -> None: ...

    def __init__(self, *args) -> None:
        """int(x=0)

        整数を作成します。

        Arguments:
            x (int or float or str): 変換するオブジェクト。
        """

    def to_bytes(self, length: _int, byteorder: Literal["little", "big"]) -> _bytes:
        """
        to_bytes(length, byteorder) -> bytes

        整数の :class:`bytes` 表現を取得します。

        Arguments:
            length (int): 使用するバイト数。
            byteorder (str): 最上位バイトを先頭にする場合は ``"big"`` を
                選択します。最下位バイトを先頭にする場合は ``"little"`` を
                選択します。

        Returns:
            整数を表すバイトシーケンス。
        """

    @_classmethod
    def from_bytes(cls, _bytes: _bytes, byteorder: Literal["little", "big"]) -> _int:
        """from_bytes(bytes, byteorder) -> int

        バイトシーケンスを、それが表す数値に変換します。

        Arguments:
            bytes (bytes): 変換するバイト列。
            byteorder (str): 最上位バイトが先頭の要素である場合は ``"big"``
                を選択します。最下位バイトが先頭の要素である場合は
                ``"little"`` を選択します。

        Returns:
            バイト列が表す数値。
        """


def isinstance(object: Any, classinfo: _type | _tuple[_type]) -> _bool:
    """
    isinstance(object, classinfo) -> bool

    オブジェクトがあるクラスのインスタンスかどうかを確認します。

    Arguments:
        object: 型を確認するオブジェクト。
        classinfo (type or tuple): クラス情報。

    Returns:
        ``object`` 引数が ``classinfo`` 引数のインスタンス、または
        そのサブクラスのインスタンスである場合は ``True`` 。
    """


def issubclass(cls: _type, classinfo: _type | _tuple[_type]) -> _bool:
    """
    issubclass(cls, classinfo) -> bool

    あるクラスが別のクラスのサブクラスかどうかを確認します。

    Arguments:
        cls: クラス型。
        classinfo (type or tuple): クラス情報。

    Returns:
        ``cls`` が ``classinfo`` のサブクラスである場合は ``True`` 。
    """


def iter(object: Iterable | Sequence) -> Iterator:
    """
    iter(object) -> Iterator

    利用可能な場合は、オブジェクトのイテレーターを取得します。

    Arguments:
        object: イテレーターを取得するオブジェクト。

    Returns:
        イテレーター。
    """


def len(s: Sequence) -> _int:
    """
    len(s) -> int

    オブジェクトの長さ（要素数）を取得します。

    Arguments:
        s (Sequence): 長さを取得するシーケンス。

    Returns:
        長さ。
    """


class list:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, iterable: Iterable) -> None: ...

    def __init__(self, *args) -> None:
        """
        list(\u200b)
        list(iterable)

        新しいリストを作成します。引数が与えられない場合は、空の
        ``list`` オブジェクトを作成します。

        リストは *ミュータブル* であり、作成後に内容を変更することが
        *できます* 。

        Arguments:
            iterable (iter): リストの構築元となるイテラブル。
        """


def locals() -> _dict:
    """
    locals() -> dict

    現在のローカルシンボルテーブルを表す辞書を取得します。

    Returns:
        ローカルの辞書。
    """


def map(function: Callable, iterable: Iterable, *args: Any) -> Iterator:
    """
    map(function, iterable) -> Iterator
    map(function, iterable1, iterable2...) -> Iterator

    指定したイテラブルの各要素に指定した関数を適用し、その結果を生成する
    新しいイテレーターを作成します。

    Arguments:
        function (callable): イテラブルの1つの要素に対して結果を計算する
            関数。この関数への引数の数は、指定したイテラブルの数と一致する
            必要があります。
        iterable (iter): データを取り出す1つ以上のソースイテラブル。
            複数のイテラブルを指定した場合、最も短いイテラブルが尽きると
            イテレーターは停止します。

    Returns:
        新しいマップされたイテレーター。
    """


@overload
def max(iterable: Iterable) -> Any: ...


@overload
def max(arg1: Any, arg2: Any, *args: Any) -> Any: ...


def max(*args):
    """
    max(iterable) -> Any
    max(arg1, arg2, ....) -> Any

    最大値を持つオブジェクトを取得します。

    引数には単一のイテラブルまたは任意の数のオブジェクトを指定できます。

    Returns:
        最大値を持つオブジェクト。
    """


@overload
def min(iterable: Iterable) -> Any: ...


@overload
def min(arg1: Any, arg2: Any, *args: Any) -> Any: ...


def min(*args):
    """
    min(iterable) -> Any
    min(arg1, arg2, ....) -> Any

    最小値を持つオブジェクトを取得します。

    引数には単一のイテラブルまたは任意の数のオブジェクトを指定できます。

    Returns:
        最小値を持つオブジェクト。
    """


def next(iterator: Iterator) -> Any:
    """
    next(iterator) -> Any

    イテレーターの ``__next__()`` メソッドを呼び出して、次の要素を
    取得します。

    Arguments:
        iterator (iter): 次の値を取り出す、初期化されたジェネレーター
            オブジェクト。

    Returns:
        ジェネレーターからの次の値。
    """


class object:
    def __init__(self) -> None:
        """
        機能を持たない新しいオブジェクトを作成します。
        """


def oct(x: _int) -> _str:
    """oct(x) -> str

    整数を8進数表現に変換します。結果は ``0o`` で始まる文字列で、
    有効なPython式です。たとえば ``oct(25)`` は ``"0o31"`` になります。

    Arguments:
        x (int): 変換する値。

    Returns:
        入力の8進数表現の文字列。
    """


# .. function:: open()


def ord(c: _str) -> _int:
    """ord(c) -> int

    1つのUnicode文字からなる文字列を対応する数値に変換します。
    これは :meth:`chr` の逆関数です。

    Arguments:
        c (str): 変換する文字。

    Returns:
        文字を表す数値（0--255）。
    """


def pow(base: _int | _float, exp: _int | _float) -> _int | _float:
    """
    pow(base, exp) -> Number

    底を指定した指数で累乗します。

    これは ``base ** exp`` を行うのと同じです。

    Arguments:
        base (Number): 底。
        exp (Number): 指数。

    Returns:
        結果。
    """


@overload
def print(*objects): ...


@overload
def print(
    *objects, sep: _str = " ", end: _str = "\n", file: uio.FileIO = usys.stdin
): ...


def print(*args):
    """print(*objects, sep=" ", end="\\n", file=usys.stdin)

    ターミナルウィンドウにテキストまたはその他のオブジェクトを表示します。

    Arguments:
        objects: 表示する0個以上のオブジェクト。

    Keyword Arguments:
        sep (str): オブジェクトが複数ある場合に、オブジェクトの間に表示されます。
        end (str): 最後のオブジェクトの後に表示されます。
        file (FileIO): デフォルトでは、結果はターミナルウィンドウに表示されます。
              ファイルがサポートされている場合、この引数でファイルに
              出力することができます。
    """


class range:
    @overload
    def __init__(self, stop: _int) -> None: ...

    @overload
    def __init__(self, start: _int, stop: _int) -> None: ...

    @overload
    def __init__(self, start: _int, stop: _int, step: _int) -> None: ...

    def __init__(self, *args) -> None:
        """
        range(stop)
        range(start, stop)
        range(start, stop, step)

        ``start`` から ``stop`` まで、 ``step`` 刻みの値を生成する
        ジェネレーターを作成します。

        Arguments:
            start (int): 開始値。引数が1つだけの場合はデフォルトで ``0`` 。
            stop (int): 終端。この値は *含まれません* 。
            step (int): 値の間の刻み幅。引数が1つまたは2つの場合は
                デフォルトで ``1`` 。
        """


def repr(x: Any) -> _str:
    """repr(object) -> str

    オブジェクトを表す文字列を取得します。

    Arguments:
        x (object): 変換するオブジェクト。

    Returns:
        オブジェクトの ``__repr__`` メソッドで実装された文字列表現。
    """


def reversed(seq: Sequence) -> Iterator:
    """
    reversed(seq) -> Iterator

    サポートされている場合、シーケンスの値を逆順に生成するイテレーターを
    取得します。

    Arguments:
        seq: 値を取り出すシーケンス。

    Returns:
        最後の値から始めて逆順に値を生成するイテレーター。
    """


@overload
def round(number: _float) -> _int: ...


@overload
def round(number: _float, ndigits: _int) -> _float: ...


def round(*args):
    """
    round(number) -> int
    round(number, ndigits) -> float

    数値を小数点以下の指定した桁数に丸めます。

    ``ndigits`` が省略または ``None`` の場合は、最も近い整数を返します。

    小数点以下1桁以上で丸めても、末尾のゼロが常に切り捨てられるとは
    限りません。数値をきれいに表示するには、代わりに文字列を
    フォーマットしてください::

        # print two decimal places
        print('my number: %.2f' % number)
        print('my number: {:.2f}'.format(number))
        print(f'my number: {number:.2f}')

    Arguments:
        number (float): 丸める数値。
        ndigits (int): 小数点以下に残す桁数。
    """


class set:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, iterable: Iterable[Hashable]) -> None: ...

    def __init__(self, *args) -> None:
        """
        set()
        set(iterable)

        新しいセットを作成します。

        引数がない場合は新しい空のセットを作成し、それ以外の場合は
        *iterable* の一意の要素を含むセットを作成します。

        セットはセットリテラルを使って作成することもできます::

            my_set = {1, 2, 3}

        セットの要素はハッシュ可能でなければなりません。
        :class:`list` のようないくつかの型はハッシュ可能ではありません。

        Args:
            iterable: ハッシュ可能なオブジェクトのイテラブル。
        """

    def copy(self) -> Self:
        """
        copy() -> set

        セットのシャローコピーを返します。

        Returns:
            新しいセット。
        """

    def difference(self, *others: set) -> Self:
        """
        difference(other1, other2, ...) -> set

        他のどのセットにも含まれない要素を持つ新しいセットを返します。

        差分は ``-`` 演算子を使って計算することもできます::

            diff = s - other

        Args:
            others: 1つ以上の他のセット。

        Returns:
            新しいセット。
        """

    def intersection(self, *others: set) -> Self:
        """
        intersection(other1, other2, ...) -> set

        このセットと他のすべてのセットに共通する要素を持つ新しいセットを
        返します。

        積集合は ``&`` 演算子を使って計算することもできます::

            intersect = s & other

        Args:
            others: 1つ以上の他のセット。

        Returns:
            新しいセット。
        """

    def isdisjoint(self, other: set) -> bool:
        """
        isdisjoint(other) -> bool

        このセットと *other* に共通する要素がないかを確認します。

        Args:
            other: 別のセット。

        Returns:
            このセットが *other* と共通する要素を持たない場合は ``True`` 、
            それ以外は ``False`` 。
        """

    def issubset(self, other: set) -> bool:
        """
        issubset(other) -> bool

        このセットが *other* の部分集合かどうかを確認します。

        この確認は ``<=`` 演算子を使って行うこともできます::

            if s <= other:
                # s is subset of other
                ...

        Args:
            other: 別のセット。

        Returns:
            このセットが *other* の部分集合である場合は ``True`` 、
            それ以外は ``False`` 。
        """

    def issuperset(self, other: set) -> bool:
        """
        issuperset(other) -> bool

        このセットが *other* の上位集合かどうかを確認します。

        この確認は ``>=`` 演算子を使って行うこともできます::

            if s >= other:
                # s is superset of other
                ...

        Args:
            other: 別のセット。

        Returns:
            このセットが *other* の上位集合である場合は ``True`` 、
            それ以外は ``False`` 。
        """

    def symmetric_difference(self, other: set) -> Self:
        """
        symmetric_difference(other) -> bool

        どちらか一方のセットにのみ含まれる要素を持つ新しいセットを返します。

        対称差は ``^`` 演算子を使って計算することもできます::

            diff = s ^ other

        Args:
            other: 別のセット。

        Returns:
            新しいセット。
        """

    def union(self, *others: set) -> Self:
        """
        union(other1, other2, ...) -> set

        このセットと他のすべてのセットの要素を含む新しいセットを返します。

        和集合は ``|`` 演算子を使って計算することもできます::

            u = s | other

        Args:
            others: 1つ以上の他のセット。

        Returns:
            新しいセット。
        """

    def __contains__(self, item: Hashable) -> bool: ...

    def __len__(self) -> int: ...

    def __bool__(self) -> bool: ...

    def __gt__(self, other: set) -> bool: ...

    def __lt__(self, other: set) -> bool: ...

    def __ge__(self, other: set) -> bool: ...

    def __le__(self, other: set) -> bool: ...

    def __eq__(self, other: set) -> bool: ...

    def __ne__(self, other: set) -> bool: ...

    def __sub__(self, other: set) -> Self: ...

    def __and__(self, other: set) -> Self: ...

    def __or__(self, other: set) -> Self: ...

    def __xor__(self, other: set) -> Self: ...


def setattr(object: Any, name: _str, value: Any) -> None:
    """
    setattr(object, name, value)

    オブジェクトが許可する場合、属性に値を割り当てます。

    これは :meth:`getattr` に対応するものです。

    Arguments:
        object: 属性を保存するオブジェクト。
        name (str): 属性の名前。
        value: 保存する値。
    """


class slice:
    @overload
    def __init__(self, stop: _int) -> None: ...

    @overload
    def __init__(self, start: _int, stop: _int) -> None: ...

    @overload
    def __init__(self, start: _int, stop: _int, step: _int) -> None: ...

    def __init__(self, *args) -> None:
        """
        slice(\u200b)

        このクラスのインスタンスの作成はサポートされていません。

        代わりにインデックス構文を使用してください。
        例： ``a[start:stop:step]`` または ``a[start:stop, i]`` 。
        """


def sorted(iterable: Iterable, key=None, reverse=False) -> builtins.list:
    """
    オブジェクトをソートします。

    Arguments:
        iterable (iter): ソートするオブジェクト。有限個のオブジェクトを
            生成するジェネレーターも指定できます。
        key (callable): オブジェクトを数値にマッピングする関数
            ``def(item) -> int`` 。ソートされた要素の順序を決定するために
            使用されます。
        reverse (bool): 最大値を先頭にして逆順にソートするかどうか。


    Returns:
        ソートされた要素を持つ新しいリスト。
    """


def staticmethod(method: _callable) -> _callable:
    """
    メソッドを静的メソッドに変換します。
    """


class str:
    @overload
    def __init__(self, object: Any = "") -> None: ...

    @overload
    def __init__(
        self, object: _bytes = b"", encoding: _str = "utf-8", errors: _str = "strict"
    ) -> None: ...

    def __init__(self) -> None:
        """
        str(\u200b)
        str(object)
        str(object, encoding)

        オブジェクトの文字列表現を取得します。

        引数が与えられない場合は、空の ``str`` オブジェクトを作成します。

        Arguments:
            object: この引数のみが与えられた場合、オブジェクトの文字列表現を
              返します。
            encoding (str): 最初の引数が ``bytearray`` または ``bytes``
              オブジェクトで、encoding引数が ``"utf-8"`` の場合、バイトデータを
              デコードして文字列表現を取得します。
        """


@overload
def sum(iterable: Iterable) -> _int: ...


@overload
def sum(iterable: Iterable, start: _int) -> _int: ...


def sum(*args):
    """
    sum(iterable) -> Number
    sum(iterable, start) -> Number

    イテラブルの要素と ``start`` の値を合計します。

    Arguments:
        iterable (iter): 合計する値。最初の値から始まります。
        start (Number): 合計に加算される値。

    Returns:
        合計。
    """


@overload
def super() -> _type: ...


@overload
def super(type: _type) -> _type: ...


@overload
def super(type: _type, object_or_type: Any) -> _type: ...


def super(*args):
    """
    super() -> type
    super(type) -> type
    super(type, object_or_type) -> type

    指定した型の親クラスまたは兄弟クラスにメソッド呼び出しを委譲する
    オブジェクトを取得します。

    Returns:
        対応する `super()` オブジェクト。
    """


class tuple:
    @overload
    def __init__(self): ...

    @overload
    def __init__(self, iterable: Iterable): ...

    def __init__(self, *args) -> None:
        """
        tuple(\u200b)
        tuple(iterable)

        新しいタプルを作成します。引数が与えられない場合は、空の
        ``tuple`` オブジェクトを作成します。

        タプルは *イミュータブル* であり、作成後に内容を変更することは
        *できません* 。

        Arguments:
            iterable (iter): タプルの構築元となるイテラブル。
        """


class type:
    def __init__(self, object: Any) -> None:
        """type(object)

        オブジェクトの型を取得します。これは、オブジェクトが特定のクラスの
        インスタンスかどうかを確認するために使用できます。

        Arguments:
            object: 型を確認するオブジェクト。
        """


def zip(*iterables: Iterable) -> Iterable[builtins.tuple]:
    """
    zip(iter_a, iter_b, ...) -> Iterable[tuple]

    タプルのイテレーターを返します。 *i* 番目のタプルには、引数の各
    シーケンスまたはイテラブルの *i* 番目の要素が含まれます。
    最も短い入力イテラブルが尽きるとイテレーターは停止します。

    イテラブルを1つだけ指定した場合は、1要素のタプルのイテレーターを返します。
    引数を指定しない場合は、空のイテレーターを返します。

    この機能は以下と同等です::

        def zip(*iterables):
            sentinel = object()
            iterators = [iter(it) for it in iterables]
            while iterators:
                result = []
                for it in iterators:
                    elem = next(it, sentinel)
                    if elem is sentinel:
                        return
                    result.append(elem)
                yield tuple(result)

    Arguments:
        iter_a (iter): 最初のイテラブル。生成される各タプルの最初の値を
            提供します。
        iter_b (iter): 2番目のイテラブル。生成される各タプルの2番目の値を
            提供します。以下同様です。

    Returns:
        個々のイテラブルの値を含むタプルを生成する新しいイテレーター。
    """


# base exceptions


class BaseException:
    """
    すべての組み込み例外の基底クラス。

    ユーザー定義クラスから直接継承することは意図されていません
    （その場合は :class:`Exception` を使用してください）。
    """

    args: builtins.tuple
    """
    例外コンストラクターに渡された引数のタプル。
    """


class Exception(BaseException):
    """
    すべての組み込み例外はこのクラスから派生しています。

    すべてのユーザー定義例外もこのクラスから派生させる必要があります。
    """


class ArithmeticError(Exception):
    """
    さまざまな算術エラーに対して送出される組み込み例外の基底クラス。
    """


class LookupError(Exception):
    """
    マッピングまたはシーケンスで使用するキーまたはインデックスが
    無効な場合に送出される例外の基底クラス。
    """


# concrete exceptions


class AssertionError(Exception):
    """
    assert文が失敗したときに送出されます。
    """


class AttributeError(Exception):
    """
    属性の参照または代入が失敗したときに送出されます。
    """


class EOFError(Exception):
    """
    :meth:`input` 関数がデータを読み取る前にファイル終端（EOF）に
    達したときに送出されます。
    """


class GeneratorExit(BaseException):
    """
    ジェネレーターまたはコルーチンが閉じられたときに送出されます。
    """


class ImportError(Exception):
    """
    ``import`` 文がモジュールを読み込めなかったときに送出されます。
    """


class IndentationError(SyntaxError):
    """
    不正なインデントに関連する構文エラーの基底クラス。
    """


class IndexError(LookupError):
    """
    シーケンスの添字が範囲外のときに送出されます。
    """


class KeyError(LookupError):
    """
    マッピング（辞書）のキーが既存のキーの中に見つからないときに送出されます。
    """


class KeyboardInterrupt(BaseException):
    """
    ユーザーが割り込みキー（通常は :kbd:`Ctrl` :kbd:`C` ）を押したときに
    送出されます。
    """


class MemoryError(Exception):
    """
    操作がメモリ不足になったときに送出されます。
    """


class NameError(Exception):
    """
    ローカル名またはグローバル名が見つからないときに送出されます。
    """


class NotImplementedError(RuntimeError):
    """
    ユーザー定義の基底クラスでは、派生クラスにメソッドのオーバーライドを
    要求する抽象メソッド、または実際の実装がまだ追加される必要があることを
    示す開発中のクラスで、この例外を送出する必要があります。
    """


class OSError(Exception):
    """
    この例外は、ハブ上で動作するオペレーティングシステムである
    ファームウェアによって送出されます。
    :ref:`例 <device_detection>` として、ポートAにモーターが
    接続されていないときに ``Motor(Port.A)`` を呼び出すと
    ``OSError`` が送出されます。
    """

    errno: _int
    """
    発生した ``OSError`` の種類を指定します。種類は :mod:`uerrno`
    モジュールに列挙されています。
    """


class OverflowError(ArithmeticError):
    """
    算術演算の結果が表現できないほど大きいときに送出されます。
    """


class RuntimeError(Exception):
    """
    他のどのカテゴリーにも当てはまらないエラーが検出されたときに送出されます。

    関連する値は、何が具体的に問題だったかを示す文字列です。
    """


class StopIteration(Exception):
    """
    組み込み関数 :meth:`next` とイテレーターの ``__next__()`` メソッドが、
    イテレーターがこれ以上要素を生成しないことを示すために送出されます。

    ジェネレーター関数は、これを直接送出する代わりにreturnすべきです。
    """


class SyntaxError(Exception):
    """
    パーサーが構文エラーに遭遇したときに送出されます。
    """


class SystemExit(BaseException):
    """
    ハブまたはPybricks Codeアプリの停止ボタンを押したときに送出されます。
    """


class TypeError(Exception):
    """
    操作または関数が不適切な型のオブジェクトに適用されたときに送出されます。
    """


class ValueError(Exception):
    """
    操作または関数が、正しい型だが不適切な値の引数を受け取ったときに
    送出されます。これは、 :class:`IndexError` のようなより正確な例外で
    状況が説明できない場合に使用されます。
    """


class ZeroDivisionError(ArithmeticError):
    """
    除算または剰余演算の第2引数が0のときに送出されます。
    """
