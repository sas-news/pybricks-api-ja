# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2020 The Pybricks Authors

"""汎用入出力デバイス。"""


class LUMPDevice:
    """LEGO UART Messaging Protocolを使用するデバイス。"""

    def __init__(self, port):
        """

        Arguments:
            port (Port): デバイスが接続されているポート。
        """
        pass

    def read(self, mode):
        """指定したモードから値を読み取ります。

        Arguments:
            mode (``int``): デバイスのモード。

        Returns:
            ``tuple``: センサーから読み取られた値。
        """
        pass

    def write(self, mode, values):
        """センサーに値を書き込みます。対応しているセンサーとモードは
        限られています。

        Arguments:
            mode (``int``): デバイスのモード。
            data (``tuple``): 書き込む値。
        """
        pass


class Ev3devSensor:
    """ev3dev互換センサーの値を読み取ります。"""

    sensor_index = 0
    """ev3dev sysfs `lego-sensor`_ クラスのインデックス。"""

    port_index = 0
    """ev3dev sysfs `lego-port`_ クラスのインデックス。"""

    def __init__(self, port):
        """

        Arguments:
            port (Port): デバイスが接続されているポート。
        """
        pass

    def read(self, mode):
        """指定したモードで値を読み取ります。

        Arguments:
            mode (``str``): `Mode name`_。

        Returns:
            ``tuple``: センサーから読み取られた値。
        """
        pass


class AnalogSensor:
    """汎用またはカスタムのアナログセンサー。"""

    def __init__(self, port):
        """

        Arguments:
            port (Port): センサーが接続されているポート。
        """
        pass

    def voltage(self):
        """アナログ電圧を測定します。

        Returns:
            :ref:`voltage`: アナログ電圧。
        """
        pass

    def resistance(self):
        """抵抗を測定します。

        この値は、アナログデバイスが抵抗器やサーミスタなどのパッシブ負荷
        である場合にのみ意味を持ちます。

        Returns:
            :ref:`resistance: Ω <voltage>`: アナログデバイスの抵抗値。
        """
        pass

    def active(self):
        """センサーをアクティブモードに設定します。これによりセンサーポートの
        ピン5が `high` になります。

        一部のアナログセンサーでは、スイッチの制御に使用されます。
        たとえば、NXTライトセンサーをカスタムアナログセンサーとして使用する
        場合、このメソッドはライトを点灯します。それ以降、 ``voltage()`` は
        反射光の生の値を返します。
        """
        pass

    def passive(self):
        """センサーをパッシブモードに設定します。これによりセンサーポートの
        ピン5が `low` になります。

        一部のアナログセンサーでは、スイッチの制御に使用されます。
        たとえば、NXTライトセンサーをカスタムアナログセンサーとして使用する
        場合、このメソッドはライトを消灯します。それ以降、 ``voltage()`` は
        環境光の生の値を返します。
        """
        pass


class I2CDevice:
    """汎用またはカスタムのI2Cデバイス。"""

    def __init__(self, port, address):
        """

        Arguments:
            port (Port): デバイスが接続されているポート。
            address(int): クライアントデバイスのI2Cアドレス。
                :ref:`I2C Addresses <i2caddress>` を参照してください。
        """
        pass

    def read(self, reg, length=1):
        """指定したレジスタからバイトを読み取ります。

        Arguments:
            reg (``int``): 読み取りを開始するレジスタ:
                0--255または0x00--0xFF。
            length (``int``): 読み取るバイト数。

        Returns:
            ``bytes``: デバイスから返されたバイト。
        """
        pass

    def write(self, reg, data=None):
        """指定したレジスタからバイトを書き込みます。

        Arguments:
            reg (``int``): 書き込みを開始するレジスタ:
                0--255または0x00--0xFF。
            data (``bytes``): 書き込むバイト。
        """
        pass


class UARTDevice:
    """汎用UARTデバイス。"""

    def __init__(self, port, baudrate, timeout=None):
        """

        Arguments:
            port (Port): デバイスが接続されているポート。
            baudrate (int): UARTデバイスのボーレート。
            timeout (:ref:`time`): :meth:`.read` が諦めるまでの
                待ち時間。 ``None`` を選ぶと、永久に待ち続けます。
        """
        pass

    def read(self, length=1):
        """バッファから指定したバイト数を読み取ります。

        プログラムは要求したバイト数を受信するまで待機します。 ``timeout``
        を超えると、 ``ETIMEDOUT`` 例外が発生します。

        Arguments:
            length (``int``): 読み取るバイト数。

        Returns:
            ``bytes``: デバイスから返されたバイト。
        """
        pass

    def read_all(self):
        """バッファからすべてのバイトを読み取ります。

        Returns:
            ``bytes``: デバイスから返されたバイト。
        """
        pass

    def write(self, data):
        """バイトを書き込みます。

        Arguments:
            data (``bytes``): 書き込むバイト。
        """
        pass

    def waiting(self):
        """読み取り待ちのバイト数を取得します。

        Returns:
            ``int``: バッファ内のバイト数。
        """
        pass

    def clear(self):
        """バッファを空にします。"""
        pass
