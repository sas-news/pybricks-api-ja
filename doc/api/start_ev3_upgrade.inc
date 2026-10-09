v1.0からv2.0へのアップグレード
===========================================

*EV3 MicroPython v2.0は2020年5月18日にリリースされました。*

このセクションは、以前にLEGO MINDSTORMS EV3
MicroPython v1.0を使っていたユーザー向けです。変更点と、最新の改善を
利用するためのアップグレード方法を説明します。

新規ユーザーでバージョン2.0を使い始めたばかりの場合は、このセクションを
読み飛ばしても構いません。

microSDカードのアップグレード
-----------------------------------------

アップグレードするには、最新のmicroSDカードファイルをダウンロードし、
標準の :ref:`手順 <prepsdcard>` でインストールしてください。

これによりSDカード上の既存のファイルはすべて消去されることに注意して
ください。
アップグレードする前に、すべてのプロジェクトがコンピューター上に
残っていることを確認してください。
残っていない場合は、
:ref:`こちらの手順 <managefiles>` でファイルをコンピューターに
アップロードして戻すことができます。

どんなソフトウェア更新でも、 *更新するタイミングには注意してください* 。
たとえば、
v1.0でコードを開発していてロボット競技会のシーズン途中である場合は、
しばらくv1.0のままにしておくとよいでしょう。


既存プログラムのアップグレード
-----------------------------------------------

v2.0の変更のほとんどは、追加センサーのサポートなどの *新機能* です。
当然ながら、これは既存のコードには影響しません。
ただし、パフォーマンスを改善するために既存機能にもいくつか変更が
加えられています。

v1.0でドキュメント化されていたすべての機能は、アップグレード後も
動作します。
つまり、v1.0向けに作られたほとんどのプログラムは、v2.0のmicroSD
カードイメージで変更なしに動作します。

試すには、以前と同じように元のコードをダウンロードして実行するだけです。

ただし、すべてが期待どおり動作することを確実にするために、microSD
カードとプログラムの両方を同時にアップグレードすることを
おすすめします。

新しいEV3Brick()クラスがev3brickモジュールを置き換え
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

バージョン2.0では :class:`EV3Brick() <pybricks.hubs.EV3Brick>` クラスが
導入されました。
古い ``ev3brick`` モジュールの代わりに使用できます。古い ``ev3brick``
モジュールも引き続き使用できますが、推奨されず、ドキュメント化も
されていません。

:class:`EV3Brick() <pybricks.hubs.EV3Brick>` クラスは、EV3画面と
EV3スピーカーの速度と信頼性を向上させます。音声や図形描画などの機能も
追加されています。また、デフォルトの
フォントサイズが大きくなり、画面上のテキストが読みやすくなりました。

以下の表をスクリプトをアップグレードするための手がかりとして使えます。
すべてのメソッドと引数の完全な詳細は、
:class:`EV3Brick() <pybricks.hubs.EV3Brick>` クラスのドキュメントを
参照してください。

.. list-table::

  * - **操作**
    - **v1.0**
    - **v2.0**

  * - | EV3を
      | 初期化する
    - ::

          from pybricks import ev3brick as brick
    - ::

          from pybricks.hubs import EV3Brick

          ev3 = EV3Brick()

  * - | ライトを点灯する
    - ::

          brick.light(Color.RED)
    - ::

          ev3.light.on(Color.RED)

  * - | ライトを消灯する
    - ::

          brick.light(None)
    - ::

          ev3.light.off()

  * - | ボタンを
      | 読み取る
    - ::

          if Button.LEFT in brick.buttons():
              print("Left is pressed.")
    - ::

          if Button.LEFT in ev3.buttons.pressed():
              print("Left is pressed.")

  * - | ビープ音を
      | 鳴らす
    - ::

          brick.sound.beep()
    - ::

          ev3.speaker.beep()

  * - | サウンドファイルを
      | 再生する
    - ::

          brick.sound.file(SoundFile.HELLO)
    - ::

          ev3.speaker.play_file(SoundFile.HELLO)

  * - | テキストを
      | 音声に変換する
    -
    - ::

          ev3.speaker.say("I can say anything!")

  * - | 音符を
      | 再生する
    -
    - ::

          ev3.speaker.play_notes(['C4/4', 'G4/4'])

  * - | 指定した位置に
      | テキストを
      | 書き込む
    - ::

          brick.display.text("Hello!", (50, 60))
    - ::

          ev3.screen.draw_text(50, 60, "Hello!")

  * - | テキストを書き込んで
      | 自動で
      | スクロールする
    - ::

          brick.display.text("Hello")
          brick.display.text("world!")
    - ::

          ev3.screen.print("Hello")
          ev3.screen.print("world!")

  * - | フォントサイズを
      | 変更する
    -
    - ::

          from pybricks.media.ev3dev import Font

          big_font = Font(size=24)
          ev3.screen.set_font(big_font)

  * - | 画面に画像を
      | 表示する
    - ::

          from pybricks.parameters import ImageFile

          brick.display.image(ImageFile.QUESTION_MARK)
    - ::

          from pybricks.media.ev3dev import ImageFile

          ev3.screen.load_image(ImageFile.Question_MARK)

  * - | 画面に図形を
      | 描画する
    -
    - ::

          ev3.screen.draw_line(30, 30, 30, 100)
          ev3.screen.draw_box(50, 30, 90, 60)
          ev3.screen.draw_circle(70, 90, 20, fill=True)

  * - | バッテリー
      | 電圧を
      | 読み取る
    - ::

          brick.battery.voltage()
    - ::

          ev3.battery.voltage()


既存機能のその他の内部変更
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- :class:`Motor() <pybricks.ev3devices.Motor>` クラスのほとんどの
  メソッドで、デフォルトが ``Stop.COAST`` ではなく ``Stop.HOLD`` に
  なりました。これにより多くの用途で精度が向上します。必要であれば
  引き続き ``Stop.COAST`` を選択できます。
- モーターの内部PIDコントローラーが以前より正確になりました。
  動作中のモーターにコマンドを送ると、新しいコマンドに合わせて速度が
  スムーズに調整されます。高速ループで速度を調整し続けても
  正しく動作します。
- モーター設定を構成するメソッドが変更されました。現在は
  :doc:`control <motors>` 属性を使って設定を変更できます。
  古い設定用セッターは実装上は残っていますが、ドキュメント化は
  されていません。
- いわゆるPythonの *キーワード引数* がサポートされるようになりました。
  以前は引数の *値* しか入力できませんでした。例:

   ::

       my_motor.run_angle(500, 90, Stop.HOLD, False)

  この書き方は引き続き使えます。ただし、任意の引数を省略し、
  他の引数を *キーワード* で指定できるようになりました。これにより
  コードが読みやすくなります。例:

   ::

      my_motor.run_angle(500, 90, wait=False)
- ``pybricks.tools.print`` をインポートする必要はなくなりました。
  ``print`` 関数が組み込みになり、PythonやMicroPythonと同じように
  動作します。
- :mod:`parameters <pybricks.parameters>` のほとんどのパラメーターに、
  固有の型と表現が付きました。たとえば、色を測定して結果を表示すると
  します。 ``print(Color.RED)`` とすると、内部的な数値ではなく
  パラメーター名が表示されます。
- サウンドと画像ファイルは専用の :doc:`media <media>` モジュールに
  移動しました。
  このリリースでは、既存のスクリプトが引き続き動作するよう、
  古い場所からのインポートも引き続き機能します。

**古いバージョンのVisual Studio Code拡張機能をインストールする**

Visual Studio Code拡張機能とこのドキュメントは自動的に更新されます。
更新された拡張機能でも既存のスクリプトは引き続き使えます。
どうしても古いバージョンを使い続けたい場合は、拡張機能タブで
EV3拡張機能を探し、歯車アイコンをクリックして
*install another version* をクリックしてください。
