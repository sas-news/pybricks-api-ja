# ThisHub = TechnicHub PrimeHub EssentialHub
from pybricks.hubs import ThisHub
from pybricks.tools import wait

# ハブを初期化する。
hub = ThisHub()

# 加速度ベクトルをg単位で取得する。
print(hub.imu.acceleration() / 9810)

# 角速度ベクトルを取得する。
print(hub.imu.angular_velocity())

# 出力したものを見られるよう少し待つ
wait(5000)
