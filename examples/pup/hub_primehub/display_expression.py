from pybricks.hubs import PrimeHub
from pybricks.parameters import Icon, Side
from pybricks.tools import wait
from urandom import randint

# ハブを初期化する。
hub = PrimeHub()
hub.display.orientation(up=Side.RIGHT)

while True:
    # 左の眉をランダムに決める: 上か下。
    if randint(0, 100) < 70:
        brows = Icon.EYE_LEFT_BROW * 0.5
    else:
        brows = Icon.EYE_LEFT_BROW_UP * 0.5

    # 右の眉をランダムに追加する: 上か下。
    if randint(0, 100) < 70:
        brows += Icon.EYE_RIGHT_BROW * 0.5
    else:
        brows += Icon.EYE_RIGHT_BROW_UP * 0.5

    for i in range(3):
        # 目を開けた顔にランダムな眉を合わせて表示する。
        hub.display.icon(Icon.EYE_LEFT + Icon.EYE_RIGHT + brows)
        wait(2000)

        # 目を閉じた顔にランダムな眉を合わせて表示する。
        hub.display.icon(Icon.EYE_LEFT_BLINK * 0.7 + Icon.EYE_RIGHT_BLINK * 0.7 + brows)
        wait(200)
