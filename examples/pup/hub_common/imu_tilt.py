# ThisHub = TechnicHub PrimeHub EssentialHub
from pybricks.hubs import ThisHub
from pybricks.tools import wait

# ハブを初期化する。
hub = ThisHub()

while True:
    # 傾きの値を読み取る。
    pitch, roll = hub.imu.tilt()

    # 結果をprintする。
    print(pitch, roll)
    wait(200)
