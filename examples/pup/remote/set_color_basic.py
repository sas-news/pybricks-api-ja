from pybricks.parameters import Color
from pybricks.pupdevices import Remote
from pybricks.tools import wait

# リモコンに接続する。
remote = Remote()

while True:
    # 色を赤にする。
    remote.light.on(Color.RED)
    wait(1000)

    # 色を青にする。
    remote.light.on(Color.BLUE)
    wait(1000)
