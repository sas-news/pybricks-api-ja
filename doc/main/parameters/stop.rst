.. pybricks-requirements::

Stop
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. currentmodule:: pybricks.parameters

.. class:: Stop

    モーターが停止したときの動作。

    .. autoattribute:: pybricks.parameters.Stop.COAST
        :annotation:

    .. autoattribute:: pybricks.parameters.Stop.COAST_SMART
        :annotation:

    .. autoattribute:: pybricks.parameters.Stop.BRAKE
        :annotation:

    .. autoattribute:: pybricks.parameters.Stop.HOLD
        :annotation:

    .. autoattribute:: pybricks.parameters.Stop.NONE
        :annotation:

    次の表は、基本的な停止タイプごとに、動きへの抵抗がどのように
    強くなるかを示しています。これらの例では、 ``m`` は
    :class:`Motor <pybricks.pupdevices.Motor>` 、 ``d`` は
    :class:`DriveBase <pybricks.robotics.DriveBase>` です。
    例には、速度0での回転がこれらの停止タイプとどう比較されるかも
    示しています。

    +--------+------------+------------+-------------+---------------+-----------------------------------------+
    | | 種類 | | 摩擦     | | 逆起電力 | | 速度を0に | | 目標角度を  | | 例                                    |
    |        |            |            | | 維持      | | 維持        |                                         |
    +========+============+============+=============+===============+=========================================+
    | Coast  | +          |            |             |               | | ``m.stop()``                          |
    |        |            |            |             |               | | ``m.run_target(500, 90, Stop.COAST)`` |
    +--------+------------+------------+-------------+---------------+-----------------------------------------+
    | Brake  | +          | +          |             |               | | ``m.brake()``                         |
    |        |            |            |             |               | | ``m.run_target(500, 90, Stop.BRAKE)`` |
    +--------+------------+------------+-------------+---------------+-----------------------------------------+
    |        | +          | +          | +           |               | | ``m.run(0)``                          |
    |        |            |            |             |               | | ``d.drive(0, 0)``                     |
    +--------+------------+------------+-------------+---------------+-----------------------------------------+
    | Hold   | +          | +          | +           | +             | | ``m.hold()``                          |
    |        |            |            |             |               | | ``m.run_target(500, 90, Stop.HOLD)``  |
    |        |            |            |             |               | | ``d.straight(0)``                     |
    |        |            |            |             |               | | ``d.straight(100)``                   |
    +--------+------------+------------+-------------+---------------+-----------------------------------------+
