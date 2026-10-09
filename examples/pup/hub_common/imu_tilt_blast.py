# ThisHub = TechnicHub PrimeHub EssentialHub
from pybricks.hubs import ThisHub
from pybricks.parameters import Axis
from pybricks.tools import wait

# ハブを初期化。ここでは、ハブが上面を前に、
# 正面を右に向けて取り付けられていると指定する。
# 例えば51515セットのBLASTでは、ハブはこの向きで取り付けられている。
hub = ThisHub(top_side=Axis.X, front_side=-Axis.Y)

while True:
    # 傾きの値を読み取る。BLASTが直立しているとき値は0になる。
    # 前に傾けるとピッチが正、右に傾けるとロールが正になる。
    pitch, roll = hub.imu.tilt()

    # 結果をprintする。
    print(pitch, roll)
    wait(200)
