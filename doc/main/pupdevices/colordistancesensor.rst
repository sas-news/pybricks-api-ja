.. pybricks-requirements:: pupdevices

Color and Distance Sensor
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/cad/output/pupdevice-colordistance.png
   :width: 35 %

.. blockimg:: pybricks_variables_set_color_distance_sensor_colordistancesensor_default

.. blockimg:: pybricks_variables_set_color_distance_sensor_colordistancesensor_detectable_colors

.. autoclass:: pybricks.pupdevices.ColorDistanceSensor
    :no-members:

    .. blockimg:: pybricks_blockColor_ColorDistanceSensor_color

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.color

    .. blockimg:: pybricks_blockLightReflection_ColorDistanceSensor

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.reflection

    .. blockimg:: pybricks_blockLightAmbient_ColorDistanceSensor

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.ambient

    .. blockimg:: pybricks_blockDistance_ColorDistanceSensor

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.distance

    .. blockimg:: pybricks_blockColor_ColorDistanceSensor_hsv

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.hsv

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.detectable_colors

    .. rubric:: 内蔵ライト

    このセンサーには内蔵ライトがあります。赤・緑・青に光らせたり、オフにしたりできます。
    この後にセンサーで測定を行うと、ライトはその測定方法のデフォルトの色で
    自動的に点灯し直します。

    .. blockimg:: pybricks_blockLightOnColor_colordistancesensor_on

    .. automethod:: pybricks.pupdevices::ColorDistanceSensor.light.on

    .. blockimg:: pybricks_blockLightOnColor_colordistancesensor_off

    .. automethod:: pybricks.pupdevices::ColorDistanceSensor.light.off

使用例
-------------------

色を測定する
***************

.. literalinclude::
    ../../../examples/pup/sensor_color_distance/color_print.py


色を待つ
*******************

.. literalinclude::
    ../../../examples/pup/sensor_color_distance/wait_for_color.py

距離を測定してライトを点滅させる
*****************************************

.. literalinclude::
    ../../../examples/pup/sensor_color_distance/distance_blink.py

色相・彩度・明度を読み取る
**********************************

.. literalinclude::
    ../../../examples/pup/sensor_color_distance/hsv.py

検出する色を変更する
******************************

デフォルトでは、センサーは赤・黄・緑・青・白・無色を検出するように
設定されており、多くの用途に適しています。

アプリケーションでより良い結果を得るには、検出したい色を事前に測定し、
センサーにその色だけを探させることができます。色は必ず、実際に使うときと
「同じ距離・同じ光の条件」で測定してください。そうすれば、通常は
検出しにくい色でも非常に正確な結果が得られます。

.. literalinclude::
    ../../../examples/pup/sensor_color_distance/detectable_colors.py
