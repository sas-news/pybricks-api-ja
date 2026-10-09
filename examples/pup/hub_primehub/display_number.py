from pybricks.hubs import PrimeHub
from pybricks.tools import wait

# ハブを初期化する。
hub = PrimeHub()

# 0から99までカウントする。
for i in range(100):
    hub.display.number(i)
    wait(200)
