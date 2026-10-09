:mod:`ev3devices <pybricks.ev3devices>` -- EV3デバイス
============================================================

.. automodule:: pybricks.ev3devices
    :no-members:

モーター
^^^^^^^^^^^^

.. _fig_ev3motors:

.. figure:: ../api/images/ev3motors_label.png
   :width: 100 %

   EV3互換モーター。矢印はデフォルトの正の回転方向を示します。

.. autoclass:: pybricks.ev3devices.Motor
    :no-members:

    .. rubric:: 計測

    .. automethod:: pybricks.ev3devices.Motor.speed

    .. automethod:: pybricks.ev3devices.Motor.angle

    .. automethod:: pybricks.ev3devices.Motor.reset_angle

    .. rubric:: 停止

    .. automethod:: pybricks.ev3devices.Motor.stop

    .. automethod:: pybricks.ev3devices.Motor.brake

    .. automethod:: pybricks.ev3devices.Motor.hold

    .. rubric:: 動作

    .. automethod:: pybricks.ev3devices.Motor.run

    .. automethod:: pybricks.ev3devices.Motor.run_time

    .. automethod:: pybricks.ev3devices.Motor.run_angle

    .. automethod:: pybricks.ev3devices.Motor.run_target

    .. automethod:: pybricks.ev3devices.Motor.run_until_stalled

    .. automethod:: pybricks.ev3devices.Motor.dc

    .. rubric:: 高度なモーション制御

    .. automethod:: pybricks.ev3devices.Motor.track_target

    .. autoattribute:: pybricks.ev3devices.Motor.control
        :annotation:


タッチセンサー
^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../api/images/sensor_ev3_touch.png
   :width: 18 %

.. autoclass:: pybricks.ev3devices.TouchSensor

カラーセンサー
^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../api/images/sensor_ev3_color.png
   :width: 18 %

.. autoclass:: pybricks.ev3devices.ColorSensor

赤外線センサーとビーコン
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../api/images/sensor_ev3_ir.png
   :width: 60 %

.. autoclass:: pybricks.ev3devices.InfraredSensor

超音波センサー
^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../api/images/sensor_ev3_ultrasonic.png
   :width: 22 %

.. autoclass:: pybricks.ev3devices.UltrasonicSensor

ジャイロセンサー
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../api/images/sensor_ev3_gyro.png
   :width: 18 %

.. autoclass:: pybricks.ev3devices.GyroSensor
    :no-members:

    .. automethod:: pybricks.ev3devices.GyroSensor.speed

    .. automethod:: pybricks.ev3devices.GyroSensor.angle

         :meth:`.angle` メソッドを使う場合、同じプログラム内で
         :meth:`.speed` メソッドは使えません。使うと速度を読み取るたびに
         センサーの角度が0にリセットされてしまいます。

    .. automethod:: pybricks.ev3devices.GyroSensor.reset_angle
