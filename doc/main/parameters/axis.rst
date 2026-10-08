.. pybricks-requirements:: stm32-float

Axis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: pybricks.parameters.Axis
    :no-members:

    .. autoattribute:: pybricks.parameters.Axis.X
        :annotation: = vector(1, 0, 0)

    .. autoattribute:: pybricks.parameters.Axis.Y
        :annotation: = vector(0, 1, 0)

    .. autoattribute:: pybricks.parameters.Axis.Z
        :annotation: = vector(0, 0, 1)

Move Hub では、これらのベクトルを使った演算はサポートされていません。
それでも、これらの軸はハブの向きを設定するために使用できます。
