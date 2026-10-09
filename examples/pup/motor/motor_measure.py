from pybricks.parameters import Port
from pybricks.pupdevices import Motor
from pybricks.tools import wait

# ポートAのモーターを初期化する。
example_motor = Motor(Port.A)

# 毎秒300度で動き始める。
example_motor.run(300)

# 角度と速度を50回表示する。
for i in range(100):
    # 角度(度)と速度(度/秒)を読み取る。
    angle = example_motor.angle()
    speed = example_motor.speed()

    # 値をprintする。
    print(angle, speed)

    # 表示を読み取れるよう少し待つ。
    wait(200)
