# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2020 The Pybricks Authors

"""ライト、ディスプレイ、スピーカー、バッテリーなどの一般的なデバイスのための
汎用クロスプラットフォームモジュール。"""

from .parameters import Direction, Stop


class DCMotor:
    """回転センサーのないシンプルなモーター（トレインモーターなど）を
    制御するための汎用クラス。"""

    def __init__(self, port,
                 positive_direction=Direction.CLOCKWISE):
        """

        Arguments:
            port (Port): モーターが接続されているポート。
            positive_direction (Direction): 正のデューティサイクル値を
                与えたときにモーターが回転する方向。
        """
        pass

    def dc(self, duty):
        """指定したデューティサイクル（「パワー」とも呼ばれます）で
        モーターを回転させます。

        Arguments:
            duty (:ref:`percentage`): デューティサイクル（-100.0から100）。
        """
        pass

    def stop(self):
        """モーターを停止し、自由に回転できる状態にします。

        モーターは摩擦によって徐々に停止します。"""
        pass

    def brake(self):
        """モーターを受動的にブレーキします。

        モーターは摩擦に加えて、まだ動いている間に発生する電圧によって
        停止します。"""
        pass


class Control:
    """PIDコントローラーとその設定を操作するクラス。

        .. data:: scale

            制御対象の整数変数と物理出力との間のスケーリング係数。
            たとえば、単一のモーターの場合、これは回転1度あたりの
            エンコーダーパルス数です。
    """

    def limits(self, speed, acceleration, actuation):
        """最大速度、加速度、駆動出力を設定します。

        引数が指定されない場合は、現在の値を返します。

        Arguments:
            speed (:ref:`speed` or :ref:`linspeed`):
                最大速度。すべての速度コマンドはこの値に制限されます。
            acceleration (:ref:`acceleration` or :ref:`linacceleration`):
                最大加速度。
            actuation (:ref:`percentage`):
                絶対最大値に対する割合で表した最大駆動出力。
        """
        pass

    def pid(self, kp, ki, kd, integral_range, integral_rate, feed_forward):
        """位置制御と速度制御のPID値を取得または設定します。

        引数が指定されない場合は、現在の値を返します。

        Arguments:
            kp (int): 比例位置（または積分速度）制御定数。
            ki (int): 積分位置制御定数。
            kd (int): 微分位置（または比例速度）制御定数。
            integral_range (:ref:`angle` or :ref:`distance`): 積分制御の
                誤差が累積される、目標角度または目標距離の周辺領域。
            integral_rate (:ref:`speed` or :ref:`linspeed`): 誤差積分が
                増加できる最大レート。
            feed_forward (:ref:`percentage`):
                速度リファレンスの方向に、PIDフィードバック信号へ加える
                フィードフォワード信号。この値は絶対最大デューティサイクルに
                対する割合で表されます。
        """
        pass

    def target_tolerances(self, speed, position):
        """動作が完了したとみなす許容誤差を取得または設定します。

        引数が指定されない場合は、現在の値を返します。

        Arguments:
            speed (:ref:`speed` or :ref:`linspeed`): 動作が完了したと
                みなされるまでの、ゼロ速度からの許容偏差。
            position (:ref:`angle` or :ref:`distance`): 動作が完了したと
                みなされるまでの、目標からの許容偏差。
        """
        pass

    def stall_tolerances(self, speed, time):
        """ストール判定の許容値を取得または設定します。

        引数が指定されない場合は、現在の値を返します。

        Arguments:
            speed (:ref:`speed` or :ref:`linspeed`): 最大の駆動出力でも
                ``time`` の間この速度に達しない場合、ストールしたと
                みなされます。
            time (:ref:`time`): コントローラーがこの最小 ``speed`` を
                下回り続けた場合に、ストールしたとみなすまでの時間。
        """
        pass

    def stalled(self):
        """コントローラーが現在ストールしているかどうかを確認します。

        最大の駆動信号を与えても目標速度または目標位置に到達できない場合に、
        コントローラーはストールしているとみなされます。

        Returns:
            bool: コントローラーがストールしていれば ``True`` 、
            そうでなければ ``False`` 。
        """
        pass

    def done(self):
        """進行中のコマンドまたは動作が完了したかどうかを確認します。

        Returns:
            bool: コマンドが完了していれば ``True`` 、そうでなければ
            ``False`` 。
        """
        pass


class Motor(DCMotor):
    """内蔵回転センサー付きモーターを制御するための汎用クラス。"""

    control = Control()
    """モーターは指定した速度と角度の目標を正確に追跡するために PID 制御を
    使用します。モーターの ``control`` 属性でこの動作を変更できます。
    利用可能なメソッドの概要は :ref:`control` を参照してください。"""

    def __init__(self, port,
                 positive_direction=Direction.CLOCKWISE,
                 gears=None):
        """

        Arguments:
            port (Port): モーターを接続するポート。
            positive_direction (Direction): 正の速度値や角度を与えたときに
                モーターが回転する方向。
            gears (list):
                モーターに連結されたギアのリスト。

                例えば ``[12, 36]`` は歯数12と歯数36のギアからなるギア列を
                表します。 ``[[12, 36], [20, 16, 40]]`` のように
                リストのリストを使うと複数のギア列を指定できます。

                ギア列を指定すると、すべてのモーターコマンドと設定は、
                得られるギア比を考慮して自動的に調整されます。
                モーターの回転方向はこれによって変わりません。
        """
        pass

    def angle(self):
        """モーターの回転角度を取得します。

        Returns:
            :ref:`angle`: モーターの角度。

        """
        pass

    def speed(self):
        """モーターの速度を取得します。

        Returns:
            :ref:`speed`: モーターの速度。

        """
        pass

    def reset_angle(self, angle):
        """モーターの累積回転角度を任意の値に設定します。

        Arguments:
            angle (:ref:`angle`): 角度をリセットする値。
        """
        pass

    def hold(self):
        """モーターを停止し、現在の角度に積極的に保持します。"""
        pass

    def run(self, speed):
        """モーターを一定の速度で回転させます。

        モーターは指定した速度まで加速し、新しいコマンドを受け取るまで
        その速度で回転し続けます。

        Arguments:
            speed (:ref:`speed`): モーターの速度。
        """
        pass

    def run_time(self, speed, time, then=Stop.HOLD, wait=True):
        """モーターを一定の速度で、指定した時間だけ回転させます。

        モーターは指定した速度まで加速し、その速度で回転し続けてから
        減速します。一連の動作はちょうど指定した ``time`` の長さになります。

        Arguments:
            speed (:ref:`speed`): モーターの速度。
            time (:ref:`time`): 動作の長さ。
            then (Stop): 停止した後に行う動作。
            wait (bool): プログラムの続きを実行する前に、動作が完了するまで
                         待機します。
        """
        pass

    def run_angle(self, speed, rotation_angle, then=Stop.HOLD, wait=True):
        """モーターを一定の速度で、指定した角度だけ回転させます。

        Arguments:
            speed (:ref:`speed`): モーターの速度。
            rotation_angle (:ref:`angle`): モーターが回転する角度。
            then (Stop): 停止した後に行う動作。
            wait (bool): プログラムの続きを実行する前に、動作が完了するまで
                         待機します。
        """
        pass

    def run_target(self, speed, target_angle, then=Stop.HOLD, wait=True):
        """モーターを一定の速度で、指定した目標角度に向かって回転させます。

        回転方向は目標角度に基づいて自動的に選択されます。 ``speed`` の
        正負は関係ありません。

        Arguments:
            speed (:ref:`speed`): モーターの速度。
            target_angle (:ref:`angle`): モーターが回転して到達する角度。
            then (Stop): 停止した後に行う動作。
            wait (bool): プログラムの続きを実行する前に、モーターが目標に
                         到達するまで待機します。
        """
        pass

    def run_until_stalled(self, speed, then=Stop.COAST, duty_limit=None):
        """モーターがストールするまで一定の速度で回転させます。

        Arguments:
            speed (:ref:`speed`): モーターの速度。
            then (Stop): 停止した後に行う動作。
            duty_limit (:ref:`percentage`): このコマンド実行中のトルク制限。
                ギアやレバーの機構にモーターの最大トルクをかけないように
                するのに便利です。

        Returns:
            :ref:`angle`: モーターがストールした角度。
        """
        pass

    def track_target(self, target_angle):
        """目標角度を追跡します。 :meth:`.run_target` と似ていますが、
        通常の滑らかな加速を行わず、できるだけ速く目標角度に移動します。
        目標角度を連続的に変化させたい場合に便利なメソッドです。

        Arguments:
            target_angle (:ref:`angle`): モーターが回転して到達する
                                         目標角度。

        """
        pass

    def dc(self, duty):
        """指定したデューティサイクル（「パワー」とも呼ばれます）で
        モーターを回転させます。

        このメソッドを使うと、モーターを単純なDCモーターのように使えます。

        Arguments:
            duty (:ref:`percentage`): デューティサイクル（-100.0から100）。
        """


class Speaker:
    """スピーカーでビープ音とサウンドを再生します。"""

    def beep(self, frequency=500, duration=100):
        """ビープ音を再生します。

        Arguments:
            frequency (:ref:`frequency`):
                ビープ音の周波数。100未満の周波数は100として扱われます。
            duration (:ref:`time`):
                ビープ音の長さ。0未満の場合、このメソッドはすぐに戻り、
                音は無限に再生され続けます。
        """
        pass

    def play_notes(self, notes, tempo=120):
        """一連の音符を再生します。

        例えば、次のように演奏できます: ``['C4/4', 'C4/4', 'G4/4', 'G4/4']``.

        Arguments:
            notes (iter):
                再生する音符のシーケンス(下記の形式を参照)。
            tempo (int):
                4分音符を1拍としたときの1分あたりの拍数。
        """
        pass

    def play_file(self, file_name):
        """サウンドファイルを再生します。

        Arguments:
            file_name (str):
                拡張子を含むサウンドファイルへのパス。
        """

        pass

    def say(self, text):
        """指定したテキストを読み上げます。

        :meth:`set_speech_options` でテキストの言語と音声を設定できます。

        Arguments:
            text (str): 読み上げるテキスト。
        """

        pass

    def set_speech_options(self, language=None, voice=None, speed=None, pitch=None):
        """:meth:`say` メソッドで使うスピーチ設定を行います。

        ``None`` に設定されたオプションは変更されません。無効な値が
        設定された場合、 :meth:`say` はデフォルト値を代わりに使用します。

        Arguments:
            language (str):
                テキストの言語。例えば ``'en'`` (英語)や ``'de'`` (ドイツ語)
                を選べます。利用可能な言語の一覧は下記の通りです。
            voice (str):
                使用する音声。例えば ``'f1'`` (女性の声バリエーション1)や
                ``'m3'`` (男性の声バリエーション3)を選べます。
                利用可能な音声の一覧は下記の通りです。
            speed (int):
                1分あたりの単語数。
            pitch (int):
                ピッチ(0から99)。数値が大きいほど高い声に、小さいほど
                低い声になります。
        """
        pass

    def set_volume(self, volume, which='_all_'):
        """スピーカーの音量を設定します。

        Arguments:
            volume (:ref:`percentage`):
                スピーカーの音量。
            which (str):
                設定する音量の対象。 ``'Beep'`` は :meth:`beep` と
                :meth:`play_notes` の音量を設定します。 ``'PCM'`` は
                :meth:`play_file` と :meth:`say` の音量を設定します。
                ``'_all_'`` は両方を同時に設定します。
        """
        pass


class ColorLight:
    """マルチカラーライトを制御します。"""

    def on(self, color):
        """指定した色でライトを点灯します。

        Arguments:
            color (Color): ライトの色。 ``None`` または利用できない色を
                           選ぶとライトは消灯します。
        """
        pass

    def off(self):
        """ライトを消します。"""
        pass

    def rgb(self, red, green, blue):
        """赤・緑・青のライトの明るさを設定します。

        Arguments:
            red (:ref:`brightness`): 赤のライトの明るさ。
            green (:ref:`brightness`): 緑のライトの明るさ。
            blue (:ref:`brightness`): 青のライトの明るさ。
        """
        pass


class KeyPad:
    """キーパッド配置のボタンの状態を取得します。"""

    def pressed(self):
        """現在押されているボタンを確認します。

        :returns: 押されているボタンのリスト。
        :rtype: List of :class:`Button <.parameters.Button>`

        """
        pass


class Battery:
    """バッテリーの状態を取得します。"""

    def voltage(self):
        """バッテリーの電圧を取得します。

        Returns:
            :ref:`voltage`: バッテリーの電圧。
        """
        pass

    def current(self):
        """バッテリーから供給される電流を取得します。

        Returns:
            :ref:`current`: バッテリーの電流。

        """
        pass
