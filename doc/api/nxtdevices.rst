:mod:`nxtdevices <pybricks.nxtdevices>` -- NXTデバイス
============================================================

.. automodule:: pybricks.nxtdevices
    :no-members:

NXTモーター
^^^^^^^^^^^^^^^^
このモーターは LEGO MINDSTORMS EV3 Large Motor とまったく同じように
使えます。プログラムでは :mod:`Motor <.ev3devices>` クラスを使います。

NXTタッチセンサー
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../api/images/sensor_nxt_touch.png
   :width: 18 %

.. autoclass:: pybricks.nxtdevices.TouchSensor
    :no-members:

    .. automethod:: pybricks.nxtdevices.TouchSensor.pressed

NXT光センサー
^^^^^^^^^^^^^^^^^^^^

.. figure:: ../api/images/sensor_nxt_light.png
   :width: 18 %

.. autoclass:: pybricks.nxtdevices.LightSensor

NXTカラーセンサー
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../api/images/sensor_nxt_color.png
   :width: 18 %

.. autoclass:: pybricks.nxtdevices.ColorSensor
    :no-members:

    .. automethod:: pybricks.nxtdevices.ColorSensor.color

    .. automethod:: pybricks.nxtdevices.ColorSensor.ambient

    .. automethod:: pybricks.nxtdevices.ColorSensor.reflection

    .. automethod:: pybricks.nxtdevices.ColorSensor.rgb

    .. rubric:: 内蔵ライト

    このセンサーには内蔵ライトがあります。赤・緑・青に点灯させるか、
    消灯できます。

    .. automethod:: pybricks.nxtdevices::ColorSensor.light.on

    .. automethod:: pybricks.nxtdevices::ColorSensor.light.off

NXT超音波センサー
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../api/images/sensor_nxt_ultrasonic.png
   :width: 24 %

.. autoclass:: pybricks.nxtdevices.UltrasonicSensor

NXTサウンドセンサー
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../api/images/sensor_nxt_sound.png
   :width: 18 %

.. autoclass:: pybricks.nxtdevices.SoundSensor

NXT温度センサー
^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../api/images/sensor_nxt_temp.png
   :width: 32 %

.. autoclass:: pybricks.nxtdevices.TemperatureSensor

NXTエネルギーメーター
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../api/images/energymeter.png
   :width: 30 %

.. autoclass:: pybricks.nxtdevices.EnergyMeter

Vernierアダプター
^^^^^^^^^^^^^^^^^^^^^^^^
.. autoclass:: pybricks.nxtdevices.VernierAdapter

.. toggle-header::
    :header: **例を表示/非表示**

    **例: Surface Temperature Sensor を使います。**

    .. literalinclude:: ../../pybricks-projects/snippets/ev3/vernier_surface_temperature/main.py
