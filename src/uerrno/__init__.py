# SPDX-License-Identifier: MIT
# Copyright (c) 2021 The Pybricks Authors
#
# Portions of documentation copied from:
# https://raw.githubusercontent.com/micropython/micropython/1e6d18c915ccea0b6a19ffec9710d33dd7e5f866/docs/library/uerrno.rst
# Copyright (c) 2014-2021, Damien P. George, Paul Sokolovsky, and contributors

"""
`OSError` 例外のシンボリックなエラーコードへのアクセスを提供します。
"""

EAGAIN: int
"""
操作が完了していないため、まもなく再試行する必要があります。
"""

EBUSY: int
"""
デバイスまたはリソースがビジー状態のため、現在使用できません。
"""

ECANCELED: int
"""
操作がキャンセルされました。
"""

EINVAL: int
"""
無効な引数が指定されました。通常は代わりに ``ValueError`` が使用されます。
"""

EIO: int
"""
不明なエラーが発生しました。
"""

ENODEV: int
"""
デバイスが見つかりません。たとえば、センサーやモーターが正しいポートに接続されていない場合です。
"""

EOPNOTSUPP: int
"""
このハブまたは接続されたデバイスでは、この操作はサポートされていません。
"""

EPERM: int
"""
現在の状態ではこの操作を実行できません。
"""

ETIMEDOUT: int
"""
操作がタイムアウトしました。
"""

# TODO: ev3dev has additional constants
# https://github.com/pybricks/pybricks-micropython/blob/11f19bc9c24fde66aa8ad42233a345e6683f5beb/bricks/ev3dev/mpconfigport.h#L156-L203

errorcode: dict[int, str]
"""
数値のエラーコードをシンボリックなエラーコードの文字列に対応付ける辞書。
"""
