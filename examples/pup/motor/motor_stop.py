from pybricks.parameters import Port
from pybricks.pupdevices import Motor
from pybricks.tools import wait

# ポートAのモーターを初期化する。
example_motor = Motor(Port.A)

# 毎秒500度で回してから惰行で止める。
example_motor.run(500)
wait(1500)
example_motor.stop()
wait(1500)

# 毎秒500度で回してからブレーキで止める。
example_motor.run(500)
wait(1500)
example_motor.brake()
wait(1500)

# 毎秒500度で回してから保持して止める。
example_motor.run(500)
wait(1500)
example_motor.hold()
wait(1500)

# 毎秒500度で回してから速度0で止める。
example_motor.run(500)
wait(1500)
example_motor.run(0)
wait(1500)
