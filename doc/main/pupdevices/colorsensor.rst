.. pybricks-requirements:: pupdevices

Color Sensor
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/diagrams/sensor_color_lights.png
   :width: 70 %

.. autoclass:: pybricks.pupdevices.ColorSensor
    :no-members:

    .. automethod:: pybricks.pupdevices.ColorSensor.color

    .. automethod:: pybricks.pupdevices.ColorSensor.reflection

    .. automethod:: pybricks.pupdevices.ColorSensor.ambient

    .. rubric:: 高度な色検出

    .. automethod:: pybricks.pupdevices.ColorSensor.hsv

    .. automethod:: pybricks.pupdevices.ColorSensor.detectable_colors

    .. rubric:: 内蔵ライト

    このセンサーには3つの内蔵ライトがあります。それぞれのライトの輝度を
    調整できます。センサーで測定を行うと、測定に必要に応じてライトが
    自動的にオン・オフされます。

    .. automethod:: pybricks.pupdevices::ColorSensor.lights.on

    .. automethod:: pybricks.pupdevices::ColorSensor.lights.off

使用例
-------------------

色と反射を測定する
******************************

.. literalinclude::
    ../../../examples/pup/sensor_color/color_print.py

色を待つ
*******************

.. literalinclude::
    ../../../examples/pup/sensor_color/wait_for_color.py

反射光での色相・彩度・明度を読み取る
************************************************

.. literalinclude::
    ../../../examples/pup/sensor_color/hsv.py

検出する色を変更する
******************************

デフォルトでは、センサーは赤・黄・緑・青・白・無色を検出するように
設定されており、多くの用途に適しています。

アプリケーションでより良い結果を得るには、検出したい色を事前に測定し、
センサーにその色だけを探させることができます。色は必ず、実際に使うときと
「同じ距離・同じ光の条件」で測定してください。そうすれば、通常は
検出しにくい色でも非常に正確な結果が得られます。

.. literalinclude::
    ../../../examples/pup/sensor_color/detectable_colors.py

環境光での色相・彩度・明度・色を読み取る
***************************************************

.. literalinclude::
    ../../../examples/pup/sensor_color/color_ambient.py

内蔵ライトを点滅させる
****************************

.. literalinclude::
    ../../../examples/pup/sensor_color/lights_blink.py

プログラム終了時にライトをオフにする
**********************************************

.. literalinclude::
    ../../../examples/pup/sensor_color/cleanup.py
