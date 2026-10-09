# ThisHub = MoveHub CityHub TechnicHub EssentialHub
from pybricks.hubs import ThisHub
from pybricks.parameters import Button, Color
from pybricks.tools import StopWatch, wait

# ハブを初期化する。
hub = ThisHub()

# 停止ボタンを無効にする。
hub.system.set_stop_button(None)

# 5秒間ボタンの状態を調べる。
watch = StopWatch()
while watch.time() < 5000:
    # 押されていたら緑、そうでなければ赤にライトを付ける。
    if hub.buttons.pressed():
        hub.light.on(Color.GREEN)
    else:
        hub.light.on(Color.RED)

# 停止ボタンを再び有効にする。
hub.system.set_stop_button(Button.CENTER)

# これで停止ボタンをいつもどおり押せる。
wait(5000)
