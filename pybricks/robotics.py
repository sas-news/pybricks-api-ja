# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2020 The Pybricks Authors

"""Pybricks APIのロボティクスモジュール。"""

from ._common import Control as _Control


class DriveBase:
    """2つの動力付きホイールと、オプションの補助輪またはキャスターを持つ
    ロボット車両です。

    ロボットの寸法を指定することで、このクラスはミリメートル単位の
    指定距離だけ走行したり、指定した角度だけ旋回したりする操作を
    簡単に行えます。

    **正** の距離と走行速度は **前進** を意味します。
    **負** は **後進** を意味します。

    **正** の角度と旋回速度は **右** への旋回を意味します。
    **負** は **左** を意味します。つまり、上から見たときに
    正は時計回り、負は反時計回りです。

    """

    distance_control = _Control()
    """走行距離と走行速度はPIDコントローラーで制御されます。
    この属性を使用して設定を変更できます。
    利用可能なメソッドの概要は :ref:`control` を参照してください。"""

    heading_control = _Control()
    """ロボットの旋回角度と旋回速度はPIDコントローラーで制御されます。
    この属性を使用して設定を変更できます。
    利用可能なメソッドの概要は :ref:`control` を参照してください。"""

    def __init__(self, left_motor, right_motor, wheel_diameter, axle_track):
        """DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

        Arguments:
            left_motor (Motor):
                左のホイールを駆動するモーター。
            right_motor (Motor):
                右のホイールを駆動するモーター。
            wheel_diameter (:ref:`dimension`): ホイールの直径。
            axle_track (:ref:`dimension`): 両方のホイールが地面に接する
                点同士の距離。
        """

    def drive(self, drive_speed, turn_rate):
        """指定した速度と旋回速度で走行を開始します。どちらの値もロボットの
        ホイール間の中心点で測定されます。

        Arguments:
            drive_speed (:ref:`linspeed`): ロボットの速度。
            turn_rate (:ref:`speed`): ロボットの旋回速度。
        """
        pass

    def stop(self):
        """モーターを空転させてロボットを停止します。"""
        pass

    def distance(self):
        """走行した推定距離を取得します。

        Returns:
            :ref:`distance`: 前回のリセットからの走行距離。
        """
        pass

    def angle(self):
        """ドライブベースの推定回転角度を取得します。

        Returns:
            :ref:`angle`: 前回のリセットからの累積角度。
        """
        pass

    def state(self):
        """ロボットの状態を取得します。

        現在の :meth:`.distance` 、走行速度、
        :meth:`.angle` 、旋回速度を返します。

        :returns: 距離、走行速度、角度、旋回速度
        :rtype: (:ref:`distance`, :ref:`linspeed`, :ref:`angle`, :ref:`speed`)
        """
        pass

    def reset(self):
        """推定走行距離と角度を0にリセットします。"""
        pass

    def settings(self, straight_speed, straight_acceleration, turn_rate,
                 turn_acceleration):
        """:meth:`.straight` と :meth:`.turn` で使用する速度と加速度を
        設定します。

        引数が指定されない場合は、現在の値をタプルで返します。

        設定はロボットが停止しているときにのみ変更できます。
        つまり走行を開始する前か、 :meth:`.stop` を呼び出した後です。

        Arguments:
            straight_speed (:ref:`linspeed`): :meth:`.straight` の間の
                ロボットの速度。
            straight_acceleration (:ref:`linacceleration`):
                :meth:`.straight` の開始時と終了時におけるロボットの
                加速度と減速度。
            turn_rate (:ref:`speed`): :meth:`.turn` の間のロボットの
                旋回速度。
            turn_acceleration (:ref:`acceleration`): :meth:`.turn` の
                開始時と終了時におけるロボットの角加速度と角減速度。
        """
        pass

    def straight(self, distance):
        """指定した距離だけ直進してから停止します。

        Arguments:
            distance (:ref:`distance`): 走行する距離。
        """
        pass

    def turn(self, angle):
        """その場で指定した角度だけ旋回してから停止します。

        Arguments:
            angle (:ref:`angle`): 旋回する角度。
        """
        pass
