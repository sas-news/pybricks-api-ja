from pybricks.parameters import Port
from pybricks.pupdevices import UltrasonicSensor
from pybricks.tools import StopWatch, wait
from umath import pi, sin

# センサーを初期化する。
eyes = UltrasonicSensor(Port.A)

# タイマーを初期化する。
watch = StopWatch()

# ライトの1周期を3秒にしたい。
PERIOD = 3000

while True:
    # 位相は単位円の上で今いる位置。
    phase = watch.time() / PERIOD * 2 * pi

    # 各ライトは平均50・振幅50のサイン波に従う。
    # このサイン波をライトごとに90度ずつずらすと、
    # それぞれのライトが違う動きをする。
    brightness = [sin(phase + offset * pi / 2) * 50 + 50 for offset in range(4)]

    # 全ライトの明るさを設定する。
    eyes.lights.on(brightness)

    # 少し待つ。
    wait(50)
