.. pybricks-requirements:: pybricks-iodevices

Powered Upデバイス
^^^^^^^^^^^^^^^^^^^^

.. figure:: ../cad/output/iodevice-pupdevice.png
   :width: 60 %

.. autoclass:: pybricks.iodevices.PUPDevice
    :no-members:

    .. automethod:: pybricks.iodevices.PUPDevice.info

    .. automethod:: pybricks.iodevices.PUPDevice.read

    .. automethod:: pybricks.iodevices.PUPDevice.write

    .. automethod:: pybricks.iodevices.PUPDevice.reset

例
-------------------

デバイスの検出
******************************

.. literalinclude::
    ../../../examples/pup/iodevices_pupdevice/port_info.py
