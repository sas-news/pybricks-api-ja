from pybricks.parameters import Color, Port
from pybricks.pupdevices import ColorDistanceSensor
from pybricks.tools import wait

# センサーを初期化する。
sensor = ColorDistanceSensor(Port.A)

# ずっと繰り返す。
while True:
    # 近くに物体を見つけたら、
    if sensor.distance() <= 40:
        # そしてライトを赤/青で5回点滅させる。
        for i in range(5):
            sensor.light.on(Color.RED)
            wait(30)
            sensor.light.on(Color.BLUE)
            wait(30)
    else:
        # 近くに何も見えなければ、
        # 少しだけ待つ。
        wait(10)
