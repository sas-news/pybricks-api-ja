#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Tank Bot Program
----------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#building-expansion
"""

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import Port, Direction, Button
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import ImageFile

# EV3 Brickを初期化します。
ev3 = EV3Brick()

# ポートBとCの2つのモーターを設定します。正の速度値で
# ロボットが前進するように、モーターの回転方向を
# 反時計回りに設定します。これらがタンクボットの左右のモーターです。
left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)

# タンクボットのホイール直径は約54mmです。
WHEEL_DIAMETER = 54

# axle trackとは、左右のホイールの中心間の距離です。
# タンクボットでは約200mmです。
AXLE_TRACK = 200

# ドライビングベースは2つのモーターで構成され、各モーターに
# ホイールが付いています。ホイール直径とaxle trackの値は、
# 走行コマンドを送ったときにモーターが正しい速さで動くように使います。
robot = DriveBase(left_motor, right_motor, WHEEL_DIAMETER, AXLE_TRACK)

# ジャイロセンサーをセットアップします。ロボットの角度を測るために使います。
# ケーブル接続時とEV3起動中は、ジャイロセンサーとEV3を
# 動かさないでください。
gyro_sensor = GyroSensor(Port.S4)

# steering変数とovershoot変数を初期化します。
steering = 60
overshoot = 5


def right_angle():
    # この関数はロボットを前進させ、直角に旋回し、再び前進して、
    # 180度旋回して同じ経路を戻り、
    # 最初の位置に戻ります。

    # ジャイロセンサーの角度をリセットします。
    gyro_sensor.reset_angle(0)

    # 750ミリメートル前進します
    robot.straight(750)

    # 角度が90度になるまで時計回りに旋回します。
    robot.drive(0, steering)

    ev3.speaker.beep()

    while gyro_sensor.angle() < 90 - overshoot:
        wait(1)
    robot.drive(0, 0)
    wait(1000)

    # 750ミリメートル前進します
    robot.straight(750)

    # 角度が270度になるまで時計回りに旋回します。
    robot.drive(0, steering)

    ev3.speaker.beep()

    while gyro_sensor.angle() < 270 - overshoot:
        wait(1)
    robot.drive(0, 0)
    wait(1000)

    # 750ミリメートル前進します
    robot.straight(750)

    # 角度が180度になるまで反時計回りに旋回します。
    robot.drive(0, -steering)

    ev3.speaker.beep()

    while gyro_sensor.angle() > 180 + overshoot:
        wait(1)
    robot.drive(0, 0)
    wait(1000)

    # 750ミリメートル前進します
    robot.straight(750)

    # 角度が360度になるまで時計回りに旋回します。
    robot.drive(0, steering)

    ev3.speaker.beep()

    while gyro_sensor.angle() < 360 - overshoot:
        wait(1)
    robot.drive(0, 0)
    wait(1000)


def polygon(sides, length):
    # この関数はロボットを多角形の経路に沿って走らせます。
    # 辺の数から旋回する角度を、長さから直進する時間を
    # 計算します。

    # ジャイロセンサーの角度をリセットします。
    gyro_sensor.reset_angle(0)

    # 旋回する角度と直進する時間を計算します。
    angle = 360 / sides

    # 多角形の経路に沿って走行します。
    for side in range(1, sides + 1):
        target_angle = side * angle - overshoot

        # 前進します。
        robot.straight(length)

        # 角度が目標角度になるまで時計回りに旋回します。
        robot.drive(0, steering)

        ev3.speaker.beep()

        while gyro_sensor.angle() < target_angle - overshoot:
            wait(1)
        robot.drive(0, 0)
        wait(1000)


# プログラムのメイン部分です。無限に繰り返す
# ループです。
#
# まず、いずれかのBrick Buttonが押されるまで待ちます。
# 次に、選ばれたパターンを画面に表示します。
# 最後に、選ばれたパターンで走行します。
#
# 処理が最初に戻るので、別のパターンを選べます。
while True:

    # ロボットが指示待ちであることを示すため、
    # クエスチョンマークを表示します。
    ev3.screen.load_image(ImageFile.QUESTION_MARK)

    # いずれかのBrick Buttonが押されるまで待ちます。
    while not any(ev3.buttons.pressed()):
        wait(10)

    ev3.screen.clear()

    # Brick Buttonの押下に応答します。選ばれたパターンを
    # 画面に表示し、そのパターンで走行します。
    if Button.UP in ev3.buttons.pressed():
        # 直角に走行します。
        ev3.screen.draw_text(30, 50, "Right Angle")
        wait(1000)
        right_angle()

    if Button.LEFT in ev3.buttons.pressed():
        # 三角形に走行します。
        ev3.screen.draw_text(30, 50, "Triangle")
        wait(2000)
        polygon(3, 850)

    if Button.CENTER in ev3.buttons.pressed():
        # 正方形に走行します。
        ev3.screen.draw_text(30, 50, "Square")
        wait(2000)
        polygon(4, 700)

    if Button.RIGHT in ev3.buttons.pressed():
        # 五角形に走行します。
        ev3.screen.draw_text(30, 50, "Pentagon")
        wait(2000)
        polygon(5, 575)

    if Button.DOWN in ev3.buttons.pressed():
        # 六角形に走行します。
        ev3.screen.draw_text(30, 50, "Hexagon")
        wait(2000)
        polygon(6, 490)

    wait(100)
