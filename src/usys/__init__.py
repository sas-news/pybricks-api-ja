# SPDX-License-Identifier: MIT
# Copyright (c) 2021 The Pybricks Authors
#
# Portions of documentation copied from:
# https://raw.githubusercontent.com/micropython/micropython/1e6d18c915ccea0b6a19ffec9710d33dd7e5f866/docs/library/sys.rst
# Copyright (c) 2014-2021, Damien P. George, Paul Sokolovsky, and contributors

"""
標準Pythonの ``sys`` モジュールのサブセットを提供します。
"""

from uio import FileIO as _FileIO

stdin: _FileIO = _FileIO()
"""
接続されたターミナルがあれば、そこからの入力を受け取る
ストリームオブジェクト（:class:`uio.FileIO`）です。

``stdin`` 経由でバイナリデータを渡すときに ``KeyboardInterrupt`` を
無効化する :func:`kbd_intr <micropython.kbd_intr>` も参照してください。
"""

stdout: _FileIO = _FileIO()
"""
接続されたターミナルがあれば、そこへ出力を送る
ストリームオブジェクト（:class:`uio.FileIO`）です。
"""

stderr: _FileIO = _FileIO()
"""
:data:`stdout` のエイリアス。
"""

implementation: tuple[str, tuple[int, int, int], str, int] = (
    "micropython",
    (1, 19, 1),
    "NAME Hub with PROCESSOR",
    6,
)
"""
MicroPythonのバージョンタプル。フォーマットと例は下記を参照してください。
"""

version: str = "3.4.0; Pybricks MicroPython v3.2.0b5 on 2022-11-11"
"""
Python互換バージョン、Pybricksバージョン、ビルド日時。
フォーマットと例は下記を参照してください。
"""

version_info: tuple[int, int, int] = (3, 4, 0)
"""Python互換バージョン。フォーマットと例は下記を参照してください。"""
