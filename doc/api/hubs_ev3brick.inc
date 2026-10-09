.. autoclass:: pybricks.hubs.EV3Brick
    :no-members:

    .. rubric:: ボタンを使う

    .. automethod:: pybricks.hubs::EV3Brick.buttons.pressed

    .. rubric:: ブロックのステータスライトを使う

    .. automethod:: pybricks.hubs::EV3Brick.light.on

        .. toggle-header::
            :header: **例を表示/非表示**

            **例: ライトを点灯して色を変えます。**

            .. literalinclude::
              ../../pybricks-projects/snippets/ev3/light_color/main.py

    .. automethod:: pybricks.hubs::EV3Brick.light.off

    .. rubric:: スピーカーを使う

    .. automethod:: pybricks.hubs::EV3Brick.speaker.beep

    .. automethod:: pybricks.hubs::EV3Brick.speaker.play_notes

        .. toggle-header::
            :header: **音符の形式を表示/非表示**

            各音符は以下の形式の文字列です:

                - 最初の文字は音名で、 ``A`` から ``G`` 、または休符を表す
                  ``R`` です。
                - 音名には変化記号 ``#`` (シャープ)または ``b`` (フラット)
                  を付けられます。 ``B#`` / ``Cb`` と ``E#`` / ``Fb`` は
                  使用できません。
                - 音名の後にはオクターブ番号 ``2`` から ``8`` が続きます。
                  例えば ``C4`` は中央のCです。オクターブはCの音で次の番号に
                  切り替わります。例えば ``B3`` は中央のC( ``C4`` )の
                  1つ下の音です。
                - オクターブの後は ``/`` と音符の長さを表す数字が続きます。
                  例えば ``/4`` は4分音符、 ``/8`` は8分音符、という具合です。
                - この後に任意で ``.`` を付けると付点音符になります。
                  付点音符は点のない音符の1.5倍の長さになります。
                - 音符の最後に任意で ``_`` を付けるとタイまたはスラーになり、
                  その音符と次の音符の間に休止が入りません。


    .. automethod:: pybricks.hubs::EV3Brick.speaker.play_file

    .. automethod:: pybricks.hubs::EV3Brick.speaker.say

    .. automethod:: pybricks.hubs::EV3Brick.speaker.set_speech_options

        .. toggle-header::
            :header: **利用可能な言語と音声を表示/非表示**

            以下の言語を選択できます:

                - ``'af'``: アフリカーンス語
                - ``'an'``: アラゴン語
                - ``'bg'``: ブルガリア語
                - ``'bs'``: ボスニア語
                - ``'ca'``: カタルーニャ語
                - ``'cs'``: チェコ語
                - ``'cy'``: ウェールズ語
                - ``'da'``: デンマーク語
                - ``'de'``: ドイツ語
                - ``'el'``: ギリシャ語
                - ``'en'``: 英語(デフォルト)
                - ``'en-gb'``: 英語(イギリス)
                - ``'en-sc'``: 英語(スコットランド)
                - ``'en-uk-north'``: 英語(イギリス、北部)
                - ``'en-uk-rp'``:
                  英語(イギリス、容認発音)
                - ``'en-uk-wmids'``: 英語(イギリス、ウェスト・ミッドランズ)
                - ``'en-us'``: 英語(アメリカ合衆国)
                - ``'en-wi'``: 英語(西インド諸島)
                - ``'eo'``: エスペラント語
                - ``'es'``: スペイン語
                - ``'es-la'``: スペイン語(ラテンアメリカ)
                - ``'et'``: エストニア語
                - ``'fa'``: ペルシャ語
                - ``'fa-pin'``: ペルシャ語(ラテン文字)
                - ``'fi'``: フィンランド語
                - ``'fr-be'``: フランス語(ベルギー)
                - ``'fr-fr'``: フランス語(フランス)
                - ``'ga'``: アイルランド語
                - ``'grc'``: ギリシャ語(古典)
                - ``'hi'``: ヒンディー語
                - ``'hr'``: クロアチア語
                - ``'hu'``: ハンガリー語
                - ``'hy'``: アルメニア語
                - ``'hy-west'``: アルメニア語(西部)
                - ``'id'``: インドネシア語
                - ``'is'``: アイスランド語
                - ``'it'``: イタリア語
                - ``'jbo'``: ロジバン語
                - ``'ka'``: ジョージア語
                - ``'kn'``: カンナダ語
                - ``'ku'``: クルド語
                - ``'la'``: ラテン語
                - ``'lfn'``: リングワ・フランカ・ノバ
                - ``'lt'``: リトアニア語
                - ``'lv'``: ラトビア語
                - ``'mk'``: マケドニア語
                - ``'ml'``: マラヤーラム語
                - ``'ms'``: マレー語
                - ``'ne'``: ネパール語
                - ``'nl'``: オランダ語
                - ``'no'``: ノルウェー語
                - ``'pa'``: パンジャブ語
                - ``'pl'``: ポーランド語
                - ``'pt-br'``: ポルトガル語(ブラジル)
                - ``'pt-pt'``: ポルトガル語(ポルトガル)
                - ``'ro'``: ルーマニア語
                - ``'ru'``: ロシア語
                - ``'sk'``: スロバキア語
                - ``'sq'``: アルバニア語
                - ``'sr'``: セルビア語
                - ``'sv'``: スウェーデン語
                - ``'sw'``: スワヒリ語
                - ``'ta'``: タミル語
                - ``'tr'``: トルコ語
                - ``'vi'``: ベトナム語
                - ``'vi-hue'``: ベトナム語(フエ)
                - ``'vi-sgn'``: ベトナム語(サイゴン)
                - ``'zh'``: 中国語(標準語)
                - ``'zh-yue'``: 中国語(広東語)

                以下の音声を選択できます:

                - ``'f1'``: 女性の声バリエーション1
                - ``'f2'``: 女性の声バリエーション2
                - ``'f3'``: 女性の声バリエーション3
                - ``'f4'``: 女性の声バリエーション4
                - ``'f5'``: 女性の声バリエーション5
                - ``'m1'``: 男性の声バリエーション1
                - ``'m2'``: 男性の声バリエーション2
                - ``'m3'``: 男性の声バリエーション3
                - ``'m4'``: 男性の声バリエーション4
                - ``'m5'``: 男性の声バリエーション5
                - ``'m6'``: 男性の声バリエーション6
                - ``'m7'``: 男性の声バリエーション7
                - ``'croak'``: しわがれ声
                - ``'whisper'``: ささやき声
                - ``'whisperf'``: 女性のささやき声


    .. automethod:: pybricks.hubs::EV3Brick.speaker.set_volume


    .. rubric:: スクリーンを使う

    .. |this image| replace:: the screen

    .. automethod:: pybricks.hubs::EV3Brick.screen.clear

    .. automethod:: pybricks.hubs::EV3Brick.screen.draw_text

    .. automethod:: pybricks.hubs::EV3Brick.screen.print

        .. toggle-header::
            :header: **例を表示/非表示**

            **例: さまざまな方法でhelloと表示します。**

            .. raw:: latex

               \begin{CJK}{UTF8}{gbsn}

            .. literalinclude::
              ../../pybricks-projects/snippets/ev3/screen_print/main.py

            .. raw:: latex

               \end{CJK}

    .. automethod:: pybricks.hubs::EV3Brick.screen.set_font

        **例:** :meth:`print` の例を参照してください。

    .. automethod:: pybricks.hubs::EV3Brick.screen.load_image

        .. toggle-header::
            :header: **例を表示/非表示**

            **例: スクリーンに画像を表示します。**

            .. literalinclude::
              ../../pybricks-projects/snippets/ev3/screen_image/main.py

    .. automethod:: pybricks.hubs::EV3Brick.screen.draw_image

    .. automethod:: pybricks.hubs::EV3Brick.screen.draw_pixel

    .. automethod:: pybricks.hubs::EV3Brick.screen.draw_line

        .. toggle-header::
            :header: **例を表示/非表示**

            **例: スクリーンにいくつかの図形を描画します。**

            .. literalinclude::
              ../../pybricks-projects/snippets/ev3/screen_draw/main.py

    .. automethod:: pybricks.hubs::EV3Brick.screen.draw_box

        **例:** :meth:`draw_line` の例を参照してください。

    .. automethod:: pybricks.hubs::EV3Brick.screen.draw_circle

        **例:** :meth:`draw_line` の例を参照してください。

    .. autoattribute:: pybricks.hubs::EV3Brick.screen.width

    .. autoattribute:: pybricks.hubs::EV3Brick.screen.height

    .. automethod:: pybricks.hubs::EV3Brick.screen.save


    .. rubric:: バッテリーを使う

    .. automethod:: pybricks.hubs::EV3Brick.battery.voltage

    .. automethod:: pybricks.hubs::EV3Brick.battery.current
