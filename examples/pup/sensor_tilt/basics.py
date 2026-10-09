from pybricks.parameters import Port
from pybricks.pupdevices import TiltSensor
from pybricks.tools import wait

# センサーを初期化する。
accel = TiltSensor(Port.A)

while True:
    # 水平面に対する傾き角度を読み取る。
    pitch, roll = accel.tilt()

    # 値をprintする
    print("Pitch:", pitch, "Roll:", roll)

    # 出力を読み取れるよう少し待つ。
    wait(100)
