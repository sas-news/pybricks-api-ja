from pybricks.parameters import Color, Port
from pybricks.pupdevices import ColorSensor
from pybricks.tools import wait

# センサーを初期化する。
sensor = ColorSensor(Port.A)

# まず、検出したい物体を決めて、それぞれのHSV値を測る。
# 前のサンプルで使った hsv() メソッドで測れる。
#
# 測った値でデフォルトの色を上書きしたり、新しい色を追加する:
Color.GREEN = Color(h=132, s=94, v=26)
Color.MAGENTA = Color(h=348, s=96, v=40)
Color.BROWN = Color(h=17, s=78, v=15)
Color.RED = Color(h=359, s=97, v=39)

# 自分の色をリストかタプルに入れる。
my_colors = (Color.GREEN, Color.MAGENTA, Color.BROWN, Color.RED, Color.NONE)

# 色を保存する。
sensor.detectable_colors(my_colors)

# color() はいつもどおり動くが、返るのは指定した色のどれかになる。
while True:
    color = sensor.color()

    # 色をprintする。
    print(color)

    # どの色かを判定する。
    if color == Color.MAGENTA:
        print("It works!")

    # 値を読み取れるよう少し待つ。
    wait(100)
