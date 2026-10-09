# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2020 The Pybricks Authors

"""
EV3ブロック間でメッセージをやり取りするためのクラス。
"""


class Mailbox:
    def __init__(self, name, connection, encode=None, decode=None):
        """データを保持するメールボックスを表すオブジェクトです。

        他のEV3ブロックから配信されたデータを読み取ったり、同じメールボックスを
        持つ他のブロックへデータを送信したりできます。

        既定では、メールボックスはバイト列だけを読み書きします。他のデータを
        送るには、Pythonオブジェクトをバイト列に変換する ``encode`` 関数と、
        バイト列をPythonオブジェクトに戻す ``decode`` 関数を指定します。

        Arguments:
            name (str):
                このメールボックスの名前。
            connection:
                :class:`BluetoothMailboxClient` などの接続オブジェクト。
            encode (callable):
                Pythonオブジェクトをバイト列にエンコードする関数。
            decode (callable):
                バイト列から新しいPythonオブジェクトを作成する関数。
        """

    def read(self):
        """メールボックスの現在の値を取得します。

        Returns:
            現在の値。メールボックスが空の場合は ``None`` 。
        """
        return ''

    def send(self, value, brick=None):
        """接続されたデバイス上のこのメールボックスに値を送信します。

        Arguments:
            value:
                メールボックスに配信される値。
            brick (str):
                ブロックの名前またはBluetoothアドレス。 ``None`` の場合は
                接続中のすべてのデバイスにブロードキャストします。

        Raises:
            OSError:
                接続に問題があります。
        """

    def wait(self):
        """リモートデバイスによってメールボックスが更新されるまで待機します。"""

    def wait_new(self):
        """メールボックス内の現在の値と異なる、新しい値がメールボックスに
        配信されるまで待機します。


        Returns:
            新しい値。
        """
        return object()


class LogicMailbox(Mailbox):
    def __init__(self, name, connection):
        """真偽値データを保持するメールボックスを表すオブジェクトです。

        通常の :class:`Mailbox` と同じように動作しますが、
        値は ``True`` または ``False`` のみです。

        EV3-Gの「ロジック」メールボックスタイプと互換性があります。

        Arguments:
            name (str):
                このメールボックスの名前。
            connection:
                :class:`BluetoothMailboxClient` などの接続オブジェクト。
        """


class NumericMailbox(Mailbox):
    def __init__(self, name, connection):
        """数値データを保持するメールボックスを表すオブジェクトです。

        通常の :class:`Mailbox` と同じように動作しますが、
        値は ``15`` や ``12.345`` のような数値である必要があります。

        EV3-Gの「数値」メールボックスタイプと互換性があります。

        Arguments:
            name (str):
                このメールボックスの名前。
            connection:
                :class:`BluetoothMailboxClient` などの接続オブジェクト。
        """


class TextMailbox(Mailbox):
    def __init__(self, name, connection):
        """テキストデータを保持するメールボックスを表すオブジェクトです。

        通常の :class:`Mailbox` と同じように動作しますが、
        データは ``'hello!'`` や ``'My name is EV3'`` のような文字列である
        必要があります。

        EV3-Gの「テキスト」メールボックスタイプと互換性があります。

        Arguments:
            name (str):
                このメールボックスの名前。
            connection:
                :class:`BluetoothMailboxClient` などの接続オブジェクト。
        """


class BluetoothMailboxServer:
    """1台以上のリモートEV3からのBluetooth接続を表すオブジェクトです。

    リモートのEV3は、MicroPythonでも標準のEV3ファームウェアでも
    動作しているものが使えます。

    「サーバー」は「クライアント」からの接続を待ちます。
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def wait_for_connection(self, count=1):
        """リモートデバイス上の :class:`BluetoothMailboxClient` が
        接続するのを待ちます。

        Arguments:
            count (int):
                待機するリモート接続の数。

        Raises:
            OSError:
                接続の確立に問題がありました。
        """

    def close(self):
        """すべての接続を閉じます。"""


class BluetoothMailboxClient:
    """1台以上のリモートEV3へのBluetooth接続を表すオブジェクトです。

    リモートのEV3は、MicroPythonでも標準のEV3ファームウェアでも
    動作しているものが使えます。

    「クライアント」は待機中の「サーバー」への接続を開始します。
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def connect(self, brick):
        """別のデバイス上の :class:`BluetoothMailboxServer` に接続します。

        リモートデバイスはペアリング済みで、接続を待機している必要があります。
        :meth:`BluetoothMailboxServer.wait_for_connection` を参照してください。

        Arguments:
            brick (str):
                接続先のリモートEV3の名前またはBluetoothアドレス。

        Raises:
            OSError:
                接続の確立に問題がありました。
        """

    def server_close(self):
        """すべての接続を閉じます。"""
