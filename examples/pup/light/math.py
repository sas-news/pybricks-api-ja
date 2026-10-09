from pybricks.parameters import Port
from pybricks.pupdevices import Light
from pybricks.tools import StopWatch, wait
from umath import cos, pi

# ライトとStopWatchを初期化する。
light = Light(Port.A)
watch = StopWatch()

# コサイン波のパラメータ。
PERIOD = 2000
MAX = 100

# 明るさをだんだん変化させる。
while True:
    # コサイン波の位相を取得する。
    phase = watch.time() / PERIOD * 2 * pi

    # 明るさを計算する。
    brightness = (0.5 - 0.5 * cos(phase)) * MAX

    # ライトの明るさを設定して少し待つ。
    light.on(brightness)
    wait(10)
