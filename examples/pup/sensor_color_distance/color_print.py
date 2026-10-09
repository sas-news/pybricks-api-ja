from pybricks.parameters import Port
from pybricks.pupdevices import ColorDistanceSensor
from pybricks.tools import wait

# センサーを初期化する。
sensor = ColorDistanceSensor(Port.A)

while True:
    # 色を読み取る。
    color = sensor.color()

    # 測った色をprintする。
    print(color)

    # センサーをあちこち動かして、
    # どのくらい色を検出できるか見てみよう。

    # 値を読み取れるよう少し待つ。
    wait(100)
