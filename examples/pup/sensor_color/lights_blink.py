from pybricks.parameters import Port
from pybricks.pupdevices import ColorSensor
from pybricks.tools import wait

# センサーを初期化する。
sensor = ColorSensor(Port.A)

# ずっと繰り返す。
while True:
    # ライトを1つずつ半分の明るさで点灯する。
    # 3つのライトすべてにこれを行い、それを5回繰り返す。
    for i in range(5):
        sensor.lights.on([50, 0, 0])
        wait(100)
        sensor.lights.on([0, 50, 0])
        wait(100)
        sensor.lights.on([0, 0, 50])
        wait(100)

    # すべてのライトを最大の明るさで付ける。
    sensor.lights.on(100)
    wait(500)

    # すべてのライトを消す。
    sensor.lights.off()
    wait(500)
