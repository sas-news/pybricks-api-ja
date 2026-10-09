.. pybricks-requirements::

Color
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: pybricks.parameters.Color
    :no-members:

    .. rubric:: 彩度が最大の色

    これらの色は彩度と輝度が最大値になっています。
    色相だけが異なります。

    .. autoattribute:: RED

        .. pybricks-color:: RED

    .. autoattribute:: ORANGE

        .. pybricks-color:: ORANGE

    .. autoattribute:: YELLOW

        .. pybricks-color:: YELLOW

    .. autoattribute:: GREEN

        .. pybricks-color:: GREEN

    .. autoattribute:: CYAN

        .. pybricks-color:: CYAN

    .. autoattribute:: BLUE

        .. pybricks-color:: BLUE

    .. autoattribute:: VIOLET

        .. pybricks-color:: VIOLET

    .. autoattribute:: MAGENTA

        .. pybricks-color:: MAGENTA

    .. rubric:: 無彩色

    これらの色は色相と彩度がゼロです。輝度だけが異なります。

    センサーでこれらの色を検出する場合、検出値は物体までの距離に
    大きく依存します。ロボット内でセンサーと物体の間の距離が一定でない
    場合は、プログラムでこれらの色のうち1つだけを使うのがよいでしょう。

    .. autoattribute:: WHITE

        .. pybricks-color:: WHITE

    .. autoattribute:: GRAY

        .. pybricks-color:: GRAY

    .. autoattribute:: BLACK

        ごくわずかな光を反射する暗い物体を表します。

        .. pybricks-color:: BLACK

    .. autoattribute:: NONE

        反射も光もまったくない、完全な暗闇を表します。

        .. pybricks-color:: NONE

.. rubric:: 自分で色を作る

この例では、色のプロパティの基本と、新しい色の定義方法を示します。

.. literalinclude::
    ../../../examples/pup/parameters/color_basics.py

この例では、 ``Color`` クラスのより高度な使用例を示します。

.. literalinclude::
    ../../../examples/pup/parameters/color_advanced.py
