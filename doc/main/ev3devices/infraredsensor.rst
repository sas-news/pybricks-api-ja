.. pybricks-requirements:: ev3devices

Infrared Sensor and Beacon
^^^^^^^^^^^^^^^^^^^^^^^^^^

このクラスの各メソッドは、センサーをそれぞれ異なる *モード* に設定します。
このセンサーではモードの切り替えに約1秒かかります。プログラムを速く実行
できるように、これらのメソッドのうち1つだけを使用してください。

.. figure:: ../../main/cad/output/ev3device-infrared.png
   :width: 60 %

.. autoclass:: pybricks.ev3devices.InfraredSensor
    :no-members:

    .. automethod:: pybricks.ev3devices.InfraredSensor.distance

    .. automethod:: pybricks.ev3devices.InfraredSensor.beacon

    .. automethod:: pybricks.ev3devices.InfraredSensor.buttons

    .. automethod:: pybricks.ev3devices.InfraredSensor.keypad
