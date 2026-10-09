# ThisHub = MoveHub CityHub TechnicHub PrimeHub EssentialHub
from pybricks.hubs import ThisHub
from pybricks.parameters import Color
from pybricks.tools import wait

# ハブを初期化する。
hub = ThisHub()

# ライトの点灯と消灯を5回繰り返す。
for i in range(5):
    hub.light.on(Color.RED)
    wait(1000)

    hub.light.off()
    wait(500)
