from pybricks.parameters import Port
from pybricks.pupdevices import Light
from pybricks.tools import wait

# ライトを初期化する。
light = Light(Port.A)

# ライトをずっと点滅させる。
while True:
    # ライトを100%の明るさで点灯する。
    light.on(100)
    wait(500)

    # ライトを消す。
    light.off()
    wait(500)
