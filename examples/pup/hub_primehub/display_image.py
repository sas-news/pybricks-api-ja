from pybricks.hubs import PrimeHub
from pybricks.parameters import Icon
from pybricks.tools import wait

# ハブを初期化する。
hub = PrimeHub()

# 上向きの大きな矢印を表示する。
hub.display.icon(Icon.UP)

# 表示を見られるよう少し待つ。
wait(2000)

# 半分の明るさでハートを表示する。
hub.display.icon(Icon.HEART / 2)

# 表示を見られるよう少し待つ。
wait(2000)
