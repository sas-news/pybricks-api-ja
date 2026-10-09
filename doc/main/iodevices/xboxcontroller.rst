.. pybricks-requirements:: xbox-controller

Xboxコントローラー
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/diagrams_source/xboxcontroller.png
   :width: 60 %

.. autoclass:: pybricks.iodevices.XboxController
  :no-members:

  .. automethod:: pybricks.iodevices::XboxController.connect

  .. automethod:: pybricks.iodevices::XboxController.disconnect

  .. automethod:: pybricks.iodevices::XboxController.name

  .. automethod:: pybricks.iodevices::XboxController.buttons.pressed

    ボタンには以下が含まれます:

      * ``Button.A`` 、 ``Button.B`` 、 ``Button.X`` 、 ``Button.Y`` 。
      * ``Button.UP`` 、 ``Button.DOWN`` 、 ``Button.LEFT`` 、
        ``Button.RIGHT`` （方向パッド）。これらは同時に最大2つまで
        押すことができます。
      * ``Button.LB`` と ``Button.RB`` （バンパー）。
      * ``Button.LJ`` と ``Button.RJ`` （ジョイスティックの押し込み）。
      * ``Button.VIEW`` 、 ``Button.MENU`` 、 ``Button.GUIDE`` （Xboxロゴ）、
        および ``Button.UPLOAD`` 。
      * ``Button.P1`` 、 ``Button.P2`` 、 ``Button.P3`` 、 ``Button.P4``
        （Elite Series 2のみ）。
        パドルを押した場合、現在アクティブなプロファイルに応じて、
        他のボタンの押下として検出される場合もあります。

  .. automethod:: pybricks.iodevices::XboxController.joystick_left

  .. automethod:: pybricks.iodevices::XboxController.joystick_right

  .. automethod:: pybricks.iodevices::XboxController.triggers

  .. automethod:: pybricks.iodevices::XboxController.dpad

  .. automethod:: pybricks.iodevices::XboxController.profile

  .. automethod:: pybricks.iodevices::XboxController.rumble

.. _xbox-controller-pairing:

Xboxコントローラーのペアリング手順
====================================
コントローラーを初めてハブで使用する場合は、ペアリングが必要です:
コントローラーの電源を入れ、背面のペアリングボタンを数秒間長押しします。
離すと、Xboxボタンの点滅が速くなります。その後、プログラムを開始します。

ペアリングして接続に成功すると、Xboxボタンは点滅を止め、プログラムが
実行されている間ずっと点灯したままになります。

再接続
------------------

同じコントローラーを同じハブで使い続ける場合は、次回はコントローラーの
電源を入れるだけで、このクラスを使用したプログラムの実行時にハブが
自動的に接続します。

Xboxコントローラーは、最後に接続したデバイスとのみこの簡単な接続を
受け付けます。そのため、Xbox本体に再接続したり、別のハブに接続したり
した場合は、上記の手順で再度ペアリングする必要があります。

対応コントローラー
----------------------

2016年以降に発売されたすべてのXboxコントローラーに対応しています。
これには、One S付属のコントローラー（2016年の ``1708`` ）、
Elite Series 2（2019年の ``1797`` ）、Series X/S（2020年の ``1914`` 、
執筆時点での最新モデル）が含まれます。

.. raw:: html

  <p>各コントローラーの写真を含むモデル番号の<a href="https://en.wikipedia.org/wiki/Xbox_Wireless_Controller#Summary" target="_blank">
  概要</a>も参照してください。</p>

Xboxコントローラーの更新
============================

Xboxコントローラーを本体で頻繁に使用している場合、コントローラーはおそらく
すでに最新の状態です。しばらく使用していなかった場合や最近購入した場合は、
更新が必要なことがあります。

本体なしでコントローラーを更新するには、Windowsコンピューターで
Xboxアクセサリーアプリを使用できます。Microsoft Storeからダウンロード
できます。コントローラーをUSBでコンピューターに接続し、アプリ内の指示に
従って「今すぐ更新」をクリックします。

Technic Hubの制限
=======================

Technic Hubの制限により、Xboxコントローラーを検索している間、ハブは
コンピューターから切断されます。つまり、 ``print`` コマンドの出力を
表示できなくなります。また、プログラムを変更する場合はコンピューターに
再接続する必要があります。
