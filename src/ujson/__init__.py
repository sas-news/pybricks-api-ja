# SPDX-License-Identifier: MIT
# Copyright (c) 2022 The Pybricks Authors
#
# Documentation adapted from:
# https://raw.githubusercontent.com/micropython/micropython/master/docs/library/json.rst
# Copyright (c) 2014-2021, Damien P. George, Paul Sokolovsky, and contributors

"""
PythonオブジェクトとJSONデータ形式を相互に変換します。
"""

from typing import IO, Any


def dump(object: Any, stream: IO, separators: tuple[str, str] = (", ", ": ")):
    """
    dump(object, stream, separators=(", ", ": "))

    オブジェクトをJSON文字列にシリアライズし、ストリームに書き込みます。

    Arguments:
        obj: シリアライズするオブジェクト。
        stream: 出力を書き込むストリーム。
        separators (tuple): 要素の区切り方を指定する
            ``(item_separator, key_separator)`` タプル。
    """


def dumps(object: Any, separators: tuple[str, str] = (", ", ": ")) -> str:
    """
    dumps(object, separators=(", ", ": "))

    オブジェクトをJSONにシリアライズし、文字列として返します。

    Arguments:
        obj: シリアライズするオブジェクト。
        separators (tuple): 要素の区切り方を指定する
            ``(item_separator, key_separator)`` タプル。

    Return:
        JSON文字列。
    """


def load(stream: IO) -> Any:
    """
    load(stream)

    ストリームを解析し、JSONデータをMicroPythonオブジェクトに
    デシリアライズ（復元）します。

    ファイル末尾に達するまで解析が続きます。ストリーム内のデータが
    正しく構成されていない場合は ``ValueError`` が発生します。

    Arguments:
        stream: JSON文字列の読み込み元ストリーム。

    Returns:
        デシリアライズされたMicroPythonオブジェクト。
    """


def loads(string) -> Any:
    """
    loads(string)

    文字列を解析し、JSONデータをMicroPythonオブジェクトに
    デシリアライズ（復元）します。

    文字列が正しく構成されていない場合は ``ValueError`` が発生します。

    Arguments:
        string (str): デコードするJSON文字列。

    Returns:
        デシリアライズされたMicroPythonオブジェクト。
    """
