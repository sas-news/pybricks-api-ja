.. pybricks-requirements:: pupdevices

Ultrasonic Sensor
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/diagrams/sensor_ultrasonic_lights.png
   :width: 80 %

.. autoclass:: pybricks.pupdevices.UltrasonicSensor
    :no-members:

    .. automethod:: pybricks.pupdevices.UltrasonicSensor.distance

    .. automethod:: pybricks.pupdevices.UltrasonicSensor.presence

    .. rubric:: 内蔵ライト

    このセンサーには4つの内蔵ライトがあります。それぞれのライトの輝度を
    調整できます。

    .. automethod:: pybricks.pupdevices::UltrasonicSensor.lights.on

    .. automethod:: pybricks.pupdevices::UltrasonicSensor.lights.off

使用例
-------------------

距離を測定してライトを点灯する
**********************************************

.. literalinclude::
    ../../../examples/pup/sensor_ultrasonic/basics.py

ライトの輝度を徐々に変化させる
**********************************************

.. literalinclude::
    ../../../examples/pup/sensor_ultrasonic/math.py
