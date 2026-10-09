.. pybricks-requirements:: pupdevices

Infrared Sensor
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/cad/output/pupdevice-infrared.png
   :width: 35 %

.. autoclass:: pybricks.pupdevices.InfraredSensor
    :no-members:

    .. automethod:: pybricks.pupdevices.InfraredSensor.distance

    .. automethod:: pybricks.pupdevices.InfraredSensor.reflection

    .. automethod:: pybricks.pupdevices.InfraredSensor.count

使用例
-------------------

距離・物体の数・反射を測定する
************************************************

.. literalinclude::
    ../../../examples/pup/sensor_infrared/basics.py
