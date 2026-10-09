# ThisHub = CityHub TechnicHub PrimeHub EssentialHub
from pybricks.hubs import ThisHub
from pybricks.parameters import Color
from pybricks.tools import wait
from umath import pi, sin

# ハブを初期化する。
hub = ThisHub()

# 複数色のアニメーションを作る。
hub.light.animate([Color.RED, Color.GREEN, Color.NONE], interval=500)

wait(10000)

# サイン波パターンで赤色を明滅させる。
hub.light.animate([Color.RED * (0.5 * sin(i / 15 * pi) + 0.5) for i in range(30)], 40)

wait(10000)

# 虹色を順番に切り替える。
hub.light.animate([Color(h=i * 8) for i in range(45)], interval=40)

wait(10000)
