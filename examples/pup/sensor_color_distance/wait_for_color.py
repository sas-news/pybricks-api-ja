from pybricks.parameters import Color, Port
from pybricks.pupdevices import ColorDistanceSensor
from pybricks.tools import wait

# センサーを初期化する。
sensor = ColorDistanceSensor(Port.A)


# 目的の色になるまで待つ関数。
def wait_for_color(desired_color):
    # 目的の色でない間は待ち続ける。
    while sensor.color() != desired_color:
        wait(20)


# 次に、さきほど作った関数を使う。
while True:
    # ここで列車や車両を前進させられる。

    print("Waiting for red ...")
    wait_for_color(Color.RED)

    # ここで列車や車両を後進させられる。

    print("Waiting for blue ...")
    wait_for_color(Color.BLUE)
