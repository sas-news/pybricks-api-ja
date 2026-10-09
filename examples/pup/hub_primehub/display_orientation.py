from pybricks.hubs import PrimeHub
from pybricks.parameters import Side
from pybricks.tools import wait

# ハブを初期化する。
hub = PrimeHub()

# 表示を回転する。これで右が上になる。
hub.display.orientation(up=Side.RIGHT)

# 数字を表示する。横向きで表示される。
hub.display.number(23)

# 表示を見られるよう少し待つ。
wait(10000)
