.. pybricks-requirements:: technichub

Technic Hub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/cad/output/hub-technic.png
    :width: 40%

.. autoclass:: pybricks.hubs.TechnicHub
    :no-members:

    .. rubric:: ステータスライトを使う

    .. automethod:: pybricks.hubs::TechnicHub.light.on

    .. automethod:: pybricks.hubs::TechnicHub.light.off

    .. automethod:: pybricks.hubs::TechnicHub.light.blink

    .. automethod:: pybricks.hubs::TechnicHub.light.animate

    .. rubric:: IMUを使う

    .. versionchanged:: 3.6

        以下のメソッドは、デフォルトでキャリブレーション済みのデータを
        返すようになりました。使用するメソッドに応じて、加速度センサーと
        ジャイロスコープのデータが、設定したキャリブレーション値と
        組み合わされます。以前の生データを取得するには、該当する場所で
        ``calibrated=False`` を使用します。

    .. automethod:: pybricks.hubs::TechnicHub.imu.ready

    .. automethod:: pybricks.hubs::TechnicHub.imu.stationary

    .. automethod:: pybricks.hubs::TechnicHub.imu.up

    .. automethod:: pybricks.hubs::TechnicHub.imu.tilt

    .. automethod:: pybricks.hubs::TechnicHub.imu.acceleration

    .. automethod:: pybricks.hubs::TechnicHub.imu.angular_velocity

    .. automethod:: pybricks.hubs::TechnicHub.imu.heading

    .. automethod:: pybricks.hubs::TechnicHub.imu.reset_heading

    .. automethod:: pybricks.hubs::TechnicHub.imu.rotation

    .. automethod:: pybricks.hubs::TechnicHub.imu.orientation

    .. automethod:: pybricks.hubs::TechnicHub.imu.settings

    .. rubric:: バッテリーを使う

    .. automethod:: pybricks.hubs::TechnicHub.battery.voltage

    .. automethod:: pybricks.hubs::TechnicHub.battery.current

    .. rubric:: ボタンとシステム制御

    .. automethod:: pybricks.hubs::TechnicHub.buttons.pressed

    .. automethod:: pybricks.hubs::TechnicHub.system.info

    .. automethod:: pybricks.hubs::TechnicHub.system.set_stop_button

    .. automethod:: pybricks.hubs::TechnicHub.system.storage

        このハブには最大128バイトのデータを保存できます。データは、
        Pybricksファームウェアを更新した場合や、元のファームウェアに
        戻した場合に消去されます。

    .. automethod:: pybricks.hubs::TechnicHub.system.reset_storage

    .. automethod:: pybricks.hubs::TechnicHub.system.shutdown

ステータスライトの例
---------------------

ライトのオンとオフ
****************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_off_technichub.py

輝度の変更とカスタムカラーの使用
*******************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_hsv_technichub.py

ライトを点滅させる
**********************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_blink_technichub.py

ライトアニメーションの作成
****************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_animate_technichub.py

IMUの例
---------------

どちらが上かを確かめる
********************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_up_technichub.py

傾きの値を読み取る
********************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_tilt_technichub.py

カスタムのハブの向きを使う
**************************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_tilt_blast_technichub.py

加速度と角速度のベクトルを読み取る
**************************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_read_vector_technichub.py

1軸の加速度と角速度を読み取る
*****************************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_read_scalar_technichub.py

ボタンとシステムの例
----------------------------------

プログラム実行中に停止ボタンを使う
*****************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/button_single_technichub.py

ハブの電源を切る
*****************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/system_shutdown_technichub.py
