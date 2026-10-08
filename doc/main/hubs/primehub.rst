.. pybricks-requirements:: primehub

Prime Hub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/cad/output/hub-spike-inventor.png
    :width: 80%

.. autoclass:: pybricks.hubs.PrimeHub
    :no-members:

    .. rubric:: 中央のライト

    .. figure:: ../../main/diagrams/primehub_light.png
        :width: 22 em

    .. automethod:: pybricks.hubs::PrimeHub.light.on

    .. blockimg:: pybricks_blockLightOnColor_primehub_off

    .. automethod:: pybricks.hubs::PrimeHub.light.off

    .. automethod:: pybricks.hubs::PrimeHub.light.blink

    .. automethod:: pybricks.hubs::PrimeHub.light.animate

    .. rubric:: ライトマトリクス

    .. figure:: ../../main/diagrams/primehub_display.png
        :width: 22 em

    .. automethod:: pybricks.hubs::PrimeHub.display.orientation

    .. automethod:: pybricks.hubs::PrimeHub.display.off

    .. automethod:: pybricks.hubs::PrimeHub.display.pixel

    .. automethod:: pybricks.hubs::PrimeHub.display.icon

    .. automethod:: pybricks.hubs::PrimeHub.display.animate

    .. automethod:: pybricks.hubs::PrimeHub.display.number

    .. automethod:: pybricks.hubs::PrimeHub.display.char

    .. automethod:: pybricks.hubs::PrimeHub.display.text

    .. rubric:: ボタン

    .. figure:: ../../main/diagrams/primehub_buttons.png
        :width: 22 em

    .. automethod:: pybricks.hubs::PrimeHub.buttons.pressed

    .. automethod:: pybricks.hubs::PrimeHub.system.set_stop_button

    .. rubric:: IMU

    .. versionchanged:: 3.6

        以下のメソッドは、デフォルトでキャリブレーション済みのデータを
        返すようになりました。使用するメソッドに応じて、加速度センサーと
        ジャイロスコープのデータが、あなたのキャリブレーション値と
        組み合わされます。以前の生データを取得するには、該当する場所で
        ``calibrated=False`` を使用します。

    .. automethod:: pybricks.hubs::PrimeHub.imu.ready

    .. automethod:: pybricks.hubs::PrimeHub.imu.stationary

    .. automethod:: pybricks.hubs::PrimeHub.imu.up

    .. blockimg:: pybricks_blockTilt_PrimeHub_imu.tilt.pitch

    .. blockimg:: pybricks_blockTilt_PrimeHub_imu.tilt.roll

    .. automethod:: pybricks.hubs::PrimeHub.imu.tilt

    .. automethod:: pybricks.hubs::PrimeHub.imu.acceleration

    .. automethod:: pybricks.hubs::PrimeHub.imu.angular_velocity

    .. automethod:: pybricks.hubs::PrimeHub.imu.heading

    .. automethod:: pybricks.hubs::PrimeHub.imu.reset_heading

    .. automethod:: pybricks.hubs::PrimeHub.imu.rotation

    .. automethod:: pybricks.hubs::PrimeHub.imu.orientation

    .. blockimg:: pybricks_blockImuConfigure_PrimeHub_imu.settings_heading_correction

    .. blockimg:: pybricks_blockImuConfigure_PrimeHub_imu.settings_angular_velocity_threshold

    .. blockimg:: pybricks_blockImuConfigure_PrimeHub_imu.settings_acceleration_threshold

    .. automethod:: pybricks.hubs::PrimeHub.imu.settings

    .. rubric:: スピーカーを使う

    .. automethod:: pybricks.hubs::PrimeHub.speaker.volume

    .. blockimg:: pybricks_blockSpeakerBeep_PrimeHub

    .. automethod:: pybricks.hubs::PrimeHub.speaker.beep

    .. automethod:: pybricks.hubs::PrimeHub.speaker.play_notes

    .. rubric:: バッテリーを使う

    .. blockimg:: pybricks_blockBatteryMeasure_PrimeHub_battery.voltage

    .. automethod:: pybricks.hubs::PrimeHub.battery.voltage

    .. blockimg:: pybricks_blockBatteryMeasure_PrimeHub_battery.current

    .. automethod:: pybricks.hubs::PrimeHub.battery.current

    .. rubric:: 充電器の状態を取得する

    .. automethod:: pybricks.hubs::PrimeHub.charger.connected

    .. automethod:: pybricks.hubs::PrimeHub.charger.current

    .. automethod:: pybricks.hubs::PrimeHub.charger.status

    .. rubric:: システム制御

    .. automethod:: pybricks.hubs::PrimeHub.system.info

    .. automethod:: pybricks.hubs::PrimeHub.system.storage

        このハブには最大512バイトのデータを保存できます。データは
        Pybricksファームウェアを更新すると消去されます。

    .. automethod:: pybricks.hubs::PrimeHub.system.reset_storage

    .. blockimg:: pybricks_blockHubShutdown_PrimeHub

    .. automethod:: pybricks.hubs::PrimeHub.system.shutdown

.. note::

        以下の例では ``PrimeHub`` クラスを使用しています。両方のハブは
        同一であるため、どちらのハブでも例は問題なく動作します。
        必要に応じて ``InventorHub`` に変更できます。

ステータスライトの例
---------------------

ライトのオンとオフ
****************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_off_primehub.py

輝度の変更とカスタムカラーの使用
*******************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_hsv_primehub.py

ライトを点滅させる
**********************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_blink_primehub.py

ライトアニメーションの作成
****************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_animate_primehub.py

マトリクス表示の例
-----------------------

画像を表示する
*****************

.. literalinclude::
    ../../../examples/pup/hub_primehub/display_image.py

数字を表示する
******************

.. literalinclude::
    ../../../examples/pup/hub_primehub/display_number.py

テキストを表示する
********************

.. literalinclude::
    ../../../examples/pup/hub_primehub/display_text.py

個々のピクセルを表示する
****************************

.. literalinclude::
    ../../../examples/pup/hub_primehub/display_pixel.py

表示の向きを変える
********************************

.. literalinclude::
    ../../../examples/pup/hub_primehub/display_orientation.py

.. literalinclude::
    ../../../examples/pup/hub_primehub/display_orientation_imu.py

.. _make_icons:

自分で画像を作る
**********************

.. literalinclude::
    ../../../examples/pup/hub_primehub/display_matrix.py

アイコンを組み合わせて表情を作る
************************************

.. literalinclude::
    ../../../examples/pup/hub_primehub/display_expression.py

アニメーションを表示する
************************

.. literalinclude::
    ../../../examples/pup/hub_primehub/display_animate.py

ボタンの例
---------------

ボタン押下を検出する
************************

.. literalinclude::
    ../../../examples/pup/hub_primehub/button_main.py

IMUの例
---------------

どちらが上かを確かめる
********************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_up_primehub.py


傾きの値を読み取る
********************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_tilt_primehub.py

カスタムのハブの向きを使う
**************************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_tilt_blast_primehub.py

加速度と角速度のベクトルを読み取る
**************************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_read_vector_primehub.py

1軸の加速度と角速度を読み取る
*****************************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_read_scalar_primehub.py

システムの例
----------------------------------

停止ボタンの組み合わせを変える
*****************************************

.. literalinclude::
    ../../../examples/pup/hub_primehub/button_stop.py

ハブの電源を切る
*****************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/system_shutdown_primehub.py

