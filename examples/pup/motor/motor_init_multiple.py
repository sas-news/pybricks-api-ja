from pybricks.parameters import Port
from pybricks.pupdevices import Motor
from pybricks.tools import wait

# ポートAとBのモーターを初期化する。
track_motor = Motor(Port.A)
gripper_motor = Motor(Port.B)

# 両方のモーターを毎秒500度で回す。
track_motor.run(500)
gripper_motor.run(500)

# 3秒待つ。
wait(3000)
