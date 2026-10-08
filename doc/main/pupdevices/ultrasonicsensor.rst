.. pybricks-requirements:: pupdevices

Ultrasonic Sensor
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/diagrams/sensor_ultrasonic_lights.png
   :width: 80 %

.. blockimg:: pybricks_variables_set_ultrasonic_sensor

.. autoclass:: pybricks.pupdevices.UltrasonicSensor
    :no-members:

    .. blockimg:: pybricks_blockDistance_UltrasonicSensor

    .. automethod:: pybricks.pupdevices.UltrasonicSensor.distance

    .. automethod:: pybricks.pupdevices.UltrasonicSensor.presence

    .. rubric:: 内蔵ライト

    このセンサーには4つの内蔵ライトがあります。それぞれのライトの輝度を
    調整できます。

    .. blockimg:: pybricks_blockLightOn_ultrasonicsensor_on

    .. blockimg:: pybricks_blockLightOn_ultrasonicsensor_on_list

    .. automethod:: pybricks.pupdevices::UltrasonicSensor.lights.on

    .. blockimg:: pybricks_blockLightOn_ultrasonicsensor_off

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
