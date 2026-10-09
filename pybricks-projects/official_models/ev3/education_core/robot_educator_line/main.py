#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Color Sensor Down Program
----------------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""

from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# モーターを初期化します。
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# カラーセンサーを初期化します。
line_sensor = ColorSensor(Port.S3)

# ドライブベースを初期化します。
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# 光のしきい値を計算します。実際の測定値に合わせて値を選んでください。
BLACK = 9
WHITE = 85
threshold = (BLACK + WHITE) / 2

# 走行速度を毎秒100ミリメートルに設定します。
DRIVE_SPEED = 100

# 比例ライントレース制御のゲインを設定します。これは、光の値が
# しきい値から1%ずれるごとに、ドライブベースの旋回速度を
# 毎秒1.2度に設定するという意味です。

# 例えば、光の値がしきい値から10ずれた場合、ロボットは
# 10*1.2 = 毎秒12度で旋回します。
PROPORTIONAL_GAIN = 1.2

# ラインのトレースをずっと続けます。
while True:
    # しきい値からのずれを計算します。
    deviation = line_sensor.reflection() - threshold

    # 旋回速度を計算します。
    turn_rate = PROPORTIONAL_GAIN * deviation

    # ドライブベースの速度と旋回速度を設定します。
    robot.drive(DRIVE_SPEED, turn_rate)

    # このループ内では、少し待機したり他の処理をしたりできます。
    wait(10)
