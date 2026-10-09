#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Elephant Program
----------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#building-expansion
"""

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor
from pybricks.parameters import Port, Direction, Color, Button
from pybricks.tools import wait, StopWatch
from pybricks.media.ev3dev import SoundFile

# EV3 Brickを初期化します。
ev3 = EV3Brick()

# 4本の脚すべてを動かす脚モーターを設定します。正の速度値で
# 脚が前に動くように、モーターの回転方向を
# 反時計回りに設定します。
legs_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)

# 鼻のモーターを設定します。正の速度値で鼻が
# 上に動くように、モーターの回転方向を反時計回りに
# 設定します。
trunk_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)

# 首のモーターをデフォルト設定で設定します。
neck_motor = Motor(Port.D)

# タッチセンサーをセットアップします。鼻が最大位置まで
# 動いたことを検出するために使います。
touch_sensor = TouchSensor(Port.S1)

# カラーセンサーをセットアップします。首が最大位置まで動いたときに
# 赤いビームを検出するために使います。
color_sensor = ColorSensor(Port.S4)

# タイマーをセットアップします。1秒後に入力ループを抜けるために使います。
timer = StopWatch()


def reset():
    # この関数はモデルを休息位置に戻します。

    # 赤いビームが検出されるまで首のモーターを動かします。
    neck_motor.run(750)
    while color_sensor.color() != Color.RED:
        wait(10)
    neck_motor.brake()

    # タッチセンサーが押されるまで鼻のモーターを動かします。
    trunk_motor.run(600)
    while not touch_sensor.pressed():
        wait(10)
    trunk_motor.brake()

    # 音を鳴らします。
    ev3.speaker.play_file(SoundFile.ELEPHANT_CALL)

    # 首と鼻のモーターを休息位置まで動かします。
    neck_motor.run_angle(-600, 700, wait=False)
    trunk_motor.run_angle(-900, 750)
    wait(0.2)

    # 首と鼻のモーターの角度を「0」にリセットします。つまり、
    # 後で「0」まで回転させると、休息位置に
    # 戻ることになります。
    neck_motor.reset_angle(0)
    trunk_motor.reset_angle(0)


def grab():
    # この関数はオブジェクトをつかんで持ち上げます。

    # モデルを休息位置に戻します。
    reset()

    # 首と鼻のモーターを使った一連の動作を実行して、
    # オブジェクトをつかんで持ち上げます。
    trunk_motor.run_angle(1000, 300, wait=False)
    neck_motor.run_angle(1500, 350)
    neck_motor.run_angle(-750, 350)
    neck_motor.run_time(-150, 1000, wait=False)
    trunk_motor.run_angle(-700, 500)
    trunk_motor.run_angle(-300, 300, wait=False)
    neck_motor.run_angle(450, 400)


# モデルを休息位置に戻します。
reset()

# プログラムのメイン部分です。無限に繰り返す
# ループです。
#
# まず、タイマーとsteps変数をリセットします。
# 次に、Brick Buttonsを押して送られるコマンドを待ちます。
# 最後に、steps変数が「0」でなければ脚モーターを動かします。
#
# 処理が最初に戻るので、新しいコマンドを受け付けられます。
while True:

    # タイマーとsteps変数をリセットします。
    timer.reset()
    steps = 0

    # いずれかのBrick Buttonが押されるまで待ちます。
    while not any(ev3.buttons.pressed()):
        wait(10)

    # Brick Buttonの押下に応答します。
    while timer.time() < 1000:
        # Up Buttonが押されているか確認し、押されていれば
        # steps変数を1増やします。
        if Button.UP in ev3.buttons.pressed():
            steps += 1

            # 複数のコマンドを入力できるようタイマーをリセットします。
            timer.reset()
            ev3.speaker.beep(600)

            # 同じコマンドを再登録しないよう、
            # Up Buttonが離されるまで待ってから続行します。
            while Button.UP in ev3.buttons.pressed():
                wait(10)

        # Down Buttonが押されているか確認し、押されていれば
        # steps変数を1減やします。
        if Button.DOWN in ev3.buttons.pressed():
            steps -= 1

            # 複数のコマンドを入力できるようタイマーをリセットします。
            timer.reset()
            ev3.speaker.beep(1200)

            # 同じコマンドを再登録しないよう、
            # Down Buttonが離されるまで待ってから続行します。
            while Button.DOWN in ev3.buttons.pressed():
                wait(10)

        # 鼻を上げて吠えます。
        if Button.LEFT in ev3.buttons.pressed():
            trunk_motor.run(300)
            while not touch_sensor.pressed():
                wait(10)
            trunk_motor.run_angle(-100, 30)
            reset()

        # オブジェクトをつかみます。
        if Button.RIGHT in ev3.buttons.pressed():
            grab()

        # 音を鳴らします。
        if Button.CENTER in ev3.buttons.pressed():
            ev3.speaker.play_file(SoundFile.ELEPHANT_CALL)

    # steps変数が「0」でないか確認します。
    if steps != 0:
        # stepsの数だけ脚モーターを動かします。1ステップごとに
        # モーターは900度回転します。
        angle = 900 * steps
        legs_motor.run_angle(1000, angle)
