DCモーター
^^^^^^^^^^^^^^^^^^

このクラスはEV3とNXT専用です。モーターとして自動検出されないモーターを
駆動できます。公式の変換ケーブルで接続されたRCXモーターや
Power Functionモーターが含まれます。注意: カスタム電子回路にモーター用の
電源を供給すると、ハブやデバイスを損傷する可能性があります。

Powered Up DCモーターの場合は、モーターを自動的に検出して正しく安全な
設定を使用する :class:`DCMotor <pybricks.pupdevices.DCMotor>` クラスを
代わりに使用してください。

.. figure:: ../../main/cad/output/iodevice-dcmotor.png
   :width: 40 %

.. autoclass:: pybricks.iodevices.DCMotor
    :no-members:

    .. automethod:: pybricks.iodevices.DCMotor.dc

    .. automethod:: pybricks.iodevices.DCMotor.brake

    .. automethod:: pybricks.iodevices.DCMotor.stop

    .. automethod:: pybricks.iodevices.DCMotor.settings
