# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2022 The Pybricks Authors

"""LEGO® MINDSTORMS® EV3 のモーターとセンサー。"""

from .parameters import Direction as _Direction
from ._common import DCMotor as _DCMotor, Motor as _Motor


class DCMotor(_DCMotor):
    pass


class Motor(_Motor):
    pass


class TouchSensor:
    """LEGO® MINDSTORMS® EV3 Touch Sensor."""

    def __init__(self, port):
        """TouchSensor(port)

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


class ColorSensor:
    """LEGO® MINDSTORMS® EV3 Color Sensor."""

    def __init__(self, port):
        """ColorSensor(port)

        Arguments:
            port (Port): センサーを接続するポート。

        """
        pass

    def color(self):
        """表面の色を測定します。

        :returns:
            ``Color.BLACK``, ``Color.BLUE``, ``Color.GREEN``, ``Color.YELLOW``,
            ``Color.RED``, ``Color.WHITE``, ``Color.BROWN`` または ``None`` 。
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
        """赤い光を使って表面の反射率を測定します。

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


class InfraredSensor:
    """LEGO® MINDSTORMS® EV3 赤外線センサーとビーコン。"""

    def __init__(self, port):
        """InfraredSensor(port)

        Arguments:
            port (Port): センサーを接続するポート。

        """
        pass

    def distance(self):
        """赤外線を使って、センサーと物体との相対的な距離を測定します。

        Returns:
            :ref:`relativedistance`: 相対距離。0(最も近い)から100(最も遠い)
            の範囲。

        """
        pass

    def beacon(self, channel):
        """リモコンと赤外線センサーとの相対的な距離と角度を測定します。

        Arguments:
            channel (int): リモコンのチャンネル番号。

        :returns: リモコンと赤外線センサーとの相対距離(0から100)と
                  おおよその角度(-75から75度)のタプル。
        :rtype: (:ref:`relativedistance`, :ref:`angle`)。リモコンが検出
                されない場合は (``None``, ``None``) 。
        """
        pass

    def buttons(self, channel):
        """赤外線リモコンのどのボタンが押されているかを確認します。

        このメソッドは一度に最大2つのボタンを検出できます。それ以上の
        ボタンを押すと、有効なデータが得られない場合があります。

        Arguments:
            channel (int): リモコンのチャンネル番号。

        :returns: 選択したチャンネルのリモコンで押されているボタンのリスト。
        :rtype: List of :class:`Button <.parameters.Button>`

        """
        pass

    def keypad(self):
        """赤外線リモコンのどのボタンが押されているかを確認します。

        このメソッドは4つの上下ボタンをすべて個別に検出できますが、
        ビーコンボタンは検出できません。

        このメソッドはチャンネル1のリモコンでのみ動作します。

        :returns: 選択したチャンネルのリモコンで押されているボタンのリスト。
        :rtype: List of :class:`Button <.parameters.Button>`

        """
        pass


class GyroSensor:
    """LEGO® MINDSTORMS® EV3 Gyro Sensor."""

    def __init__(self, port, positive_direction=_Direction.CLOCKWISE):
        """

        Arguments:
            port (Port): センサーを接続するポート。
            positive_direction (Direction):
                センサー上部の赤い点を見たときの正の回転方向。

        """
        pass

    def speed(self):
        """センサーの速度(角速度)を取得します。

        Returns:
            :ref:`speed`: センサーの角速度。

        """
        pass

    def angle(self):
        """センサーの累積角度を取得します。

        Returns:
            :ref:`angle`: 回転角度。

        """
        pass

    def reset_angle(self, angle):
        """センサーの回転角度を任意の値に設定します。

        Arguments:
            angle (:ref:`angle`): 角度をリセットする値。
        """
        pass

    def _calibrate(self):
        """センサーをキャリブレーションします。

        この処理は速度と角度を0に設定し、角度値がドリフトしないように
        します。

        キャリブレーション中はセンサーを動かさないでください。

        この処理には最大15秒かかります。
        """
        pass


class UltrasonicSensor:
    """LEGO® MINDSTORMS® EV3 Ultrasonic Sensor."""

    def __init__(self, port):
        """UltrasonicSensor(port)

        Arguments:
            port (Port): センサーを接続するポート。

        """
        pass

    def distance(self, silent=False):
        """超音波を使って、センサーと物体との距離を測定します。

        Arguments:
            silent (bool): ``True`` を選ぶと、距離の測定後にセンサーを
                           オフにします。他の超音波センサーとの干渉を
                           減らせます。ただし頻繁に行いすぎるとセンサーが
                           フリーズすることがあります。その場合は一度
                           抜いて差し直してください。

        Returns:
            :ref:`distance`: 距離。

        """
        pass

    def presence(self):
        """超音波を検出することで、他の超音波センサーの存在を確認します。

        他の超音波センサーがサイレントモードで動作している場合、その
        センサーが測定を行っている間だけ存在を検出できます。

        Returns:
            bool: 超音波が検出された場合は ``True`` 、そうでない場合は
            ``False`` 。
        """
        pass
