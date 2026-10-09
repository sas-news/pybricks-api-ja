from pybricks.parameters import Color, Direction, Port
from pybricks.pupdevices import ColorDistanceSensor, PFMotor
from pybricks.tools import wait

# センサーを初期化する。
sensor = ColorDistanceSensor(Port.B)

# チャンネル別に複数のモーターを使える。
arm = PFMotor(sensor, 1, Color.BLUE)
wheel = PFMotor(sensor, 4, Color.RED, Direction.COUNTERCLOCKWISE)

# 両方のモーターを加速する。使えるのはこれらの値だけ。
# それ以外の値は近いものに切り捨てられる。
for duty in [15, 30, 45, 60, 75, 90, 100]:
    arm.dc(duty)
    wheel.dc(duty)
    wait(1000)

# 信号を確実に届けるため、コマンドの間に短い
# 間が入る。そのため速度の変化と
# 停止のタイミングが少しずつずれる。

# 両方のモーターにブレーキをかける。
arm.brake()
wheel.brake()
