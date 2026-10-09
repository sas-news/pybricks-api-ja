from pybricks.hubs import PrimeHub
from pybricks.parameters import Button

# ハブを初期化する。
hub = PrimeHub()

# 停止ボタンの組み合わせを設定する。これで、
# 中央ボタンとBluetoothボタンの同時押しでプログラムが止まる。
hub.system.set_stop_button((Button.CENTER, Button.BLUETOOTH))

# これで中央ボタンを普通のボタンとして使える。
while True:
    # 中央ボタンが押されたら音を鳴らす。
    if Button.CENTER in hub.buttons.pressed():
        hub.speaker.beep()
