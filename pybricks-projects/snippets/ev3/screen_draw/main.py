#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.tools import wait


# EV3を初期化
ev3 = EV3Brick()


# 長方形を描画
ev3.screen.draw_box(10, 10, 40, 40)

# 塗りつぶした長方形を描画
ev3.screen.draw_box(20, 20, 30, 30, fill=True)

# 角丸の長方形を描画
ev3.screen.draw_box(50, 10, 80, 40, 5)

# 円を描画
ev3.screen.draw_circle(25, 75, 20)

# 線を使って三角形を描画
x1, y1 = 65, 55
x2, y2 = 50, 95
x3, y3 = 80, 95
ev3.screen.draw_line(x1, y1, x2, y2)
ev3.screen.draw_line(x2, y2, x3, y3)
ev3.screen.draw_line(x3, y3, x1, y1)

# 図形を確認するためしばらく待機
wait(5000)
