.. pybricks-requirements:: pupdevices

Remote Control
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/cad/output/pupdevice-remote.png
   :width: 60 %

.. autoclass:: pybricks.pupdevices.Remote
  :no-members:

  .. automethod:: pybricks.pupdevices::Remote.connect

  .. automethod:: pybricks.pupdevices::Remote.name

  .. automethod:: pybricks.pupdevices::Remote.light.on

  .. automethod:: pybricks.pupdevices::Remote.light.off

  .. automethod:: pybricks.pupdevices::Remote.buttons.pressed

  .. automethod:: pybricks.pupdevices::Remote.disconnect

使用例
-------------------

どのボタンが押されているか確認する
**********************************

.. literalinclude::
    ../../../examples/pup/remote/basics.py

リモコンのライトの色を変える
**********************************

.. literalinclude::
    ../../../examples/pup/remote/set_color_basic.py

ボタンを使ってライトの色を変える
*******************************************

.. literalinclude::
    ../../../examples/pup/remote/set_color.py

``timeout`` の設定を使う
**********************************

``timeout`` 引数を使うと、ハブがリモコンを検索する時間を変更できます。
``None`` を選択すると、無制限に検索し続けます。

.. literalinclude::
    ../../../examples/pup/remote/timeout_none.py

指定した ``timeout`` 内にリモコンが見つからなかった場合は、
:ref:`OSError <OSError>` が発生します。この例外をキャッチして、
リモコンが利用できないときに別のコードを実行できます。

.. literalinclude::
    ../../../examples/pup/remote/timeout_exception.py

リモコンの名前を変更する
*******************************

リモコンのBluetooth名を変更できます。工場出荷時のデフォルト名は
``Handset`` です。

.. literalinclude::
    ../../../examples/pup/remote/set_name.py

リモコンに接続するときにこの名前を指定できます。
複数のリモコンが近くにある場合に、正しいものを選べます。

.. literalinclude::
    ../../../examples/pup/remote/use_name.py
