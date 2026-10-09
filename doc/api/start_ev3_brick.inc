EV3 Brickを使う
===================

EV3 Brickの電源が切れていることを確認してください。準備したmicroSDカードを、
:numref:`fig_sd` のようにEV3 BrickのmicroSDカードスロットに挿入します。

.. _fig_sd:

.. figure:: ../api/images/sd_label.png
   :width: 75 %
   :alt: sd
   :align: center

   書き込み済みのmicroSDカードをEV3 Brickに挿入する


EV3 Brickの電源オン/オフ
-----------------------------------------------------------

中央の濃いグレーのボタンを押して、EV3 Brickの電源を入れます。

起動には数分かかることがあります。起動中、EV3 Brickのステータスライトが
オレンジ色に点滅し、EV3の画面に大量のテキストが表示されます。
ステータスライトが緑色になれば、EV3 Brickは使用できる状態です。

EV3 Brickの電源を切るには、戻るボタンでシャットダウンメニューを開き、
中央ボタンで *Power Off* を選択します（ :numref:`fig_onoff` ）。

.. _fig_onoff:

.. figure:: ../api/images/onoff_label.png
   :width: 65 %
   :alt: onoff
   :align: center

   EV3 Brickの電源を切る

モーターとセンサーの値を見る
-----------------------------------------------------------

プログラムを実行していないときは、 :numref:`fig_devicebrowser` のように
device browserでモーターとセンサーの値を確認できます。

.. _fig_devicebrowser:

.. figure:: ../api/images/devicebrowser_label.png
   :width: 100 %
   :alt: devicebrowser
   :align: center

   モーターとセンサーの値を見る

コンピューターなしでプログラムを実行する
--------------------------------------------------------------

以前にダウンロードしたプログラムは、EV3 Brickから直接実行できます。

EV3画面の *file browser* でプログラムを見つけ、中央ボタンを押すと、
:numref:`fig_manualrun` のようにプログラムが起動します。

.. _fig_manualrun:

.. figure:: ../api/images/manualrun_label.png
   :width: 100 %
   :alt: manualrun
   :align: center

   EV3 Brickのボタンを使ってプログラムを起動する

元のファームウェアに戻す
-----------------------------------------------------------

いつでもLEGO®ファームウェアとLEGOプログラムに戻すことができます。
手順は次のとおりです。

1. 上記の手順でEV3 Brickの電源を切ります。
2. 画面とBrickのステータスライトが消えるまで待ちます。
3. microSDカードを取り出します。
4. EV3の電源を入れます。
