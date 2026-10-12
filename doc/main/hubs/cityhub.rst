.. pybricks-requirements:: cityhub

City Hub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. figure:: ../../main/cad/output/hub-city.png
    :width: 30%

.. autoclass:: pybricks.hubs.CityHub
    :no-members:

    .. rubric:: ステータスライトを使う

    .. automethod:: pybricks.hubs::CityHub.light.on

    .. automethod:: pybricks.hubs::CityHub.light.off

    .. automethod:: pybricks.hubs::CityHub.light.blink

    .. automethod:: pybricks.hubs::CityHub.light.animate

    .. rubric:: バッテリーを使う

    .. automethod:: pybricks.hubs::CityHub.battery.voltage

    .. automethod:: pybricks.hubs::CityHub.battery.current

    .. rubric:: ボタンとシステム制御

    .. automethod:: pybricks.hubs::CityHub.buttons.pressed

    .. automethod:: pybricks.hubs::CityHub.system.info

    .. automethod:: pybricks.hubs::CityHub.system.set_stop_button

    .. automethod:: pybricks.hubs::CityHub.system.storage

        このハブには最大128バイトのデータを保存できます。データは、
        Pybricksファームウェアを更新した場合や、元のファームウェアに
        戻した場合に消去されます。

    .. automethod:: pybricks.hubs::CityHub.system.reset_storage

    .. automethod:: pybricks.hubs::CityHub.system.shutdown

ステータスライトの例
---------------------

ライトのオンとオフ
****************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_off_cityhub.py

輝度の変更とカスタムカラーの使用
*******************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_hsv_cityhub.py

ライトを点滅させる
**********************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_blink_cityhub.py

ライトアニメーションの作成
****************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_animate_cityhub.py

ボタンとシステムの例
----------------------------------

プログラム実行中に停止ボタンを使う
*****************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/button_single_cityhub.py

ハブの電源を切る
*****************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/system_shutdown_cityhub.py
