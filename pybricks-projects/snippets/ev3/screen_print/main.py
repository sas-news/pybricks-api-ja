#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from pybricks.media.ev3dev import Font

# フォントをファイルから読み込むには時間がかかるため、このように
# プログラムの最初で一度だけ読み込むのが最適です:
tiny_font = Font(size=6)
big_font = Font(size=24, bold=True)
chinese_font = Font(size=24, lang='zh-cn')


# EV3を初期化
ev3 = EV3Brick()


# helloと表示
ev3.screen.print('Hello!')

# 小さくhelloと表示
ev3.screen.set_font(tiny_font)
ev3.screen.print('hello')

# 大きくhelloと表示
ev3.screen.set_font(big_font)
ev3.screen.print('HELLO')

# 中国語でhelloと表示
ev3.screen.set_font(chinese_font)
ev3.screen.print('你好')

# スクリーンを確認するためしばらく待機
wait(5000)
