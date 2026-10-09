#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.parameters import Button

from menu import wait_for_button

# EV3を初期化します。
ev3 = EV3Brick()

while True:
    # メニューを表示し、ボタンが1つ選択されるまで待ちます。
    button = wait_for_button(ev3)

    # 押されたボタンに応じて、処理を分けられます。

    # このデモでは、ボタンごとに違う音を鳴らします。
    if button == Button.LEFT:
        ev3.speaker.beep(200)
    elif button == Button.RIGHT:
        ev3.speaker.beep(400)
    elif button == Button.UP:
        ev3.speaker.beep(600)
    elif button == Button.DOWN:
        ev3.speaker.beep(800)
    elif button == Button.CENTER:
        ev3.speaker.beep(1000)
