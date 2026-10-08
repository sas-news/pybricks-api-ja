.. pybricks-requirements:: pupdevices

Power Functions
^^^^^^^^^^^^^^^^^^^^^^^^^

:class:`ColorDistanceSensor <pybricks.pupdevices.ColorDistanceSensor>` は
赤外線信号を送信して、Power Functions の赤外線レシーバーを制御できます。
この手法を使って、M・L・XL・トレインモーターを制御できます。
赤外線の到達距離は約30 cmまでに限られており、角度や周囲の環境によって
変わります。

.. figure:: ../../main/cad/output/pupdevice-pfmotor.png
   :width: 95 %

   Powered Up の
   :class:`ColorDistanceSensor <pybricks.pupdevices.ColorDistanceSensor>`
   （左）、Power Functions の赤外線レシーバー（中央）、
   Power Functions モーター（右）。この例では、レシーバーは
   チャンネル1を使い、赤いポートにモーターを接続しています。

.. blockimg:: pybricks_variables_set_pf_motor

.. autoclass:: pybricks.pupdevices.PFMotor
    :no-members:

    .. blockimg:: pybricks_blockMotorDuty_PFMotor

    .. automethod:: pybricks.pupdevices.PFMotor.dc

    .. blockimg:: pybricks_blockMotorStop_PFMotor_coast

    .. automethod:: pybricks.pupdevices.PFMotor.stop

    .. blockimg:: pybricks_blockMotorStop_PFMotor_brake

    .. automethod:: pybricks.pupdevices.PFMotor.brake

使用例
-------------------

Power Functions モーターを制御する
**********************************

.. literalinclude::
    ../../../examples/pup/motor_pf/motor_pf_basics.py

複数の Power Functions モーターを制御する
*******************************************

.. literalinclude::
    ../../../examples/pup/motor_pf/motor_pf_pwm.py
