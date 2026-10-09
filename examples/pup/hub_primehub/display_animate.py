from pybricks.hubs import PrimeHub
from pybricks.parameters import Icon
from pybricks.tools import wait

# ハブを初期化する。
hub = PrimeHub()

# ハブのライトを消す(任意)。
hub.light.off()

# 0から100まで行って戻る明るさのリストを作る。
brightness = list(range(0, 100, 4)) + list(range(100, 0, -4))

# 明るさが変わるハートアイコンのアニメーションを作る。
hub.display.animate([Icon.HEART * i / 100 for i in brightness], 30)

# アニメーションはバックグラウンドで繰り返される。ここでは待つだけ。
while True:
    wait(100)
