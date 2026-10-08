汎用I2Cデバイス
^^^^^^^^^^^^^^^^^^

EV3とNXTは、汎用I2Cデバイスのハブへの接続をサポートしています。
:doc:`こちらのピン配置 <uartdevice>` を参照してください。

.. figure:: ../../main/cad/output/iodevice-rj12cyan.png
   :width: 25 %

.. autoclass:: pybricks.iodevices.I2CDevice

**例: I2Cデバイスへの読み取りと書き込み**

.. literalinclude:: ../../../examples/ev3/i2c_basics/main.py

.. _i2caddress:

I2Cアドレス
---------------
I2Cアドレスは7ビットの値です。ただし、LEGO互換センサーを製造する
ほとんどのベンダーは、ドキュメントで8ビットのアドレスを提供しています。
これらのアドレスを使用するには、1ビットシフトする必要があります。
たとえば、記載されているアドレスが ``0xD2`` の場合は、
``address = 0xD2 >> 1`` とできます。

高度なI2Cコマンド
---------------------
一部の基本的なI2Cデバイスは、レジスタ引数やデータを必要としません。
以下の例に示すように、この動作を実現できます。

**例: 高度なI2C読み取りと書き込みのテクニック**

.. literalinclude:: ../../../examples/ev3/i2c_extra/main.py

**追加の技術リソース**

``I2CDevice`` クラスのメソッドは、Linux SMBusドライバーの関数を
呼び出します。内部でどのコマンドが呼び出されているかを確認するには、
`Pybricks source code`_ をチェックしてください。
MicroPythonを使用せずにI2Cを使用する詳細については、 `ev3dev I2C`_ の
ページを参照してください。

.. _ev3dev I2C: http://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-stretch/i2c.html
.. _Pybricks source code: https://github.com/pybricks/pybricks-micropython
