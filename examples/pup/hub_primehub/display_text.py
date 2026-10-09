from pybricks.hubs import PrimeHub
from pybricks.tools import wait

# ハブを初期化する。
hub = PrimeHub()

# 文字Aを2秒間表示する。
hub.display.char("A")
wait(2000)

# 文字列を1文字ずつ表示する。
hub.display.text("Hello, world!")
