.. pybricks-requirements::

:mod:`tools <pybricks.tools>` -- 汎用ツール
========================================================

.. automodule:: pybricks.tools
    :no-members:

時間計測ツール
---------------

.. blockimg:: pybricks_blockWaitTime

.. blockimg:: pybricks_blockWaitForever

.. autofunction:: wait

.. blockimg:: pybricks_variables_set_stopwatch

.. autoclass:: pybricks.tools.StopWatch
    :no-members:

    .. blockimg:: pybricks_blockStopWatchTime

    .. automethod:: pybricks.tools.StopWatch.time

    .. blockimg:: pybricks_blockStopWatchDo_StopWatch_pause

    .. automethod:: pybricks.tools.StopWatch.pause

    .. blockimg:: pybricks_blockStopWatchDo_StopWatch_resume

    .. automethod:: pybricks.tools.StopWatch.resume

    .. blockimg:: pybricks_blockStopWatchDo_StopWatch_reset

    .. automethod:: pybricks.tools.StopWatch.reset

入力ツール
-----------

.. blockimg:: pybricks_blockReadInput_read_input_first_byte

.. blockimg:: pybricks_blockReadInput_read_input_first_char

.. blockimg:: pybricks_blockReadInput_read_input_last_byte

.. blockimg:: pybricks_blockReadInput_read_input_last_char

.. autofunction:: pybricks.tools.read_input_byte

.. versionchanged:: 3.3

    ``last`` と ``chr`` のオプションが追加されました。


.. pybricks-requirements:: light-matrix

.. autofunction:: pybricks.tools.hub_menu

.. literalinclude::
    ../../../examples/pup/tools/hub_menu.py

線形代数ツール
--------------------

.. versionchanged:: 3.3

    これらのツールは、以前は ``pybricks.geometry`` モジュールにありました。

.. pybricks-requirements:: stm32-float

.. autoclass:: pybricks.tools.Matrix
    :no-members:

    .. autoattribute:: pybricks.tools::Matrix.T

    .. autoattribute:: pybricks.tools::Matrix.shape

.. pybricks-requirements:: stm32-float

.. blockimg:: pybricks_blockVector

.. autofunction:: pybricks.tools.vector

.. autofunction:: pybricks.tools.cross

マルチタスク
--------------------

.. versionadded:: 3.3

Pybricksは ``async`` と ``await`` キーワードを使った協調マルチタスクを
サポートしています。これにより、通常は完了に時間がかかる操作を、
他の操作と並行して実行できます。

.. blockimg:: pybricks_blockMultiTask

.. autofunction:: pybricks.tools.multitask

.. autofunction:: pybricks.tools.run_task

以下の例は、マルチタスクを使ってロボットを前進させ、旋回とグリッパーの
動作を同時に行い、その後後退させる方法を示しています。

.. literalinclude::
    ../../../examples/pup/robotics/drivebase_async.py

.. class:: coroutine

.. class:: await

関数やメソッドの前に ``await`` が付いている場合、それはマルチタスクを
サポートしていることを意味します。 ``run_task`` でコルーチンを実行すると、
``await`` が付いたすべてのメソッドと関数はコルーチンとして動作します。

マルチタスクを使用しない場合は、 ``await`` キーワードを無視して
通常どおりプログラムを書けます。具体的には、 ``run_task`` を使用しない場合、
``await`` が付いた関数は通常の関数として動作します。
