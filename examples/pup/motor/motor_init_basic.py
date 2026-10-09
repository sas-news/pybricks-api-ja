from pybricks.parameters import Port
from pybricks.pupdevices import Motor
from pybricks.tools import wait

# ポートAのモーターを初期化する。
example_motor = Motor(Port.A)

# モーターを毎秒500度で時計回りに回す。
example_motor.run(500)

# 3秒待つ。
wait(3000)

# モーターを毎秒500度で反時計回りに回す。
example_motor.run(-500)

# 3秒待つ。
wait(3000)
