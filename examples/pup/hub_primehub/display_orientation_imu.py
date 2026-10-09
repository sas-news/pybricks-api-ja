from pybricks.hubs import PrimeHub
from pybricks.parameters import Icon
from pybricks.tools import wait

# ハブを初期化する。
hub = PrimeHub()

while True:
    # ハブのどの面が上を向いているか調べる。
    up_side = hub.imu.up()

    # その面を使って表示の向きを決める。
    hub.display.orientation(up_side)

    # 矢印など、何かを表示する。
    hub.display.icon(Icon.UP)

    wait(10)
