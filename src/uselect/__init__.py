# SPDX-License-Identifier: MIT
# Copyright (c) 2021 The Pybricks Authors
#
# Portions of documentation copied from:
# https://raw.githubusercontent.com/micropython/micropython/1e6d18c915ccea0b6a19ffec9710d33dd7e5f866/docs/library/uselect.rst
# Copyright (c) 2014-2021, Damien P. George, Paul Sokolovsky, and contributors

"""
このモジュールは、複数のストリームでイベントを効率的に待機する関数を提供します。
"""

from __future__ import annotations

from typing import IO, TYPE_CHECKING, overload

if TYPE_CHECKING:
    from collections.abc import Iterator

POLLIN: int
"""
読み取り可能なデータがあります。
"""

POLLOUT: int
"""
さらにデータを書き込むことができます。
"""

POLLERR: int
"""
関連するストリームでエラー状態が発生しました。明示的に処理する必要があります。
そうしないと、それ以降の :meth:`poll` の呼び出しがすぐに返る場合があります。
"""

POLLHUP: int
"""
関連するストリームでハングアップが発生しました。明示的に処理する必要があります。
そうしないと、それ以降の :meth:`poll` の呼び出しがすぐに返る場合があります。
"""


class Poll:
    def register(self, object: IO, eventmask: int) -> None:
        """
        register(object, eventmask=POLLOUT | POLLOUT)

        ポーリング対象のストリームオブジェクトを登録します。ストリーム
        オブジェクトはイベントが監視されるようになります。イベントが発生
        すると、それが :meth:`poll` の戻り値の一部になります。

        同じストリームオブジェクトに対してこのメソッドが再度呼び出された
        場合、オブジェクトは再登録されませんが、``eventmask`` フラグは
        :meth:`modify()` を呼び出したかのように更新されます。

        Arguments:
            object (FileIO): ポーリングに登録するストリーム。
            eventmask (int): 使用するイベント。 ``POLLIN``、``POLLOUT``、
                またはそれらの論理和 ``POLLIN | POLLOUT`` を指定します。
        """

    def unregister(self, object: IO) -> None:
        """
        unregister(poll)

        オブジェクトをポーリングから登録解除します。

        Arguments:
            object (FileIO): ポーリングから登録解除するストリーム。
        """

    def modify(self, obj: IO, eventmask: int) -> None:
        """
        modify(object, eventmask)

        ストリームオブジェクトのイベントマスクを変更します。

        Arguments:
            object (FileIO): ポーリングに登録するストリーム。
            eventmask (int): 使用するイベント。

        Raises:
            ``OSError``: オブジェクトが登録されていない場合。エラーは ``ENOENT`` です。
        """

    @overload
    def poll(self) -> list[tuple[IO, int]]: ...

    @overload
    def poll(self, timeout: int) -> list[tuple[IO, int]]: ...

    def poll(self, timeout: int = -1, /) -> list[tuple[IO, int]]:
        """
        poll(timeout=-1) -> list[tuple[FileIO, int]]

        登録されたオブジェクトの少なくとも1つが、処理可能な新しいイベント
        または例外状態になるまで待機します。

        Arguments:
            timeout (int): タイムアウト（ミリ秒）。 ``0`` を選択するとすぐに
                返り、``-1`` を選択すると無制限に待機します。

        Returns:
            タプルのリスト。イベントのあるオブジェクトごとに1つの
            (``object``, ``eventmask``, ...) タプルがあり、処理すべき
            イベントがない場合はタプルはありません。 ``eventmask`` の値は、
            何が起こったかを示すポーリングフラグの組み合わせです。これには
            登録されていなくても ``POLLERR`` と ``POLLHUP`` が含まれる
            場合があります。
        """

    @overload
    def ipoll(self) -> Iterator[tuple[IO, int]]: ...

    @overload
    def ipoll(self, timeout: int) -> Iterator[tuple[IO, int]]: ...

    @overload
    def ipoll(self, timeout: int, flags: int) -> Iterator[tuple[IO, int]]: ...

    def ipoll(self, timeout: int = -1, flags: int = 0, /) -> Iterator[tuple[IO, int]]:
        """
        ipoll(timeout=-1, flags=1) -> Iterator[tuple[FileIO, int]]

        まず、:meth:`poll` と同様に、登録されたオブジェクトの少なくとも
        1つが、処理可能な新しいイベントまたは例外状態になるまで待機します。

        ただし、リストの代わりに、このメソッドは効率向上のために
        イテレーターを返します。イテレーターは一度に1つの
        (``object``, ``eventmask``, ...) タプルを生成し、次の値を生成する
        ときにそれを上書きします。後で値が必要な場合は、明示的にコピー
        してください。

        Arguments:
            timeout (int): タイムアウト（ミリ秒）。 ``0`` を選択するとすぐに
                返り、``-1`` を選択すると無制限に待機します。
            flags (int): ``1`` に設定すると、イベントにワンショット動作が
                適用されます。これは、イベントが発生したストリームの
                イベントマスクが ``poll.modify(obj, 0)`` を使用して自動的に
                リセットされることを意味します。このように、:meth:`modify`
                で新しいマスクが設定されるまで、そのようなストリームの
                新しいイベントは処理されません。これは非同期 I/O
                スケジューラーに役立ちます。
        """


def poll() -> Poll:
    """
    :class:`Poll` クラスのインスタンスを作成します。

    Returns:
        :class:`Poll` のインスタンス。
    """


# Hide type-only names from jedi completions in the module namespace.
if TYPE_CHECKING:
    del Iterator
