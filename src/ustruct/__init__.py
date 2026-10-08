# SPDX-License-Identifier: MIT
# Copyright (c) 2021 The Pybricks Authors
#
# Portions of documentation copied from:
# https://raw.githubusercontent.com/micropython/micropython/1e6d18c915ccea0b6a19ffec9710d33dd7e5f866/docs/library/ustruct.rst
# Copyright (c) 2014-2021, Damien P. George, Paul Sokolovsky, and contributors

"""
Pythonの値とC言語風のデータ構造体を相互に変換する関数を提供します。
"""


def calcsize(format: str) -> int:
    """
    フォーマット文字列に対応するデータサイズを取得します。

    Arguments:
        format (str): データフォーマット文字列。

    Returns:
        このフォーマットを表現するのに必要なバイト数。
    """


def pack(format: str, *values) -> bytes:
    """
    pack(format, value1, value2, ...)

    指定したフォーマットで値をパックします。

    Arguments:
        format (str): データフォーマット文字列。

    Returns:
        バイト列にエンコードされたデータ。
    """


def pack_into(format: str, buffer: bytearray, offset: int, *values) -> bytes:
    """
    pack_into(format, buffer, offset, value1, value2, ...)

    指定したフォーマットで値をエンコードし、指定したバッファに書き込みます。

    Arguments:
        format (str): データフォーマット文字列。
        buffer (bytearray): エンコードしたデータの格納先バッファ。
        offset (int): バッファ先頭からのオフセット。負の値を指定すると
            バッファ末尾から数えます。
    """


def unpack(format: str, data: bytes | bytearray) -> tuple:
    """
    unpack(format, data) -> tuple

    指定したフォーマットでバイナリデータをデコードします。

    Arguments:
        format (str): データフォーマット文字列。
        data (bytes or bytearray): アンパックするデータ。

    Returns:
        値のタプルとしてデコードされたデータ。
    """


def unpack_from(format: str, data: bytes | bytearray, offset: int) -> tuple:
    """
    unpack_from(format, data, offset) -> tuple

    指定したフォーマットでバッファ内のバイナリデータをデコードします。

    Arguments:
        format (str): データフォーマット文字列。
        data (bytes or bytearray): アンパックするデータバッファ。
        offset (int): データ先頭からのオフセット。負の値を指定すると
            データ末尾から数えます。

    Returns:
        値のタプルとしてデコードされたデータ。
    """
