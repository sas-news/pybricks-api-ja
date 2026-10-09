from pybricks.parameters import Port
from pybricks.pupdevices import DCMotor
from pybricks.tools import wait

# ポートAの回転センサー無しモーターを初期化する。
example_motor = DCMotor(Port.A)

# モーターを70%のデューティ比(「70%パワー」)で時計回り(前進)に回す。
example_motor.dc(70)

# 3秒待つ。
wait(3000)

# モーターを70%のデューティ比で反時計回り(後退)に回す。
example_motor.dc(-70)

# 3秒待つ。
wait(3000)
