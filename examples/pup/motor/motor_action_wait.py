from pybricks.parameters import Port
from pybricks.pupdevices import Motor

# ポートAとBのモーターを初期化する。
track_motor = Motor(Port.A)
gripper_motor = Motor(Port.B)

# 走行用モーターを動かし始めるが、
# 終わるまで待たない。
track_motor.run_angle(500, 360, wait=False)

# 今度はグリッパーのモーターを回す。つまり
# 両方が同時に動く。
gripper_motor.run_angle(200, 720)
