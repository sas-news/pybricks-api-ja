.. pybricks-requirements:: movehub

Move Hub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _fig_movehub:

.. figure:: ../../main/diagrams/movehub.png
    :width: 100%

.. autoclass:: pybricks.hubs.MoveHub
    :no-members:

    .. rubric:: ステータスライトを使う

    .. automethod:: pybricks.hubs::MoveHub.light.on

    .. automethod:: pybricks.hubs::MoveHub.light.off

    .. automethod:: pybricks.hubs::MoveHub.light.blink

    .. automethod:: pybricks.hubs::MoveHub.light.animate

    .. rubric:: IMUを使う

    .. automethod:: pybricks.hubs::MoveHub.imu.up

    .. automethod:: pybricks.hubs::MoveHub.imu.tilt

    .. automethod:: pybricks.hubs::MoveHub.imu.acceleration

        .. versionchanged:: 3.2

            加速度の単位を m/s² から mm/s² に変更しました。

    .. rubric:: バッテリーを使う

    .. automethod:: pybricks.hubs::MoveHub.battery.voltage

    .. automethod:: pybricks.hubs::MoveHub.battery.current

    .. rubric:: ボタンとシステム制御

    .. automethod:: pybricks.hubs::MoveHub.buttons.pressed

    .. automethod:: pybricks.hubs::MoveHub.system.info

    .. automethod:: pybricks.hubs::MoveHub.system.set_stop_button

    .. automethod:: pybricks.hubs::MoveHub.system.storage

        このハブには最大128バイトのデータを保存できます。データは、
        Pybricksファームウェアを更新した場合や、元のファームウェアに
        戻した場合に消去されます。

    .. automethod:: pybricks.hubs::MoveHub.system.reset_storage

    .. automethod:: pybricks.hubs::MoveHub.system.shutdown

ステータスライトの例
---------------------

ライトのオンとオフ
******************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_off_movehub.py

ライトを点滅させる
******************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_blink_movehub.py

IMUの例
---------------

どちらが上かを確かめる
********************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_up_movehub.py

加速度を読み取る
**************************************************

.. literalinclude::
    ../../../examples/pup/hub_movehub/imu_read_acceleration.py

ボタンとシステムの例
----------------------------------

プログラム実行中に停止ボタンを使う
*****************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/button_single_movehub.py

ハブの電源を切る
*****************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/system_shutdown_movehub.py

乱数を作る
**************************************************

Move Hub には :mod:`urandom` モジュールがありません。アプリケーションで
乱数が必要な場合は、次の例を応用できます。

より正確に動作させるには、 ``_rand`` の初期値を、アプリケーション内で
真にランダムな値に変更してください。たとえば、IMUの加速度やセンサー値が
使えます。

.. literalinclude::
    ../../../examples/pup/hub_movehub/randint_implementation.py
