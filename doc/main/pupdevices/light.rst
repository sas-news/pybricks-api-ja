.. pybricks-requirements:: pupdevices

Light
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/cad/output/pupdevice-light.png
   :width: 35 %

.. blockimg:: pybricks_variables_set_light

.. autoclass:: pybricks.pupdevices.Light
    :no-members:

    .. blockimg:: pybricks_blockLightOn_light_on

    .. automethod:: pybricks.pupdevices.Light.on

    .. blockimg:: pybricks_blockLightOn_light_off

    .. automethod:: pybricks.pupdevices.Light.off

使用例
-------------------

ライトを点滅させる
**********************

.. literalinclude::
    ../../../examples/pup/light/basics.py

輝度を徐々に変化させる
*******************************

.. literalinclude::
    ../../../examples/pup/light/math.py
