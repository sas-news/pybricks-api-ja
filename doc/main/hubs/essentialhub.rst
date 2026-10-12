.. pybricks-requirements:: essentialhub

Essential Hub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/cad/output/hub-essential.png
    :width: 30%

.. autoclass:: pybricks.hubs.EssentialHub
    :no-members:

    .. rubric:: ステータスライトを使う

    .. automethod:: pybricks.hubs::EssentialHub.light.on

    .. automethod:: pybricks.hubs::EssentialHub.light.off

    .. automethod:: pybricks.hubs::EssentialHub.light.blink

    .. automethod:: pybricks.hubs::EssentialHub.light.animate

    .. rubric:: ボタンを使う

    .. automethod:: pybricks.hubs::EssentialHub.buttons.pressed

    .. automethod:: pybricks.hubs::EssentialHub.system.set_stop_button

    .. rubric:: IMUを使う

    .. versionchanged:: 3.6

        以下のメソッドは、デフォルトでキャリブレーション済みのデータを
        返すようになりました。使用するメソッドに応じて、加速度センサーと
        ジャイロスコープのデータが、設定したキャリブレーション値と
        組み合わされます。以前の生データを取得するには、該当する場所で
        ``calibrated=False`` を使用します。

    .. automethod:: pybricks.hubs::EssentialHub.imu.ready

    .. automethod:: pybricks.hubs::EssentialHub.imu.stationary

    .. automethod:: pybricks.hubs::EssentialHub.imu.up

    .. automethod:: pybricks.hubs::EssentialHub.imu.tilt

    .. automethod:: pybricks.hubs::EssentialHub.imu.acceleration

    .. automethod:: pybricks.hubs::EssentialHub.imu.angular_velocity

    .. automethod:: pybricks.hubs::EssentialHub.imu.heading

    .. automethod:: pybricks.hubs::EssentialHub.imu.reset_heading

    .. automethod:: pybricks.hubs::EssentialHub.imu.rotation

    .. automethod:: pybricks.hubs::EssentialHub.imu.orientation

    .. automethod:: pybricks.hubs::EssentialHub.imu.settings

    .. rubric:: バッテリーを使う

    .. automethod:: pybricks.hubs::EssentialHub.battery.voltage

    .. automethod:: pybricks.hubs::EssentialHub.battery.current

    .. rubric:: 充電器の状態を取得する

    .. automethod:: pybricks.hubs::EssentialHub.charger.connected

    .. automethod:: pybricks.hubs::EssentialHub.charger.current

    .. automethod:: pybricks.hubs::EssentialHub.charger.status

    .. rubric:: システム制御

    .. automethod:: pybricks.hubs::EssentialHub.system.info

    .. automethod:: pybricks.hubs::EssentialHub.system.storage

        このハブには最大512バイトのデータを保存できます。データは
        Pybricksファームウェアを更新すると消去されます。

    .. automethod:: pybricks.hubs::EssentialHub.system.reset_storage

    .. automethod:: pybricks.hubs::EssentialHub.system.shutdown

ステータスライトの例
---------------------

ライトのオンとオフ
****************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_off_essentialhub.py

輝度の変更とカスタムカラーの使用
*******************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_hsv_essentialhub.py

ライトを点滅させる
**********************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_blink_essentialhub.py

ライトアニメーションの作成
****************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_animate_essentialhub.py

IMUの例
---------------

どちらが上かを確かめる
********************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_up_essentialhub.py

傾きの値を読み取る
********************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_tilt_essentialhub.py

カスタムのハブの向きを使う
**************************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_tilt_blast_essentialhub.py

加速度と角速度のベクトルを読み取る
**************************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_read_vector_essentialhub.py

1軸の加速度と角速度を読み取る
*****************************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_read_scalar_essentialhub.py

システムの例
----------------------------------

プログラム実行中に停止ボタンを使う
*****************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/button_single_essentialhub.py

ハブの電源を切る
*****************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/system_shutdown_essentialhub.py
