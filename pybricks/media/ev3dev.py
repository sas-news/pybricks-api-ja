# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2020 The Pybricks Authors

"""ev3dev上のPybricks向けの画像とサウンド。"""

from ..parameters import Color as _Color


class Image:
    """グラフィックス画像を表すオブジェクト。画像のメモリ内コピー、
    または画面に表示される画像のいずれかになります。"""

    # Documentation note: This class is also treated as the `screen` object
    # on EV3 so we use |this image| when it would make sense to say "the screen"
    # in that context and it is automatically replaced when the documentation
    # is generated.

    def __init__(self, source, sub=False):
        """
        Arguments:
            source (str or Image):
                画像のソース。

                ``source`` が文字列の場合、その文字列で指定された
                ファイルパスから画像が読み込まれます。 ``.png`` ファイルのみ
                サポートされます。特殊ケースとして、文字列が ``_screen_`` の
                場合、画像は画面に直接描画するように設定されます。

                :class:`Image` が指定された場合、新しいオブジェクトには
                ``source`` 画像オブジェクトのコピーが格納されます。

            sub (bool):
                ``sub`` が ``True`` の場合、この画像オブジェクトは
                ``source`` 画像のサブ画像として動作します（これは ``source``
                の型が :class:`Image` の場合のみ有効で、 ``str`` の場合は
                無効です）。

                ``sub=True`` の場合は、追加のキーワード引数 ``x1``、``y1``、
                ``x2``、``y2`` が必要です。これらはサブ画像の範囲として
                使用される、 ``source`` 画像内の左上と右下の座標を指定します。
        """
        pass

    @property
    def width(self):
        """|this image| の幅をピクセル単位で取得します。"""
        return 0

    @property
    def height(self):
        """|this image| の高さをピクセル単位で取得します。"""
        return 0

    def clear(self):
        """|this image| を消去します。|this image| のすべてのピクセルが
        :attr:`Color.WHITE <pybricks.parameters.Color.WHITE>` に設定されます。
        """
        pass

    def draw_pixel(self, x, y, color=_Color.BLACK):
        """|this image| に1ピクセルを描画します。

        Arguments:
            x (int): ピクセルのX座標。
            y (int): ピクセルのY座標。
            color (Color): ピクセルの色。
        """
        pass

    def draw_line(self, x1, y1, x2, y2, width=1, color=_Color.BLACK):
        """|this image| に線を描画します。

        Arguments:
            x1 (int): 線の開始点のX座標。
            y1 (int): 線の開始点のY座標。
            x2 (int): 線の終了点のX座標。
            y2 (int): 線の終了点のY座標。
            width (int): 線の幅（ピクセル単位）。
            color (Color): 線の色。
        """
        pass

    def draw_box(self, x1, y1, x2, y2, r=0, fill=False, color=_Color.BLACK):
        """|this image| に矩形を描画します。

        Arguments:
            x1 (int): 矩形の左辺のX座標。
            y1 (int): 矩形の上辺のY座標。
            x2 (int): 矩形の右辺のX座標。
            y2 (int): 矩形の下辺のY座標。
            r (int): 矩形の角の半径。
            fill (bool): ``True`` の場合、矩形が ``color`` で塗りつぶされます。
                それ以外の場合は矩形の輪郭のみ描画されます。
            color (Color): 矩形の色。
        """
        pass

    def draw_circle(self, x, y, r, fill=False, color=_Color.BLACK):
        """|this image| に円を描画します。

        Arguments:
            x (int): 円の中心のX座標。
            y (int): 円の中心のY座標。
            r (int): 円の半径。
            fill (bool): ``True`` の場合、円が ``color`` で塗りつぶされます。
                それ以外の場合は円周のみ描画されます。
            color (Color): 円の色。
        """
        pass

    def draw_image(self, x, y, source, transparent=None):
        """|this image| の上に ``source`` 画像を描画します。

        Arguments:
            x (int):
                画像の左端が始まるX座標の値。
            y (int):
                画像の上端が始まるY座標の値。
            source (Image or str):
                ソースの :class:`Image` 。引数が文字列の場合、 ``source``
                画像はファイルから読み込まれます。
            transparent (Color):
                ``image`` 内で透明として扱う色。透明にしない場合は
                ``None`` 。
        """

    def load_image(self, source):
        """|this image| を消去してから、 ``source`` 画像を
        |this image| の中央に描画します。

        Arguments:
            source (Image or str):
                ソースの :class:`Image` 。引数が文字列の場合、 ``source``
                画像はファイルから読み込まれます。
        """

    def draw_text(self, x, y, text, text_color=_Color.BLACK, background_color=None):
        """|this image| にテキストを描画します。

        :meth:`set_font` で直前に設定されたフォントが使われます。
        フォントがまだ設定されていない場合は :data:`Font.DEFAULT` が
        使われます。

        Arguments:
            x (int):
                テキストの左端が始まるX座標の値。
            y (int):
                テキストの上端が始まるY座標の値。
            text (str):
                描画するテキスト。
            text_color (Color):
                テキストの描画に使う色。
            background_color (Color):
                テキストの背後の矩形を塗りつぶす色。背景を透明にする場合は
                ``None`` 。
        """
        pass

    def print(self, *args, sep=' ', end='\n'):
        """|this image| にテキストの行を出力します。

        このメソッドは組み込みの ``print()`` 関数と同じように動作しますが、
        代わりに |this image| に書き込みます。

        フォントは :meth:`set_font` で設定できます。フォントが設定されて
        いない場合は :data:`Font.DEFAULT` が使われます。テキストは常に
        白背景に黒い文字で出力されます。

        組み込みの ``print()`` とは異なり、テキストが |this image| に
        収まらないほど広い場合でも折り返されず、単に切り捨てられます。
        ただしテキストが画像の下端を超える場合は、画像全体が上に
        スクロールし、 |this image| の下部の新しい空白領域にテキストが
        出力されます。

        Arguments:
            * (object):
                出力する0個以上のオブジェクト。
            sep (str):
                出力される各オブジェクトの間に挟まれる区切り文字。
            end (str):
                最後のオブジェクトの後に出力される行末文字。
        """
        pass

    def set_font(self, font):
        """|this image| への書き込みに使うフォントを設定します。

        このフォントは :meth:`draw_text` と :meth:`print` の両方に使われます。

        Arguments:
            font (:class:`Font`):
                使用するフォント。
        """
        pass

    @staticmethod
    def empty(width=178, height=128):
        """empty(width=<screen width>, height=<screen height>)

        新しい空の :class:`Image` オブジェクトを作成します。

        Arguments:
            width (int):
                画像の幅（ピクセル単位）。
            height (int):
                画像の高さ（ピクセル単位）。

        Returns:
            Image:
                すべてのピクセルが :attr:`Color.WHITE
                <pybricks.parameters.Color.WHITE>` に設定された新しい画像。

        Raises:
            TypeError:
                ``width`` または ``height`` が数値ではありません。
            ValueError:
                ``width`` または ``height`` が1未満です。
            RuntimeError:
                新しい画像の割り当てに問題がありました。
        """

    def save(self, filename):
        """|this image| を ``.png`` ファイルとして保存します。

        Arguments:
            filename (str):
                保存するファイルのパス。

        Raises:
            TypeError:
                ``filename`` が文字列ではありません。
            OSError:
                ファイルの保存に問題がありました。
        """


class Font:
    """テキストの描画に使用するフォントを表すオブジェクトです。"""

    DEFAULT = None  # assigned later since we can't use Font() here
    """既定のフォント。"""

    def __init__(self, family=None, size=12, bold=False, monospace=False,
                 lang=None, script=None):
        """フォントオブジェクトは、指定されたパラメータとインストール済みの
        フォントに基づいて「最も」一致するフォントになります。

        Arguments:
            family (str):
                希望するフォントファミリー。既定値を使う場合は ``None`` 。
            size (int):
                希望するフォントサイズ。ほとんどのフォントは6から24の
                サイズです。これは「ポイント」サイズであり、 :attr:`height`
                とは異なります。
            bold (bool):
                ``True`` の場合、太字フォントを優先します。
            monospace (bool):
                ``True`` の場合、等幅フォントを優先します。
                複数行のテキストを揃えるときに便利です。
            lang (str):
                ``'en'`` や ``'zh-cn'`` のような言語コード。
                既定の言語を使う場合は ``None`` 。[#font_lang]_
            script (str):
                ``'Runr'`` のようなUnicodeのスクリプト識別子、
                または ``None`` 。

        .. [#font_lang]
            .. toggle-header::
                :header: 言語コード

                注: 使用できる言語はインストール済みのフォントに依存します。
                ここにない言語コードも使用可能な場合があり、また記載の
                言語コードでも十分なフォントがない場合があります。

                - ``'aa'``: アファル語
                - ``'af'``: アフリカーンス語
                - ``'an'``: アラゴン語
                - ``'av'``: アヴァル語
                - ``'ay'``: アイマラ語
                - ``'az-az'``: アゼルバイジャン語
                - ``'be'``: ベラルーシ語
                - ``'bg'``: ブルガリア語
                - ``'bi'``: ビスラマ語
                - ``'bm'``: バンバラ語
                - ``'br'``: ブルトン語
                - ``'bs'``: ボスニア語
                - ``'bua'``: ブリヤート語
                - ``'ca'``: カタルーニャ語
                - ``'ce'``: チェチェン語
                - ``'ch'``: チャモロ語
                - ``'co'``: コルシカ語
                - ``'crh'``: クリミア・タタール語
                - ``'cs'``: チェコ語
                - ``'csb'``: カシューブ語
                - ``'cy'``: ウェールズ語
                - ``'da'``: デンマーク語
                - ``'de'``: ドイツ語
                - ``'ee'``: エウェ語
                - ``'el'``: ギリシャ語
                - ``'en'``: 英語
                - ``'eo'``: エスペラント語
                - ``'es'``: スペイン語
                - ``'et'``: エストニア語
                - ``'eu'``: バスク語
                - ``'ff'``: フラ語
                - ``'fi'``: フィンランド語
                - ``'fil'``: フィリピノ語
                - ``'fj'``: フィジー語
                - ``'fo'``: フェロー語
                - ``'fr'``: フランス語
                - ``'fur'``: フリウリ語
                - ``'fy'``: 西フリジア語
                - ``'ga'``: アイルランド語
                - ``'gd'``: ゲール語
                - ``'gl'``: ガリシア語
                - ``'gv'``: マン島語
                - ``'ha'``: ハウサ語
                - ``'haw'``: ハワイ語
                - ``'he'``: ヘブライ語
                - ``'ho'``: ヒリ・モツ語
                - ``'hr'``: クロアチア語
                - ``'hsb'``: 上ソルブ語
                - ``'ht'``: ハイチ語
                - ``'hu'``: ハンガリー語
                - ``'ia'``: インターリングア
                - ``'id'``: インドネシア語
                - ``'ie'``: インターリングエ
                - ``'ik'``: イヌピアック語
                - ``'io'``: イド語
                - ``'is'``: アイスランド語
                - ``'it'``: イタリア語
                - ``'ja'``: 日本語
                - ``'jv'``: ジャワ語
                - ``'ki'``: キクユ語
                - ``'kj'``: クワニャマ語
                - ``'kl'``: カラーリット語
                - ``'ko'``: 韓国語
                - ``'ku-tr'``: クルド語
                - ``'kum'``: クムク語
                - ``'kw'``: コーンウォール語
                - ``'kwm'``: クワンビ語
                - ``'la'``: ラテン語
                - ``'lb'``: ルクセンブルク語
                - ``'lez'``: レズギ語
                - ``'lg'``: ガンダ語
                - ``'li'``: リンブルグ語
                - ``'ln'``: リンガラ語
                - ``'lt'``: リトアニア語
                - ``'lv'``: ラトビア語
                - ``'mg'``: マダガスカル語
                - ``'mh'``: マーシャル語
                - ``'mi'``: マオリ語
                - ``'mk'``: マケドニア語
                - ``'mn-mn'``: モンゴル語
                - ``'mo'``: モルドバ語
                - ``'ms'``: マレー語
                - ``'mt'``: マルタ語
                - ``'na'``: ナウル語
                - ``'nb'``: ノルウェー語（ブークモール）
                - ``'nds'``: 低地ドイツ語
                - ``'ng'``: ンドンガ語
                - ``'nl'``: オランダ語
                - ``'nn'``: ノルウェー語（ニーノシュク）
                - ``'no'``: ノルウェー語
                - ``'nr'``: 南ンデベレ語
                - ``'nso'``: 北ソト語
                - ``'nv'``: ナバホ語
                - ``'ny'``: チェワ語
                - ``'oc'``: オック語
                - ``'om'``: オロモ語
                - ``'os'``: オセット語
                - ``'pap-an'``: パピアメント語（オランダ領アンティル）
                - ``'pap-aw'``: パピアメント語（アルバ）
                - ``'pl'``: ポーランド語
                - ``'pt'``: ポルトガル語
                - ``'qu'``: ケチュア語
                - ``'quz'``: ケチュア語（クスコ）
                - ``'rm'``: ロマンシュ語
                - ``'rn'``: ルンディ語
                - ``'ro'``: ルーマニア語
                - ``'ru'``: ロシア語
                - ``'rw'``: キニアルワンダ語
                - ``'sc'``: サルデーニャ語
                - ``'sco'``: スコットランド語
                - ``'se'``: 北部サーミ語
                - ``'sel'``: セリクプ語
                - ``'sg'``: サンゴ語
                - ``'sk'``: スロバキア語
                - ``'sl'``: スロベニア語
                - ``'sm'``: サモア語
                - ``'sma'``: 南部サーミ語
                - ``'smj'``: ルレ・サーミ語
                - ``'smn'``: イナリ・サーミ語
                - ``'sms'``: スコルト・サーミ語
                - ``'sn'``: ショナ語
                - ``'so'``: ソマリ語
                - ``'sq'``: アルバニア語
                - ``'sr'``: セルビア語
                - ``'ss'``: スワティ語
                - ``'st'``: 南ソト語
                - ``'su'``: スンダ語
                - ``'sv'``: スウェーデン語
                - ``'sw'``: スワヒリ語
                - ``'tk'``: トルクメン語
                - ``'tl'``: タガログ語
                - ``'tn'``: ツワナ語
                - ``'to'``: トンガ語
                - ``'tr'``: トルコ語
                - ``'ts'``: ツォンガ語
                - ``'ty'``: タヒチ語
                - ``'uk'``: ウクライナ語
                - ``'uz'``: ウズベク語
                - ``'vo'``: ヴォラピュク語
                - ``'vot'``: ヴォート語
                - ``'wa'``: ワロン語
                - ``'wen'``: ソルブ語
                - ``'wo'``: ウォロフ語
                - ``'xh'``: コサ語
                - ``'yap'``: ヤップ語
                - ``'yi'``: イディッシュ語
                - ``'za'``: チワン語
                - ``'zh-cn'``: 中国語（中国）
                - ``'zh-sg'``: 中国語（シンガポール）
                - ``'zh-tw'``: 中国語（台湾）
                - ``'zu'``: ズールー語
        """

    @property
    def family(self):
        """フォントのファミリー名を取得します。"""
        return 'Lucida'

    @property
    def style(self):
        """フォントスタイルを表す文字列を取得します。

        "Regular" または "Bold" になります。
        """
        return 'Regular'

    @property
    def width(self):
        """フォントの最も幅の広い文字の幅を取得します。"""
        return 0

    @property
    def height(self):
        """フォントの高さを取得します。"""
        return 0

    def text_width(self, text):
        """このフォントでテキストを描画したときの幅を取得します。

        Arguments:
            text (str):
                テキスト。

        Returns:
            int:
                幅（ピクセル単位）。
        """
        return 0

    def text_height(self, text):
        """このフォントでテキストを描画したときの高さを取得します。

        Arguments:
            text (str):
                テキスト。

        Returns:
            int:
                高さ（ピクセル単位）。
        """
        return 0


Font.DEFAULT = Font('Lucida', 12)


class SoundFile:
    """標準のEV3サウンドへのパス。"""

    _BASE_PATH = '/usr/share/sounds/ev3dev/'
    SHOUTING = _BASE_PATH + 'expressions/shouting.wav'
    CHEERING = _BASE_PATH + 'expressions/cheering.wav'
    CRYING = _BASE_PATH + 'expressions/crying.wav'
    OUCH = _BASE_PATH + 'expressions/ouch.wav'
    LAUGHING_2 = _BASE_PATH + 'expressions/laughing_2.wav'
    SNEEZING = _BASE_PATH + 'expressions/sneezing.wav'
    SMACK = _BASE_PATH + 'expressions/smack.wav'
    BOING = _BASE_PATH + 'expressions/boing.wav'
    BOO = _BASE_PATH + 'expressions/boo.wav'
    UH_OH = _BASE_PATH + 'expressions/uh-oh.wav'
    SNORING = _BASE_PATH + 'expressions/snoring.wav'
    KUNG_FU = _BASE_PATH + 'expressions/kung_fu.wav'
    FANFARE = _BASE_PATH + 'expressions/fanfare.wav'
    CRUNCHING = _BASE_PATH + 'expressions/crunching.wav'
    MAGIC_WAND = _BASE_PATH + 'expressions/magic_wand.wav'
    LAUGHING_1 = _BASE_PATH + 'expressions/laughing_1.wav'
    LEFT = _BASE_PATH + 'information/left.wav'
    BACKWARDS = _BASE_PATH + 'information/backwards.wav'
    RIGHT = _BASE_PATH + 'information/right.wav'
    OBJECT = _BASE_PATH + 'information/object.wav'
    COLOR = _BASE_PATH + 'information/color.wav'
    FLASHING = _BASE_PATH + 'information/flashing.wav'
    ERROR = _BASE_PATH + 'information/error.wav'
    ERROR_ALARM = _BASE_PATH + 'information/error_alarm.wav'
    DOWN = _BASE_PATH + 'information/down.wav'
    FORWARD = _BASE_PATH + 'information/forward.wav'
    ACTIVATE = _BASE_PATH + 'information/activate.wav'
    SEARCHING = _BASE_PATH + 'information/searching.wav'
    TOUCH = _BASE_PATH + 'information/touch.wav'
    UP = _BASE_PATH + 'information/up.wav'
    ANALYZE = _BASE_PATH + 'information/analyze.wav'
    STOP = _BASE_PATH + 'information/stop.wav'
    DETECTED = _BASE_PATH + 'information/detected.wav'
    TURN = _BASE_PATH + 'information/turn.wav'
    START = _BASE_PATH + 'information/start.wav'
    MORNING = _BASE_PATH + 'communication/morning.wav'
    EV3 = _BASE_PATH + 'communication/ev3.wav'
    GO = _BASE_PATH + 'communication/go.wav'
    GOOD_JOB = _BASE_PATH + 'communication/good_job.wav'
    OKEY_DOKEY = _BASE_PATH + 'communication/okey-dokey.wav'
    GOOD = _BASE_PATH + 'communication/good.wav'
    NO = _BASE_PATH + 'communication/no.wav'
    THANK_YOU = _BASE_PATH + 'communication/thank_you.wav'
    YES = _BASE_PATH + 'communication/yes.wav'
    GAME_OVER = _BASE_PATH + 'communication/game_over.wav'
    OKAY = _BASE_PATH + 'communication/okay.wav'
    SORRY = _BASE_PATH + 'communication/sorry.wav'
    BRAVO = _BASE_PATH + 'communication/bravo.wav'
    GOODBYE = _BASE_PATH + 'communication/goodbye.wav'
    HI = _BASE_PATH + 'communication/hi.wav'
    HELLO = _BASE_PATH + 'communication/hello.wav'
    MINDSTORMS = _BASE_PATH + 'communication/mindstorms.wav'
    LEGO = _BASE_PATH + 'communication/lego.wav'
    FANTASTIC = _BASE_PATH + 'communication/fantastic.wav'
    SPEED_IDLE = _BASE_PATH + 'movements/speed_idle.wav'
    SPEED_DOWN = _BASE_PATH + 'movements/speed_down.wav'
    SPEED_UP = _BASE_PATH + 'movements/speed_up.wav'
    BROWN = _BASE_PATH + 'colors/brown.wav'
    GREEN = _BASE_PATH + 'colors/green.wav'
    BLACK = _BASE_PATH + 'colors/black.wav'
    WHITE = _BASE_PATH + 'colors/white.wav'
    RED = _BASE_PATH + 'colors/red.wav'
    BLUE = _BASE_PATH + 'colors/blue.wav'
    YELLOW = _BASE_PATH + 'colors/yellow.wav'
    TICK_TACK = _BASE_PATH + 'mechanical/tick_tack.wav'
    HORN_1 = _BASE_PATH + 'mechanical/horn_1.wav'
    BACKING_ALERT = _BASE_PATH + 'mechanical/backing_alert.wav'
    MOTOR_IDLE = _BASE_PATH + 'mechanical/motor_idle.wav'
    AIR_RELEASE = _BASE_PATH + 'mechanical/air_release.wav'
    AIRBRAKE = _BASE_PATH + 'mechanical/airbrake.wav'
    RATCHET = _BASE_PATH + 'mechanical/ratchet.wav'
    MOTOR_STOP = _BASE_PATH + 'mechanical/motor_stop.wav'
    HORN_2 = _BASE_PATH + 'mechanical/horn_2.wav'
    LASER = _BASE_PATH + 'mechanical/laser.wav'
    SONAR = _BASE_PATH + 'mechanical/sonar.wav'
    MOTOR_START = _BASE_PATH + 'mechanical/motor_start.wav'
    INSECT_BUZZ_2 = _BASE_PATH + 'animals/insect_buzz_2.wav'
    ELEPHANT_CALL = _BASE_PATH + 'animals/elephant_call.wav'
    SNAKE_HISS = _BASE_PATH + 'animals/snake_hiss.wav'
    DOG_BARK_2 = _BASE_PATH + 'animals/dog_bark_2.wav'
    DOG_WHINE = _BASE_PATH + 'animals/dog_whine.wav'
    INSECT_BUZZ_1 = _BASE_PATH + 'animals/insect_buzz_1.wav'
    DOG_SNIFF = _BASE_PATH + 'animals/dog_sniff.wav'
    T_REX_ROAR = _BASE_PATH + 'animals/t-rex_roar.wav'
    INSECT_CHIRP = _BASE_PATH + 'animals/insect_chirp.wav'
    DOG_GROWL = _BASE_PATH + 'animals/dog_growl.wav'
    SNAKE_RATTLE = _BASE_PATH + 'animals/snake_rattle.wav'
    DOG_BARK_1 = _BASE_PATH + 'animals/dog_bark_1.wav'
    CAT_PURR = _BASE_PATH + 'animals/cat_purr.wav'
    EIGHT = _BASE_PATH + 'numbers/eight.wav'
    SEVEN = _BASE_PATH + 'numbers/seven.wav'
    SIX = _BASE_PATH + 'numbers/six.wav'
    FOUR = _BASE_PATH + 'numbers/four.wav'
    TEN = _BASE_PATH + 'numbers/ten.wav'
    ONE = _BASE_PATH + 'numbers/one.wav'
    TWO = _BASE_PATH + 'numbers/two.wav'
    THREE = _BASE_PATH + 'numbers/three.wav'
    ZERO = _BASE_PATH + 'numbers/zero.wav'
    FIVE = _BASE_PATH + 'numbers/five.wav'
    NINE = _BASE_PATH + 'numbers/nine.wav'
    READY = _BASE_PATH + 'system/ready.wav'
    CONFIRM = _BASE_PATH + 'system/confirm.wav'
    GENERAL_ALERT = _BASE_PATH + 'system/general_alert.wav'
    CLICK = _BASE_PATH + 'system/click.wav'
    OVERPOWER = _BASE_PATH + 'system/overpower.wav'


class ImageFile:
    """標準のEV3画像へのパス。"""

    _BASE_PATH = '/usr/share/images/ev3dev/mono/'
    RIGHT = _BASE_PATH + 'information/right.png'
    FORWARD = _BASE_PATH + 'information/forward.png'
    ACCEPT = _BASE_PATH + 'information/accept.png'
    QUESTION_MARK = _BASE_PATH + 'information/question_mark.png'
    STOP_1 = _BASE_PATH + 'information/stop_1.png'
    LEFT = _BASE_PATH + 'information/left.png'
    DECLINE = _BASE_PATH + 'information/decline.png'
    THUMBS_DOWN = _BASE_PATH + 'information/thumbs_down.png'
    BACKWARD = _BASE_PATH + 'information/backward.png'
    NO_GO = _BASE_PATH + 'information/no_go.png'
    WARNING = _BASE_PATH + 'information/warning.png'
    STOP_2 = _BASE_PATH + 'information/stop_2.png'
    THUMBS_UP = _BASE_PATH + 'information/thumbs_up.png'
    EV3 = _BASE_PATH + 'lego/ev3.png'
    EV3_ICON = _BASE_PATH + 'lego/ev3_icon.png'
    TARGET = _BASE_PATH + 'objects/target.png'
    BOTTOM_RIGHT = _BASE_PATH + 'eyes/bottom_right.png'
    BOTTOM_LEFT = _BASE_PATH + 'eyes/bottom_left.png'
    EVIL = _BASE_PATH + 'eyes/evil.png'
    CRAZY_2 = _BASE_PATH + 'eyes/crazy_2.png'
    KNOCKED_OUT = _BASE_PATH + 'eyes/knocked_out.png'
    PINCHED_RIGHT = _BASE_PATH + 'eyes/pinched_right.png'
    WINKING = _BASE_PATH + 'eyes/winking.png'
    DIZZY = _BASE_PATH + 'eyes/dizzy.png'
    DOWN = _BASE_PATH + 'eyes/down.png'
    TIRED_MIDDLE = _BASE_PATH + 'eyes/tired_middle.png'
    MIDDLE_RIGHT = _BASE_PATH + 'eyes/middle_right.png'
    SLEEPING = _BASE_PATH + 'eyes/sleeping.png'
    MIDDLE_LEFT = _BASE_PATH + 'eyes/middle_left.png'
    TIRED_RIGHT = _BASE_PATH + 'eyes/tired_right.png'
    PINCHED_LEFT = _BASE_PATH + 'eyes/pinched_left.png'
    PINCHED_MIDDLE = _BASE_PATH + 'eyes/pinched_middle.png'
    CRAZY_1 = _BASE_PATH + 'eyes/crazy_1.png'
    NEUTRAL = _BASE_PATH + 'eyes/neutral.png'
    AWAKE = _BASE_PATH + 'eyes/awake.png'
    UP = _BASE_PATH + 'eyes/up.png'
    TIRED_LEFT = _BASE_PATH + 'eyes/tired_left.png'
    ANGRY = _BASE_PATH + 'eyes/angry.png'
