.. pybricks-requirements:: pupdevices

回転センサーなしモーター
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _fig_pupdcmotors:

.. figure:: ../../main/diagrams/pupdcmotors.png
   :width: 70 %
   :alt: pupmotors
   :align: center

   回転センサーなしの Powered Up モーター。矢印はデフォルトの
   正方向を示しています。

.. autoclass:: pybricks.pupdevices.DCMotor
    :no-members:

    .. automethod:: pybricks.pupdevices.DCMotor.dc

    .. automethod:: pybricks.pupdevices.DCMotor.stop

    .. automethod:: pybricks.pupdevices.DCMotor.brake

    .. automethod:: pybricks.pupdevices.DCMotor.settings

使用例
-------------------

電車を走らせ続ける
************************************

.. literalinclude::
    ../../../examples/pup/motor_dc/motor_dc_battery_box.py

モーターを往復させる
************************************

.. literalinclude::
    ../../../examples/pup/motor_dc/motor_dc_init_basic.py

正方向を変更する
*******************************

.. literalinclude::
    ../../../examples/pup/motor_dc/motor_dc_init_direction.py

起動と停止
*********************

.. literalinclude::
    ../../../examples/pup/motor_dc/motor_dc_stop.py
