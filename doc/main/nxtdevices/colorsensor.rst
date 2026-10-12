.. pybricks-requirements:: nxtdevices

NXT Color Sensor
^^^^^^^^^^^^^^^^

.. figure:: ../../main/cad/output/nxtdevice-color.png
   :width: 18 %

.. autoclass:: pybricks.nxtdevices.ColorSensor
    :no-members:

    .. automethod:: pybricks.nxtdevices.ColorSensor.color

    .. automethod:: pybricks.nxtdevices.ColorSensor.ambient

    .. automethod:: pybricks.nxtdevices.ColorSensor.reflection

    .. automethod:: pybricks.nxtdevices.ColorSensor.rgb

    .. rubric:: 高度な色検出

    .. automethod:: pybricks.nxtdevices.ColorSensor.hsv

    .. automethod:: pybricks.nxtdevices.ColorSensor.detectable_colors

    .. rubric:: 内蔵ライト

    このセンサーには内蔵ライトがあります。赤・緑・青に光らせたり、オフに
    したりできます。

    .. automethod:: pybricks.nxtdevices::ColorSensor.light.on

    .. automethod:: pybricks.nxtdevices::ColorSensor.light.off
