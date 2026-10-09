#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Driving Base Program
-----------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

# EV3 Brickを初期化します。
ev3 = EV3Brick()

# モーターを初期化します。
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# ドライブベースを初期化します。
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# 1メートル前進し、1メートル後退します。
robot.straight(1000)
ev3.speaker.beep()

robot.straight(-1000)
ev3.speaker.beep()

# 時計回りに360度旋回し、元に戻ります。
robot.turn(360)
ev3.speaker.beep()

robot.turn(-360)
ev3.speaker.beep()
