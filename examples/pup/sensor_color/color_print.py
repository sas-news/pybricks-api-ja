from pybricks.parameters import Port
from pybricks.pupdevices import ColorSensor
from pybricks.tools import wait

# センサーを初期化する。
sensor = ColorSensor(Port.A)

while True:
    # 色と反射率を読み取る
    color = sensor.color()
    reflection = sensor.reflection()

    # 測った色と反射率をprintする。
    print(color, reflection)

    # センサーをあちこち動かして、
    # どのくらい色を検出できるか見てみよう。

    # 値を読み取れるよう少し待つ。
    wait(100)
