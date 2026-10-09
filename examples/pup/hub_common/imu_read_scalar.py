# ThisHub = TechnicHub PrimeHub EssentialHub
from pybricks.hubs import ThisHub
from pybricks.parameters import Axis
from pybricks.tools import wait

# ハブを初期化する。
hub = ThisHub()

# 1軸分の加速度または角速度を取得する。
# 値が1つだけ必要なら、こちらのほうがメモリ効率が良い。
while True:
    # 前方向の加速度を読み取る。
    forward_acceleration = hub.imu.acceleration(Axis.X)

    # ヨーレートを読み取る。
    yaw_rate = hub.imu.angular_velocity(Axis.Z)

    # ヨーレートをprintする。
    print(yaw_rate)
    wait(100)
