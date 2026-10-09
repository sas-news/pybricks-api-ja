from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase

# 両方のモーターを初期化。この例では、左側のモーターは
# 反時計回りに回るとロボットが前進する。
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)

# ドライブベースを初期化。この例では車輪の直径は56mm。
# 左右の車輪が地面に接する点どうしの距離は112mm。
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)

# 必要なら次の行のコメントを外すと、ジャイロで精度を上げられる。
# drive_base.use_gyro(True)

# 500mm(50cm)前進する。
drive_base.straight(500)

# 時計回りに180度旋回する。
drive_base.turn(180)

# もう一度前進してスタート地点に戻る。
drive_base.straight(500)

# 反時計回りに旋回する。
drive_base.turn(-180)
