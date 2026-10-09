from pybricks.parameters import Port
from pybricks.pupdevices import Motor
from pybricks.tools import wait

# ポートAとBのモーターを初期化する。
track_motor = Motor(Port.A)
gripper_motor = Motor(Port.B)

# 両方のモーターに wait=False で動作させる
track_motor.run_angle(500, 360, wait=False)
gripper_motor.run_angle(200, 720, wait=False)

# 片方または両方のモーターがまだ動作中の間、
# 別のことをする。この例ではただ待つだけ。
while not track_motor.done() or not gripper_motor.done():
    wait(10)

print("Both motors are done!")
