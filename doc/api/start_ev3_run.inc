プログラムの作成と実行
===================================

コンピューターとEV3 Brickのセットアップが完了したので、プログラムを
書き始められます。

プログラムを作成・管理しやすくするために、まずEV3ロボット用の
MicroPythonプロジェクトとプログラムの構成を簡単に見てみましょう。

プログラムは *プロジェクトフォルダー* にまとめられます
( :numref:`fig_projectstructure` )。プロジェクトフォルダーとは、
メインプログラム( **main.py** )と任意のスクリプトやファイルを含む、
コンピューター上のディレクトリです。このプロジェクトフォルダーは
中身ごとEV3 Brickにコピーされ、メインプログラムが実行されます。

このページでは、そのようなプロジェクトを作成してEV3 Brickに転送する
方法を説明します。

.. _fig_projectstructure:

.. figure:: ../api/images/projectstructure_label.png
   :width: 100 %
   :alt: projectstructure
   :align: center

   プロジェクトには **main.py** というプログラムと、
   サウンドやMicroPythonモジュールなどの任意のリソースが含まれます。


新しいプロジェクトを作成する
-----------------------------------------------------------

新しいプロジェクトを作成するには、 :numref:`fig_newproject` のように
EV3 MicroPythonタブを開き、 *create a new project* をクリックします。
表示されたテキストフィールドにプロジェクト名を入力し、 *Enter* を
押します。
確認を求められたら、このプログラムの保存場所を選び、 *choose folder*
をクリックして確定します。

.. _fig_newproject:

.. figure:: ../api/images/newproject_label.png
   :width: 100 %
   :alt: newproject
   :align: center

   新しいプロジェクトを作成する。この例では *getting_started* という
   名前ですが、任意の名前を付けられます。

新しいプロジェクトを作成すると、 *main.py* というファイルが最初から
含まれています。内容を確認したり編集したりするには、
:numref:`fig_projectoverview` のようにファイルブラウザーから開きます。
ここにプログラムを書いていきます。

MicroPythonプログラミングが初めての場合は、既存のコードを残したまま、
そこに自分のコードを追加していくことをおすすめします。

.. _fig_projectoverview:

.. figure:: ../api/images/projectoverview_label.png
   :width: 100 %
   :alt: projectoverview
   :align: center

   デフォルトの *main.py* プログラムを開く。

既存のプロジェクトを開く
-----------------------------------------------------------

以前作成したプロジェクトを開くには、 :numref:`fig_existingproject`
のように *File* をクリックし、
*Open Folder* をクリックします。次に、以前作成した
プロジェクトフォルダーに移動して *OK* をクリックします。
*Open Recent* メニューから最近使ったプロジェクトを開くこともできます。

.. _fig_existingproject:

.. figure:: ../api/images/existingproject_label.png
   :width: 75 %
   :alt: existingproject
   :align: center

   以前作成したプロジェクトを開く。


Visual Studio CodeでEV3 Brickに接続する
-----------------------------------------------------------

コードをEV3 Brickに転送するには、まずmini-USBケーブルでEV3 Brickを
コンピューターに接続し、Visual Studio Codeで接続を設定する必要が
あります。手順は次のとおりです。

- EV3 Brickの電源を入れます
- mini-USBケーブルでEV3 Brickをコンピューターに接続します
- :numref:`fig_connecting` のようにUSB接続を設定します。

.. _fig_connecting:

.. figure:: ../api/images/connecting_label.png
   :width: 100 %
   :alt: connecting
   :align: center

   コンピューターとEV3 Brick間のUSB接続を設定する

プログラムをダウンロードして実行する
-----------------------------------------------------------

F5キーを押してプログラムを実行できます。または、 *debug* タブを開いて
緑色の開始矢印をクリックして手動で起動できます( :numref:`fig_running` )。

プログラムが開始すると、ポップアップツールバーが表示され、必要に応じて
プログラムを停止できます。EV3 Brickの戻るボタンでもいつでも
プログラムを停止できます。

プログラムが ``print`` コマンドで何か出力を生成した場合、それは
出力ウィンドウに表示されます。

.. _fig_running:

.. figure:: ../api/images/running_label.png
   :width: 100 %
   :alt: running
   :align: center

   プログラムを実行する

サンプルプログラムを拡張する
-----------------------------------------------------------

基本的なコードテンプレートを実行できたので、プログラムを拡張して
モーターを動かしてみましょう。まず、 :numref:`fig_firstprogram` の
ように、EV3 BrickのポートBにLarge Motorを接続します。

.. _fig_firstprogram:

.. figure:: ../api/images/firstprogram_label.png
   :width: 100 %
   :alt: firstprogram
   :align: center

   ポートBにLarge Motorを接続したEV3 Brick。

次に、 *main.py* を次のように編集します:

.. literalinclude::
   ../../pybricks-projects/snippets/ev3/getting_started/main.py

このプログラムはロボットをビープさせ、モーターを回転させ、もう一度
高音でビープさせます。プログラムを実行して、期待どおりに動作することを
確認してください。

.. _managefiles:

EV3 Brick上のファイルを管理する
-----------------------------------------------------------

プロジェクトをEV3 Brickにダウンロードしたら、
:numref:`fig_files` のようにdevice browserを使って、Brick上の
プログラムを実行・削除・バックアップできます。

.. _fig_files:

.. figure:: ../api/images/files_label.png
   :width: 100 %
   :alt: files
   :align: center

   EV3 device browserでEV3 Brick上のファイルを管理する
