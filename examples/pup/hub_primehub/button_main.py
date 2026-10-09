from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon
from pybricks.tools import wait

# ハブを初期化する。
hub = PrimeHub()

# どれかのボタンが押されるまで待ち、結果を保存する。
pressed = []
while not any(pressed):
    pressed = hub.buttons.pressed()
    wait(10)

# 丸を表示する。
hub.display.icon(Icon.CIRCLE)

# すべてのボタンが離されるまで待つ。
while any(hub.buttons.pressed()):
    wait(10)

# 押されたボタンに対応する矢印を表示する。
if Button.LEFT in pressed:
    hub.display.icon(Icon.ARROW_LEFT_DOWN)
elif Button.RIGHT in pressed:
    hub.display.icon(Icon.ARROW_RIGHT_DOWN)
elif Button.BLUETOOTH in pressed:
    hub.display.icon(Icon.ARROW_RIGHT_UP)

wait(3000)
