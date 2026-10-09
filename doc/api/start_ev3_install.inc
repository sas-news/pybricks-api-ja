インストール
===================

このページでは、プログラミングを始めるために必要なものを集めて
インストールする手順を説明します。

必要なもの
-----------------------------------------------------------

始めるには、以下のものが必要です。

- Windows 10またはMac OSのコンピューター
- インターネット接続と管理者権限

    これらが必要なのはインストール中だけです。その後プログラムを書いて
    実行するときに特別な権限は必要ありません。

- microSDカード

    容量が4GB以上32GB以下のカードが必要です。このタイプのmicroSDカードは
    microSDHCとも呼ばれます。Application Performance Class A1のカードを
    おすすめします。

- コンピューターのmicroSDカードスロットまたはカードリーダー

    コンピューターに(micro)SDカードスロットがない場合は、外付けの
    USB (micro)SDカードリーダーを使えます。

- EV3セットに付属しているようなmini-USBケーブル

この機器の典型的な構成を
:numref:`fig_overview` にまとめました。

.. _fig_overview:

.. figure:: ../api/images/overview_label.png
   :width: 90 %
   :alt: overview
   :align: center

   セットアップの概要

コンピューターの準備
-----------------------------------------------------------

MicroPythonプログラムはVisual Studio Codeを使って書きます。以下の手順で
このアプリケーションをダウンロード、インストール、設定してください。

1. `Visual Studio Code <https://code.visualstudio.com/Download>`_ を
   ダウンロードします。
2. 画面の指示に従ってアプリケーションをインストールします。
3. Visual Studio Codeを起動します。
4. 拡張機能タブを開きます。
5. :numref:`fig_store` のようにEV3 MicroPython拡張機能を
   インストールします。

.. _fig_store:

.. figure:: ../api/images/store_label.png
    :alt: store
    :align: center

    Visual Studio Codeのマーケットプレイスから拡張機能を
    インストールする

.. _prepsdcard:

microSDカードの準備
-----------------------------------------------------------

EV3 BrickでMicroPythonプログラムを実行できるようにするため、必要な
ツールをmicroSDカードにインストールする方法を説明します。

microSDカードに残したいファイルがある場合は、先に内容のバックアップを
作成してください。
必要に応じて、以前のMicroPythonプログラムをバックアップする方法は
:ref:`EV3上のファイルの管理 <managefiles>` を参照してください。

*この手順では、以前のMicroPythonプログラムを含むmicroSDカード上の
すべての内容が消去されます。*


microSDカードにMicroPythonツールをインストールするには:

.. include:: start_ev3_download.inc

2. `Etcher <https://www.balena.io/etcher/>`_ などのmicroSDカード
   書き込みツールをダウンロードしてインストールします。
3. microSDカードをコンピューターまたはカードリーダーに挿入します。
4. 書き込みツールを起動し、画面の手順に従ってダウンロードした
   ファイルを書き込みます。Etcherを使う場合は、 :numref:`fig_etcher`
   のように以下の手順に従えます。

    a. ダウンロードしたEV3 MicroPython microSDカードイメージファイルを
       選択します。
    b. microSDカードを選択します。デバイスとサイズが使用するmicroSD
       カードと一致していることを確認してください。
    c. 書き込みを開始します。数分かかることがあります。書き込みが
       完了するまでカードを抜かないでください。

.. _fig_etcher:

.. figure:: ../api/images/etcher_label.png
   :width: 85 %
   :alt: etcher
   :align: center

   Etcherを使ってEV3 MicroPython microSDカードイメージを書き込む

microSDカードの更新
-----------------------------------------------------------

microSDカードを更新するには、上記のリンクから新しいイメージファイルを
ダウンロードし、上記の手順でmicroSDカードに書き込んでください。
残したいMicroPythonプログラムは必ず
:ref:`バックアップしてください <managefiles>`。

先にmicroSDカードの内容を消去する必要はありません。新しいイメージ
ファイルを書き込むときに自動で消去されます。
