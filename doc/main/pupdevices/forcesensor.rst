.. pybricks-requirements:: pupdevices

Force Sensor
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/cad/output/pupdevice-force.png
   :width: 35 %

.. blockimg:: pybricks_variables_set_force_sensor

.. autoclass:: pybricks.pupdevices.ForceSensor
    :no-members:

    .. blockimg:: pybricks_blockSensorPressed_ForceSensor_force

    .. automethod:: pybricks.pupdevices.ForceSensor.force

    .. blockimg:: pybricks_blockDistance_ForceSensor

    .. automethod:: pybricks.pupdevices.ForceSensor.distance

    .. blockimg:: pybricks_blockSensorPressed_ForceSensor_pressed

    .. blockimg:: pybricks_blockSensorPressed_ForceSensor_released

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
