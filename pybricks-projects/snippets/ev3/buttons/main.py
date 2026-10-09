#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from pybricks.parameters import Button

# EV3を初期化します。
ev3 = EV3Brick()

# いずれかのボタンが押されるまで待ちます
while not any(ev3.buttons.pressed()):
    wait(10)

# 左ボタンが押されたときの処理をします
if Button.LEFT in ev3.buttons.pressed():
    print("The left button is pressed.")

# すべてのボタンが離されるまで待ちます
while any(ev3.buttons.pressed()):
    wait(10)
