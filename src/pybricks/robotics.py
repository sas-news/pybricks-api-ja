# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2023 The Pybricks Authors

"""Pybricks APIのロボティクスモジュール。"""

from __future__ import annotations

from typing import TYPE_CHECKING, overload

from . import _common
from .parameters import Stop

if TYPE_CHECKING:
    from ._common import MaybeAwaitable, Motor
    from .parameters import Number


class DriveBase:
    """2つの動力付きホイールと、オプションの補助輪またはキャスターを持つ
    ロボット車両です。

    ロボットの寸法を指定することで、このクラスはミリメートル単位の
    指定距離だけ走行したり、指定した角度だけ旋回したりする操作を
    簡単に行えます。

    **正** の距離、半径、走行速度は **前進** を意味します。
    **負** は **後進** を意味します。

    **正** の角度と旋回速度は **右** への旋回を意味します。
    **負** は **左** を意味します。つまり、上から見たときに
    正は時計回り、負は反時計回りです。

    直径と軸距の値を測定・調整するコツは、 `measuring`_ セクションを
    参照してください。
    """

    distance_control = _common.Control()
    """走行距離と走行速度はPIDコントローラーで制御されます。
    この属性を使用して設定を変更できます。利用可能なメソッドの概要は
    :meth:`モーターの制御 <pybricks.pupdevices.Motor.control.limits>` 属性を
    参照してください。 ``distance_control`` 属性は同じ機能を持ちますが、
    設定は1つのモーターが回転した度数ではなく、ドライブベースが
    走行したミリメートルごとに適用されます。"""

    heading_control = _common.Control()
    """ロボットの旋回角度と旋回速度はPIDコントローラーで制御されます。
    この属性を使用して設定を変更できます。利用可能なメソッドの概要は
    :meth:`モーターの制御 <pybricks.pupdevices.Motor.control.limits>` 属性を
    参照してください。 ``heading_control`` 属性は同じ機能を持ちますが、
    設定は1つのモーターが回転した度数ではなく、ドライブベース全体の
    （上から見た）回転角度ごとに適用されます。"""

    def __init__(
        self,
        left_motor: Motor,
        right_motor: Motor,
        wheel_diameter: Number,
        axle_track: Number,
    ):
        """DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

        Arguments:
            left_motor (Motor):
                左のホイールを駆動するモーター。
            right_motor (Motor):
                右のホイールを駆動するモーター。
            wheel_diameter (Number, mm): ホイールの直径。
            axle_track (Number, mm): 両方のホイールが地面に接する
                点同士の距離。
        """

    def drive(self, speed: Number, turn_rate: Number) -> None:
        """drive(speed, turn_rate)

        指定した速度と旋回速度で走行を開始します。どちらの値もロボットの
        ホイール間の中心点で測定されます。

        Arguments:
            speed (Number, mm/s): ロボットの速度。
            turn_rate (Number, deg/s): ロボットの旋回速度。
        """

    def stop(self) -> None:
        """stop()

        モーターを空転させてロボットを停止します。"""

    def brake(self) -> None:
        """brake()

        モーターを受動的にブレーキしてロボットを停止します。
        """

    def hold(self) -> None:
        """hold()

        ロボットを停止し、その場にアクティブに保持します。
        """

    def distance(self) -> int:
        """distance() -> int: mm

        走行した推定距離を取得します。

        Returns:
            前回のリセットからの走行距離。
        """

    def angle(self) -> float:
        """angle() -> float: deg

        ドライブベースの推定回転角度を取得します。

        このドライブベースでジャイロが使用されている場合、これはジャイロの
        角度になります。それ以外の場合は、モーターの変位から推定された
        角度になります。

        Returns:
            前回のリセットからの累積角度。
        """

    def state(self) -> tuple[int, int, int, int]:
        """state() -> tuple[int, int, int, int]

        ロボットの状態を取得します。

        :meth:`.angle` メソッドと同様に、ジャイロが使用されている場合、
        報告される角度と旋回速度はジャイロのものになります。
        それ以外の場合はモーターの変位から推定されます。

        Returns:
            ロボットの距離、走行速度、角度、旋回速度のタプル。
        """

    def reset(self, distance: Number = 0, angle: Number = 0) -> None:
        """reset(distance=0, angle=0)

        推定走行距離と方位角をリセットします。

        これは :meth:`.stop` も呼び出して、進行中の動作を停止します。
        ロボットが :meth:`.use_gyro` を ``True`` に設定して制御されている
        場合、このメソッドを呼び出すとジャイロ `も` 指定された角度に
        設定されます。

        Arguments:
            distance (Number, mm): 走行距離の新しい値。
            angle (Number, deg): ロボットの新しい方位角。
        """

    @overload
    def settings(
        self,
        straight_speed: Number | None = None,
        straight_acceleration: Number | tuple[Number, Number] | None = None,
        turn_rate: Number | None = None,
        turn_acceleration: Number | tuple[Number, Number] | None = None,
    ) -> None: ...

    @overload
    def settings(
        self,
    ) -> tuple[int, int | tuple[int, int], int, int | tuple[int, int]]: ...

    def settings(self, *args):
        """
        settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)
        settings() -> tuple[int, int, int, int]
        settings() -> tuple[int, tuple[int, int], int, tuple[int, int]]

        ドライブベースの速度と加速度を設定します。

        引数を指定しない場合は、現在の値をタプルとして返します。

        初期値はホイール径と軸距に基づいて自動的に設定されます。
        ロボットが最大速度の約40%で走行するように選択されています。

        ここで指定した速度値は :meth:`.drive` メソッドには適用されません。
        そのメソッドでは独自の速度値を引数として指定するためです。

        速度とレートの値は絶対値として扱われます。負の値は自動的に
        正の値に変換されます。

        Arguments:
            straight_speed (Number, mm/s): ロボットの直進速度。
            straight_acceleration (Number or tuple[Number, Number], mm/s²):
                ロボットの直進時の加速度と減速度。単一の値を指定すると
                加速度と減速度が同じになります。2つの値のタプルを
                指定すると個別に設定できます。
            turn_rate (Number, deg/s): ロボットの旋回速度。
            turn_acceleration (Number or tuple[Number, Number], deg/s²):
                ロボットの角加速度と角減速度。単一の値を指定すると
                加速度と減速度が同じになります。2つの値のタプルを
                指定すると個別に設定できます。
        """

    def straight(
        self, distance: Number, then: Stop = Stop.HOLD, wait: bool = True
    ) -> MaybeAwaitable:
        """straight(distance, then=Stop.HOLD, wait=True)

        指定した距離だけ直進してから停止します。

        Arguments:
            distance (Number, mm): 走行する距離。
            then (Stop): 静止した後に何をするか。
            wait (bool): プログラムの残りを続行する前に、動作が完了する
                         まで待機するかどうか。
        """

    def turn(
        self,
        angle: Number,
        then: Stop = Stop.HOLD,
        wait: bool = True,
        absolute: bool = False,
    ) -> MaybeAwaitable:
        """turn(angle, then=Stop.HOLD, wait=True, absolute=False)

        指定した角度だけその場で旋回してから停止します。

        Arguments:
            angle (Number, deg): 旋回する角度。
            then (Stop): 静止した後に何をするか。
            wait (bool): プログラムの残りを続行する前に、動作が完了する
                         まで待機するかどうか。
            absolute (bool): ``False``（デフォルト）の場合、ロボットは現在
                の方位からの相対角度 _だけ_ 旋回します。 ``True`` の場合、
                ロボットは指定された絶対的な方位角まで旋回します。
        """

    def arc(
        self,
        radius: Number,
        angle: Number = None,
        distance: Number = None,
        then: Stop = Stop.HOLD,
        wait: bool = True,
    ) -> MaybeAwaitable:
        """arc(radius, angle=None, distance=None, then=Stop.HOLD, wait=True)

        指定した半径で円弧（円の一部）を描いて走行します。角度または
        距離のどちらかを使って、どれだけ走行するかを指定できます。

        半径が正の場合、ロボットは右側の円に沿って走行します。
        半径が負の場合、ロボットは左側の円に沿って走行します。

        その円に沿ってどれだけ進むかを角度（度）または距離（mm）で
        指定できます。正の値は円に沿った前進を意味します。負の値は
        後退を意味します。

        Arguments:
            radius (Number, mm): 円の半径。
            angle (Number, deg): 円に沿って走行する角度。
            distance (Number, mm): 円に沿って走行する距離。ロボットの
                                   中心で測定します。
            then (Stop): 静止した後に何をするか。
            wait (bool): プログラムの残りを続行する前に、動作が完了する
                         まで待機するかどうか。
        Raises:
            ValueError:
                ``angle`` または ``distance`` のどちらか一方のみを指定する
                必要があり、両方は指定できません。半径を0にすることは
                できません。その場での旋回には :meth:`.turn` を使用して
                ください。
        """

    def done(self) -> bool:
        """done() -> bool

        進行中のコマンドまたは動作が完了したかどうかを確認します。

        Returns:
            コマンドが完了した場合は ``True`` 、そうでない場合は ``False`` 。
        """

    def stalled(self) -> bool:
        """stalled() -> bool

        ドライブベースが現在ストールしているかどうかを確認します。

        最大の駆動信号を使っても目標速度または目標位置に到達できない
        場合、ストールしています。

        Returns:
            ドライブベースがストールしている場合は ``True`` 、そうでない
            場合は ``False`` 。
        """

    def move_by(self, dx: Number, dy: Number, then: Stop = Stop.HOLD) -> MaybeAwaitable:
        """move_by(dx, dy, then=Stop.HOLD)

        ロボットの走行エリア上のX座標とY座標で指定した量だけロボットを
        移動します。X軸はプログラム開始時に前だった方向です。Y軸は
        そこから左に90°の方向です。方位をリセットすることでこれを
        リセットできます。

        ロボットはまず必要な方位へ旋回し、次に直線距離を走行します。
        方位の目標は絶対的なので、結果はロボットの現在の方位に依存
        しません。

        Arguments:
            dx (Number, mm): 走行エリア上のX方向の距離。
            dy (Number, mm): 走行エリア上のY方向の距離。
            then (Stop): 静止した後に何をするか。

        Raises:
            ValueError: いずれかの距離が30 mを超える場合。
        """

    def use_gyro(self, use_gyro: bool) -> None:
        """use_gyro(use_gyro)

        旋回や直進にジャイロセンサーを使用する場合は ``True`` を選択します。
        モーター内蔵の回転センサーのみに依存する場合は ``False`` を
        選択します。

        このメソッドは自動的に :meth:`.stop` を呼び出して、進行中の動作を
        停止します。

        Arguments:
            use_gyro (bool): 有効にする場合は ``True`` 、無効にする場合は
                ``False`` 。
        """


class Car:
    """1つのステアリングモーターと、1つ以上の駆動モーターを持つ車両です。

    このクラスを使用すると、ステアリングモーターが自動的に中心位置を
    見つけます。これにより、どの角度が100%ステアリングに対応するかも
    決定されます。
    """

    def __init__(
        self,
        steer_motor: Motor,
        drive_motors: Motor | tuple[Motor, ...],
        torque_limit: Number = 100,
    ):
        """Car(steer_motor, drive_motors, torque_limit=100)

        Arguments:
            steer_motor (Motor):
                前輪をステアリングするモーター。
            drive_motors (Motor): ホイールを駆動するモーター。複数の
                モーターにはタプルを使用します。
            torque_limit (Number, %): ステアリング機構の端点を見つける
                ために使用する最大トルク制限。ステアリングモーターの
                最大トルクに対する割合です。
        """

    def steer(self, percentage: Number) -> None:
        """steer(percentage)

        前輪を指定した量だけステアリングします。100%ステアリングの場合、
        初期化時に決定された角度だけ右へステアリングします。-100%
        ステアリングの場合は左へ、0%は直進を意味します。

        Arguments:
            percentage (Number, %): 前輪をステアリングする量。
        """

    def drive_power(self, power: Number) -> None:
        """drive_power(power)

        指定したパワーレベルで車を走行させます。正の値は前進、負の値は
        後進します。

        ``power`` の値は、バッテリー電圧に対する割合としてモーター電圧を
        設定するために使用されます。10%未満では、急ブレーキではなく
        スムーズに転がり続けるよう、車はホイールを空転させます。

        このコマンドは、ボタン押下やジョイスティック操作に即座に
        反応させたいリモートコントロール用途に便利です。

        Arguments:
            power (Number, %): 車のパワー。
        """

    def drive_speed(self, speed: Number) -> None:
        """drive_speed(speed)

        指定したモーター速度で車を走行させます。正の値は前進、負の値は
        後進します。

        このコマンドは、穏やかな加減速によるより精密な走行に便利です。
        障害物を越えて走行する際に速度を維持するため、自動的に
        パワーが上がります。

        Arguments:
            speed (Number, deg/s): 駆動モーターの角速度。
        """


# Hide type-only names from jedi completions in the module namespace.
if TYPE_CHECKING:
    del MaybeAwaitable
    del Motor
    del Number
    del Stop
