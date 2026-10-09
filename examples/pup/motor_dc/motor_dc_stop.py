from pybricks.parameters import Port
from pybricks.pupdevices import DCMotor
from pybricks.tools import wait

# ポートAの回転センサー無しモーターを初期化する。
example_motor = DCMotor(Port.A)

# 起動と停止を10回繰り返す。
for count in range(10):
    print("Counter:", count)

    example_motor.dc(70)
    wait(1000)

    example_motor.stop()
    wait(1000)
