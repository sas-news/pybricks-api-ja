from pybricks.hubs import PrimeHub
from pybricks.tools import wait

# ハブを初期化する。
hub = PrimeHub()

# 1行2列目のピクセルを点灯する。
hub.display.pixel(1, 2)
wait(2000)

# 2行4列目のピクセルを50%の明るさで点灯する。
hub.display.pixel(2, 4, 50)
wait(2000)

# 1行2列目のピクセルを消す。
hub.display.pixel(1, 2, 0)
wait(2000)
