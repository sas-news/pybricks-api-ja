アナログセンサー
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../api/images/sensor_rj12_brown.png
   :width: 25 %

.. autoclass:: pybricks.iodevices.AnalogSensor

I2Cデバイス
^^^^^^^^^^^^^^^^^^

.. figure:: ../api/images/sensor_rj12_bluegreen.png
   :width: 25 %

.. autoclass:: pybricks.iodevices.I2CDevice

.. toggle-header::
    :header: **例を表示/非表示**

    **例: I2Cデバイスへの読み取りと書き込み**

    .. literalinclude:: ../../pybricks-projects/snippets/ev3/i2c_basics/main.py

.. _i2caddress:

I2Cアドレス
-----------------
I2Cアドレスは7ビットの値です。ただし、LEGO互換センサーを製造する
ほとんどのベンダーは、ドキュメントで8ビットのアドレスを提供しています。
これらのアドレスを使用するには、1ビットシフトする必要があります。
たとえば、記載されているアドレスが ``0xD2`` の場合は、
``address = 0xD2 >> 1`` とできます。

高度なI2Cコマンド
--------------------------
一部の基本的なI2Cデバイスは、レジスタ引数やデータを必要としません。
以下の例に示すように、この動作を実現できます。

.. toggle-header::
    :header: **例を表示/非表示**

    **例: 高度なI2C読み取りと書き込みのテクニック**

    .. literalinclude:: ../../pybricks-projects/snippets/ev3/i2c_extra/main.py

**その他の技術資料**

``I2CDevice`` クラスのメソッドは、Linux SMBusドライバーの関数を
呼び出します。内部でどのコマンドが呼び出されているかは、
`Pybricksのソースコード`_ を確認してください。
MicroPythonを使わずにI2Cを使用する詳細については、
`ev3dev I2C`_ のページを参照してください。

.. _ev3dev I2C: http://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-stretch/i2c.html
.. _Pybricksのソースコード: https://github.com/pybricks/pybricks-micropython


UARTデバイス
^^^^^^^^^^^^^^^^^^

.. figure:: ../api/images/sensor_rj12_gray.png
   :width: 25 %

.. autoclass:: pybricks.iodevices.UARTDevice

.. toggle-header::
    :header: **例を表示/非表示**

    **例: UARTデバイスへの読み取りと書き込み**

    .. literalinclude::
        ../../pybricks-projects/snippets/ev3/uart_basics/main.py

DCモーター
^^^^^^^^^^^^^^^^

.. figure:: ../api/images/rcxmotor.png
   :width: 40 %

.. autoclass:: pybricks._common.DCMotor
    :noindex:
    :no-members:

    .. automethod:: pybricks._common.DCMotor.dc
        :noindex:

    .. automethod:: pybricks._common.DCMotor.stop
        :noindex:

Ev3devセンサー
^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../api/images/sensor_ev3dev.png
   :width: 70 %

EV3 MicroPythonはev3devの上に構築されているため、このドキュメントに
記載されていないセンサーでもサポートされている場合があります。その場合、
``Ev3devSensor`` クラスで使用できます。これは上記のカスタムデバイス
クラスを使うより簡単で高速です。

``Ev3devSensor`` クラスを使用できるかどうかを確認するには:

    * センサーをEV3ブロックに接続します。
    * EV3ブロックのメインメニューを開きます。
    * `Device Browser` を選択し、次に `Sensors` を選択します。
    * センサーが表示されれば、使用できます。

メニューからセンサーを選択し、 `set mode` を選択します。そのセンサーで
利用可能なすべてのモードが表示されます。これらのモード名を、後述の
``mode`` 設定で使用できます。

対応デバイスと各モードの詳細については、 `ev3dev sensors`_ のページを
参照してください。

.. autoclass:: pybricks.iodevices.Ev3devSensor
    :no-members:

    .. autoattribute:: pybricks.iodevices.Ev3devSensor.sensor_index
        :annotation:

    .. autoattribute:: pybricks.iodevices.Ev3devSensor.port_index
        :annotation:

    .. automethod:: pybricks.iodevices.Ev3devSensor.read

.. toggle-header::
    :header: **例を表示/非表示: Ev3devSensorクラスで値を読み取る**

    **例**

    この例では、LEGO MINDSTORMS EV3カラーセンサーをraw RGBモードで
    使用します。これにより、補正されていない赤、緑、青の反射値が
    得られます。

    .. literalinclude::
        ../../pybricks-projects/snippets/ev3/ev3devsensor/main.py

.. toggle-header::
    :header: **例を表示/非表示: Ev3devSensorクラスの拡張**

    **例**

    この例では、このデバイスのLinuxシステムフォルダにある追加機能に
    アクセスして、 ``Ev3devSensor`` クラスを拡張する方法を示します。

    .. literalinclude::
        ../../pybricks-projects/snippets/ev3/ev3devsensor/class_example.py

.. _ev3dev sensors: http://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-stretch/sensors.html
.. _Mode name: http://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-stretch/sensor_data.html
.. _lego-sensor: http://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-stretch/sensors.html#the-lego-sensor-subsytem
.. _lego-port: http://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-stretch/ports.html#the-lego-port-subsystem
