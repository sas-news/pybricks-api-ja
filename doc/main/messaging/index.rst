:mod:`messaging <pybricks.messaging>` -- メッセージの送受信
==================================================================

.. automodule:: pybricks.messaging
    :no-members:

.. pybricks-requirements:: ble

.. autoclass:: pybricks.messaging.BLERadio
    :no-members:

    .. automethod:: pybricks.messaging.BLERadio.broadcast

    .. automethod:: pybricks.messaging.BLERadio.observe

    .. automethod:: pybricks.messaging.BLERadio.signal_strength

    .. automethod:: pybricks.messaging.BLERadio.version

.. autoclass:: pybricks.messaging.AppData
    :no-members:

    .. automethod:: pybricks.messaging.AppData.get_bytes

    .. automethod:: pybricks.messaging.AppData.write_bytes

    .. automethod:: pybricks.messaging.AppData.configure

    .. automethod:: pybricks.messaging.AppData.close

BLERadio の使用例
------------------

他のHubへデータをブロードキャストする
**************************************

.. literalinclude::
    ../../../examples/pup/ble_radio/ble_broadcast.py

他のHubからデータを観測する
****************************

.. literalinclude::
    ../../../examples/pup/ble_radio/ble_observe.py

EV3 Brick間のメッセージング
----------------------------

.. pybricks-requirements:: hub-network

.. autoclass:: pybricks.messaging.HubNetwork
    :no-members:

    .. automethod:: pybricks.messaging.HubNetwork.address

    .. automethod:: pybricks.messaging.HubNetwork.connect

    .. automethod:: pybricks.messaging.HubNetwork.is_connected

    .. automethod:: pybricks.messaging.HubNetwork.send

    .. automethod:: pybricks.messaging.HubNetwork.inbox
