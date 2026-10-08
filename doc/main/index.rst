Pybricks ドキュメント
==================================================================

.. only:: ide

   このドキュメントではPybricksのすべての関数とクラスを説明しています。
   たとえば、モーターの速度など、特定の関数パラメータの意味を調べられます。

   Pybricksをはじめて使う場合は、まず `Pybricks learn`_
   ガイドから始めることをおすすめします。

.. only:: main

   `Pybricks <https://pybricks.com/>`_ は、LEGO® Hub用のPython実行環境です。
   MicroPythonを実行するHubに接続し、モーターとセンサーを制御します。

   Pybricksは、LEGO® BOOST、City、Technic、MINDSTORMS®、SPIKE®上で実行できます。
   ブラウザがあればどこでもコーディングできます。

   .. note:: ここはPybricksのコーディングに関するドキュメントです。
             Pybricksについて詳しく学ぶなら `PybricksのWebサイト`_ を参照してください。

   .. note:: LEGO MINDSTORMS EV3を使っている場合は、
            `EV3用ドキュメント`_ を参照してください。

このドキュメントではSPIKE Primeに限定して日本語化しています。

以下のデバイスをクリックすると、そのドキュメントに移動します。
左側のメニューで、Pybricksのモジュールや関数を探すこともできます。
☰をクリックして、メニューを開く必要がある場合があります。

.. _EV3用ドキュメント: ev3/index.html
.. _PybricksのWebサイト: https://pybricks.com/
.. _Pybricks learn: https://pybricks.com/learn/

.. rubric:: Hub一覧

.. figure:: ../main/cad/output/hub-all.png
   :width: 100 %
   :target: hubs/index.html

.. rubric:: モーターとセンサー

.. figure:: ../main/cad/output/pupdevice-all.png
   :width: 100 %
   :target: pupdevices/index.html

.. figure:: ../main/cad/output/pupdevice-motors.png
   :width: 100 %
   :target: pupdevices/motor.html

.. figure:: ../main/cad/output/pupdevice-dcmotors.png
   :width: 70 %
   :target: pupdevices/dcmotor.html

.. rubric:: EV3のモーターとセンサー

.. figure:: ../main/cad/output/ev3device-all.png
   :width: 100 %
   :target: ev3devices/index.html

.. toctree::
    :maxdepth: 1
    :caption: Table of contents
    :hidden:

.. toctree::
   :maxdepth: 1
   :caption: Pybricks modules
   :hidden:

   hubs/index
   pupdevices/index
   ev3devices/index
   nxtdevices/index
   iodevices/index
   parameters/index
   tools/index
   robotics
   messaging/index
   signaltypes

.. toctree::
   :maxdepth: 1
   :caption: MicroPython modules
   :hidden:

   micropython/builtins
   micropython/exceptions
   micropython/micropython
   micropython/uerrno
   micropython/uio
   micropython/ujson
   micropython/umath
   micropython/urandom
   micropython/uselect
   micropython/ustruct
   micropython/usys
