.. pybricks-requirements::

Direction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. currentmodule:: pybricks.parameters

.. class:: Direction

    正の速度または角度の値に対する回転方向。

    .. autoattribute:: pybricks.parameters.Direction.CLOCKWISE
        :annotation:

    .. autoattribute:: pybricks.parameters.Direction.COUNTERCLOCKWISE
        :annotation:

    +--------------------------------+-------------------+-----------------+
    | ``positive_direction =``       | 正の速度:         | 負の速度:       |
    +================================+===================+=================+
    | ``Direction.CLOCKWISE``        | 時計回り          | 反時計回り      |
    +--------------------------------+-------------------+-----------------+
    | ``Direction.COUNTERCLOCKWISE`` | 反時計回り        | 時計回り        |
    +--------------------------------+-------------------+-----------------+

    一般に、時計回りは **モーターのシャフトを時計を見るのと同じように
    見たとき** に定義されます。2つのシャフトを持つモーターもあります。
    迷った場合は、 ``Motor`` クラスのドキュメントの図を参照してください。
