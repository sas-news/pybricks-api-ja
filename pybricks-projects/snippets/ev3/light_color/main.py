#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from pybricks.parameters import Color

# EV3を初期化
ev3 = EV3Brick()

# 赤色でライトを点灯
ev3.light.on(Color.RED)

# 待機
wait(1000)

# ライトを消す
ev3.light.off()
