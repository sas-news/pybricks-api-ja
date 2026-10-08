.. pybricks-requirements::

Side
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. currentmodule:: pybricks.parameters

.. class:: Side

    ハブまたはセンサーの面。これらのデバイスは主に6つの面を持つ
    直方体です:

    .. autoattribute:: pybricks.parameters.Side.TOP
        :annotation:

    .. autoattribute:: pybricks.parameters.Side.BOTTOM
        :annotation:

    .. autoattribute:: pybricks.parameters.Side.FRONT
        :annotation:

    .. autoattribute:: pybricks.parameters.Side.BACK
        :annotation:

    .. autoattribute:: pybricks.parameters.Side.LEFT
        :annotation:

    .. autoattribute:: pybricks.parameters.Side.RIGHT
        :annotation:


    スクリーンやライトマトリクスには4つの面しかありません。それらでは
    ``TOP`` は ``FRONT`` と同じように、 ``BOTTOM`` は ``BACK`` と
    同じように扱われます。以下の図は、関連するデバイスの面を
    定義しています。

    **Prime Hub**

    .. figure:: ../../main/diagrams/orientation_primehub.png
        :width: 60%

    **Inventor Hub**

    .. figure:: ../../main/diagrams/orientation_inventorhub.png
        :width: 60%

    **Essential Hub**

    .. figure:: ../../main/diagrams/orientation_essentialhub.png
        :width: 60%

    **Move Hub**

    .. figure:: ../../main/diagrams/orientation_movehub.png
        :width: 60%

    **Technic Hub**

    .. figure:: ../../main/diagrams/orientation_technichub.png
        :width: 60%

    .. versionchanged:: 3.2

        どの面が前面かを変更しました。

    **Tilt Sensor**

    .. figure:: ../../main/diagrams/orientation_tiltsensor.png
        :width: 50%
