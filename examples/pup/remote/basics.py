from pybricks.parameters import Button
from pybricks.pupdevices import Remote
from pybricks.tools import wait

# リモコンに接続する。
my_remote = Remote()

while True:
    # どのボタンが押されているか調べる。
    pressed = my_remote.buttons.pressed()

    # 結果を表示する。
    print("pressed:", pressed)

    # 特定のボタンを調べる。
    if Button.CENTER in pressed:
        print("You pressed the center button!")

    # 結果を見られるよう少し待つ。
    wait(100)
