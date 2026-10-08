# SPDX-License-Identifier: MIT
# Copyright (c) 2022 The Pybricks Authors
#
# Portions of documentation copied from:
# https://raw.githubusercontent.com/micropython/micropython/1e6d18c915ccea0b6a19ffec9710d33dd7e5f866/docs/library/uio.rst
# Copyright (c) 2014-2021, Damien P. George, Paul Sokolovsky, and contributors

"""
このモジュールには、ファイルのように振る舞う ``stream`` オブジェクトが含まれています。
"""

# TODO: open() is not implemented on Powered Up hubs

from typing import overload

# TODO: MicroPython streams implement '__enter__', '__exit__', 'close', 'read',
# 'readinto', 'readline', 'write', 'flush', 'seek', 'tell'
# and are iterable


class BytesIO:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, data: bytes | bytearray) -> None: ...

    @overload
    def __init__(self, alloc_size: int) -> None: ...

    def __init__(self, *args) -> None:
        """
        BytesIO(\u200b)
        BytesIO(data)
        BytesIO(alloc_size)

        メモリ内バイトバッファを使用するバイナリストリームです。

        Arguments:
            data (bytes or bytearray): 初期データを含むオプションの
                bytes-like オブジェクト。
            alloc_size (int): 事前に割り当てるバイト数（オプション）。この
                パラメーターはMicroPython固有です。エンドユーザーコードで
                使用することは推奨されません。
        """

    def getvalue(self) -> bytes:
        """
        getvalue() -> bytes

        基になるバッファの内容を取得します。
        """


class StringIO:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, string: str) -> None: ...

    @overload
    def __init__(self, alloc_size: int) -> None: ...

    def __init__(self, *args) -> None:
        """
        StringIO(\u200b)
        StringIO(string)
        StringIO(alloc_size)

        メモリ内文字列バッファを使用するストリームです。

        Arguments:
            string (str): 初期データを持つオプションの文字列。
            alloc_size (int): 事前に割り当てるバイト数（オプション）。この
                パラメーターはMicroPython固有です。エンドユーザーコードで
                使用することは推奨されません。
        """

    def getvalue(self) -> str:
        """
        getvalue() -> str

        基になるバッファの内容を取得します。
        """


class FileIO:
    """
    この型は ``open(name, 'rb')`` でバイナリモードで開かれたファイルを表します。
    このクラスは直接インスタンス化しないでください。
    """
