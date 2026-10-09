from pybricks.parameters import Port
from pybricks.pupdevices import ForceSensor
from pybricks.tools import wait

# センサーを初期化する。
button = ForceSensor(Port.A)

while True:
    # このセンサーから取れる情報をすべて読み取る。
    force = button.force()
    dist = button.distance()
    press = button.pressed()
    touch = button.touched()

    # 値をprintする
    print("Force", force, "Dist:", dist, "Pressed:", press, "Touched:", touch)

    # センサーボタンを押して値がどう変わるか見てみよう。

    # 出力を読み取れるよう少し待つ。
    wait(200)
