#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from pybricks.media.ev3dev import Image, ImageFile

# SDカードから画像を読み込むには時間がかかるため、このように
# プログラムの最初で一度だけ読み込むのが最適です:
ev3_img = Image(ImageFile.EV3_ICON)


# EV3を初期化
ev3 = EV3Brick()


# 画像を表示
ev3.screen.load_image(ev3_img)

# 画像を確認するためしばらく待機
wait(5000)
