# ThisHub = MoveHub CityHub TechnicHub PrimeHub EssentialHub
from pybricks.hubs import ThisHub
from pybricks.parameters import Color
from pybricks.tools import wait

# ハブを初期化
hub = ThisHub()

# 赤の点灯と消灯を繰り返し続ける。
hub.light.blink(Color.RED, [500, 500])

wait(10000)

# 緑でゆっくり、つづいて速く点滅し続ける。
hub.light.blink(Color.GREEN, [500, 500, 50, 900])

wait(10000)
