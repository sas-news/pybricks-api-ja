from pybricks.hubs import MoveHub
from pybricks.tools import wait

# ハブを初期化する。
hub = MoveHub()

# 加速度のタプルを取得する。
print(hub.imu.acceleration())

while True:
    # 加速度を個別に取得する。
    x, y, z = hub.imu.acceleration()
    print(x, y, z)

    # 出力したものを見られるよう少し待つ。
    wait(100)
