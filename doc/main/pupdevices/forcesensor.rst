.. pybricks-requirements:: pupdevices

Force Sensor
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/cad/output/pupdevice-force.png
   :width: 35 %

.. autoclass:: pybricks.pupdevices.ForceSensor
    :no-members:

    .. automethod:: pybricks.pupdevices.ForceSensor.force

    .. automethod:: pybricks.pupdevices.ForceSensor.distance

    .. automethod:: pybricks.pupdevices.ForceSensor.pressed

    .. automethod:: pybricks.pupdevices.ForceSensor.touched

使用例
-------------------

力と動きを測定する
****************************

.. literalinclude::
    ../../../examples/pup/sensor_force/basics.py

ピークの力を測定する
********************

.. literalinclude::
    ../../../examples/pup/sensor_force/peak.py
