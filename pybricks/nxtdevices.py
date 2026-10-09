# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2020 The Pybricks Authors

"""LEGO® MINDSTORMS® NXT のモーターとセンサーを EV3 ブロックで使用します。"""


from .iodevices import AnalogSensor as _AnalogSensor
from ._common import ColorLight as _ColorLight


class TouchSensor:
    """LEGO® MINDSTORMS® NXT Touch Sensor."""

    def __init__(self, port):
        """

        Arguments:
            port (Port): センサーを接続するポート。
        """
        pass

    def pressed(self):
        """センサーが押されているかを確認します。

        Returns:
            bool: センサーが押されていれば ``True`` 、押されていなければ
            ``False`` 。

        """
        pass


class LightSensor:
    """LEGO® MINDSTORMS® NXT Color Sensor."""

    def __init__(self, port):
        """

        Arguments:
            port (Port): センサーを接続するポート。

        """
        pass

    def ambient(self):
        """周囲の光の強さを測定します。

        Returns:
            :ref:`percentage`: 周囲の光の強さ。0(暗い)から100(明るい)の範囲。
        """
        pass

    def reflection(self):
        """赤い光を使って表面の反射率を測定します。

        Returns:
            :ref:`percentage`: 反射率。0(反射なし)から100(高い反射)の範囲。

        """
        pass


class ColorSensor:
    """LEGO® MINDSTORMS® NXT Color Sensor."""

    light = _ColorLight()

    def __init__(self, port):
        """

        Arguments:
            port (Port): センサーを接続するポート。

        """
        pass

    def color(self):
        """表面の色を測定します。

        :returns:
            ``Color.BLACK``, ``Color.BLUE``, ``Color.GREEN``, ``Color.YELLOW``,
            ``Color.RED``, ``Color.WHITE`` または ``None`` 。
        :rtype: :class:`Color <.parameters.Color>`。色が検出されない場合は
                ``None`` 。

        """
        pass

    def ambient(self):
        """周囲の光の強さを測定します。

        Returns:
            :ref:`percentage`: 周囲の光の強さ。0(暗い)から100(明るい)の範囲。
        """
        pass

    def reflection(self):
        """表面の反射率を測定します。

        Returns:
            :ref:`percentage`: 反射率。0(反射なし)から100(高い反射)の範囲。

        """
        pass

    def rgb(self):
        """赤・緑・青の順に光を当てて、表面の反射率を測定します。

        :returns: 赤・緑・青それぞれの光に対する反射率のタプル。
                  各値は0.0(反射なし)から100.0(高い反射)の範囲。
        :rtype: (:ref:`percentage`, :ref:`percentage`, :ref:`percentage`)
        """
        pass


class UltrasonicSensor:
    """LEGO® MINDSTORMS® NXT Ultrasonic Sensor."""

    def __init__(self, port):
        """

        Arguments:
            port (Port): センサーを接続するポート。

        """
        pass

    def distance(self):
        """超音波を使って、センサーと物体との距離を測定します。

        Returns:
            :ref:`distance`: 距離。

        """
        pass


class SoundSensor:
    """LEGO® MINDSTORMS® NXT Sound Sensor."""

    def __init__(self, port):
        """

        Arguments:
            port (Port): センサーを接続するポート。

        """
        pass

    def intensity(self, audible_only=True):
        """周囲の音の強さ(音量)を測定します。

        Arguments:
            audible_only (bool): 可聴音のみを検出します。人間の耳に
                聞こえない周波数を除去しようとします。

        Returns:
            :ref:`percentage`: 音の強さ。

        """
        pass


class TemperatureSensor:
    """LEGO® MINDSTORMS® NXT Temperature Sensor."""

    def __init__(self, port):
        """

        Arguments:
            port (Port): センサーを接続するポート。

        """
        pass

    def temperature(self):
        """温度を測定します。

        Returns:
            :ref:`temperature`: 測定された温度。

        """
        pass


class EnergyMeter:
    """LEGO® MINDSTORMS® Education NXT エネルギーメーター。"""

    def __init__(self, port):
        """

        Arguments:
            port (Port): センサーを接続するポート。

        """
        pass

    def storage(self):
        """バッテリーに蓄えられている利用可能な総エネルギーを取得します。

        Returns:
            :ref:`energy`: 残りの蓄積エネルギー。

        """
        pass

    def input(self):
        """エネルギーメーターの入力側(底面)の電気信号を測定します。
        印加される電圧と流れる電流を測定し、この2つの値の積が電力に
        なります。この電力値は蓄積エネルギーが増加する速さです。この電力は、
        付属のソーラーパネルや外部から駆動されるモーターなどのエネルギー源
        から供給されます。

        Returns:
            (:ref:`voltage`, :ref:`current`, :ref:`power`): 入力ポートで
            測定された電圧・電流・電力。

        """
        pass

    def output(self):
        """エネルギーメーターの出力側(上面)の電気信号を測定します。
        外部負荷に印加される電圧と流れる電流を測定し、この2つの値の積が
        電力になります。この電力値は蓄積エネルギーが減少する速さです。
        この電力はライトやモーターなどの負荷によって消費されます。

        Returns:
            (:ref:`voltage`, :ref:`current`, :ref:`power`): 出力ポートで
            測定された電圧・電流・電力。

        """
        pass


class VernierAdapter(_AnalogSensor):
    """LEGO® MINDSTORMS® Education NXT/EV3 Vernierセンサー用アダプター。"""

    def __init__(self, port, conversion=None):
        """

        Arguments:
            port (Port): センサーを接続するポート。
            conversion (callable): :meth:`.conversion` 形式の関数。
                この関数は生のアナログ電圧をセンサー固有の出力値に変換する
                ために使われます。各 Vernier センサーには独自の変換関数が
                あります。下記の例は Surface Temperature Sensor の変換を
                示しています。
        """
        pass

    def voltage(self):
        """センサーの生のアナログ電圧を測定します。

        Returns:
            :ref:`voltage`: アナログ電圧。
        """
        pass

    def conversion(self, voltage):
        """生の電圧(mV)をセンサー値に変換します。

        前もって ``conversion`` 関数を指定していない場合、変換は
        適用されません。

        Arguments:
            voltage (:ref:`voltage`): アナログセンサーの電圧。

        :returns: 変換されたセンサー値。
        :rtype: float
        """
        pass

    def value(self):
        """センサーの :meth:`.voltage` を測定し、指定した
        :meth:`.conversion` を適用してセンサー値を返します。

        :returns: 変換されたセンサー値。
        :rtype: float
        """
        pass
