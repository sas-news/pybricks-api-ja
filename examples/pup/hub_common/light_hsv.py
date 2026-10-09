# ThisHub = CityHub TechnicHub PrimeHub EssentialHub
from pybricks.hubs import ThisHub
from pybricks.parameters import Color
from pybricks.tools import wait

# ハブを初期化する。
hub = ThisHub()

# 明るさ30%で色を表示する。
hub.light.on(Color.RED * 0.3)

wait(2000)

# 自分で作った色を使う。
hub.light.on(Color(h=30, s=100, v=50))

wait(2000)

# すべての色を順に試す。
for hue in range(360):
    hub.light.on(Color(hue))
    wait(10)
