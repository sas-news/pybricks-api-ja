from pybricks.parameters import Port
from pybricks.pupdevices import InfraredSensor
from pybricks.tools import wait

# センサーを初期化する。
ir = InfraredSensor(Port.A)

while True:
    # このセンサーから取れる情報をすべて読み取る。
    dist = ir.distance()
    count = ir.count()
    ref = ir.reflection()

    # 値をprintする
    print("Distance:", dist, "Count:", count, "Reflection:", ref)

    # センサーを動かしたり手をかざしたりして、
    # 値がどう変わるか見てみよう。

    # 出力を読み取れるよう少し待つ。
    wait(200)
