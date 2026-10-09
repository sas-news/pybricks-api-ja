#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Ultrasonic Sensor Driving Base Program
-----------------------------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# EV3 Brickを初期化します。
ev3 = EV3Brick()

# 超音波センサーを初期化します。ロボットが走行中の
# 障害物を検出するために使います。
obstacle_sensor = UltrasonicSensor(Port.S4)

# ポートBとポートCの2つのモーターをデフォルト設定で初期化します。
# これらがドライブベースの左右のモーターになります。
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# DriveBaseは2つのモーターで構成され、各モーターにホイールが付いています。
# wheel_diameterとaxle_trackの値は、走行コマンドを送ったときに
# モーターが正しい速さで動くようにするために使います。
# axle trackとは、左右のホイールが地面に接する点の
# 間の距離です。
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# 走行開始の準備ができたことを音で知らせます
ev3.speaker.beep()

# 次のループは、障害物を検出するまでロボットを前進させます。
# その後バックして向きを変えます。プログラムを停止するまで
# この動作を繰り返します。
while True:
    # 毎秒200ミリメートルの速さで前進を開始します。
    robot.drive(200, 0)

    # 障害物が検出されるまで待ちます。これは、測定した距離が
    # 300mmより大きい間、何もしない(10ミリ秒待つ)ことを
    # 繰り返すことで行います。
    while obstacle_sensor.distance() > 300:
        wait(10)

    # 300ミリメートル後退します。
    robot.straight(-300)

    # 120度旋回して向きを変えます
    robot.turn(120)
