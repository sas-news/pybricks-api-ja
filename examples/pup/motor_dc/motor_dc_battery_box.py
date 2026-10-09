from pybricks.parameters import Port
from pybricks.pupdevices import DCMotor
from pybricks.tools import wait

# モーターを初期化する。
train_motor = DCMotor(Port.A)

# 列車の「パワー」を選ぶ。負の値は後進。
train_motor.dc(50)

# 何もせず待ち続ける。列車は走り続ける。
while True:
    wait(1000)
