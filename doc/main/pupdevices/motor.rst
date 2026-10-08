.. pybricks-requirements:: pupdevices

回転センサー付きモーター
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _fig_pupmotors:

.. figure:: ../../main/diagrams/pupmotors.png
   :width: 100 %
   :alt: pupmotors

   回転センサー付きの Powered Up モーター。矢印はデフォルトの
   正方向を示しています。内蔵モーターのデフォルトの方向は
   :mod:`hubs <pybricks.hubs>` モジュールを参照してください。

.. blockimg:: pybricks_variables_set_motor

.. autoclass:: pybricks.pupdevices.Motor
    :no-members:

    .. include:: ../common/motor_members.rst.txt

初期化の例
-----------------------

モーターを往復させる
*******************************************************

.. literalinclude::
    ../../../examples/pup/motor/motor_init_basic.py

複数のモーターを初期化する
*******************************************************

.. literalinclude::
    ../../../examples/pup/motor/motor_init_multiple.py

正方向を反時計回りに設定する
*******************************************************

.. literalinclude::
    ../../../examples/pup/motor/motor_init_direction.py

ギアを使用する
*******************************************************

.. literalinclude::
    ../../../examples/pup/motor/motor_init_gears.py

測定の例
-----------------------

角度と速度を測定する
*******************************************************

.. literalinclude::
    ../../../examples/pup/motor/motor_measure.py

測定した角度をリセットする
*******************************************************

.. literalinclude::
    ../../../examples/pup/motor/motor_reset_angle.py

絶対角度を取得する
*******************************************************

.. literalinclude::
    ../../../examples/pup/motor/motor_absolute.py


動作の例
-----------------------

すべての ``run`` メソッドの基本的な使い方
*******************************************************

.. literalinclude::
    ../../../examples/pup/motor/motor_action_basic.py

進行中の動作をさまざまな方法で停止する
*******************************************************

.. literalinclude::
    ../../../examples/pup/motor/motor_stop.py

``then`` 引数を使って実行コマンドの停止方法を変える
*************************************************************

.. literalinclude::
    ../../../examples/pup/motor/motor_action_then.py

ストールの例
-----------------------

機械的な端点までモーターを動かす
*******************************************************

.. literalinclude::
    ../../../examples/pup/motor/motor_until_stalled.py

ステアリング機構を中央に合わせる
*******************************************************

.. literalinclude::
    ../../../examples/pup/motor/motor_until_stalled_center.py


並列動作の例
--------------------------

``wait`` 引数を使ってモーターを並列に動かす
*********************************************************

.. literalinclude::
    ../../../examples/pup/motor/motor_action_wait.py

2つの並列動作の完了を待つ
*******************************************************

.. literalinclude::
    ../../../examples/pup/motor/motor_action_wait_advanced.py
