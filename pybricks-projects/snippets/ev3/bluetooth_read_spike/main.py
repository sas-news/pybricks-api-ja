#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.tools import wait

from connection import SpikePrimeStreamReader

# ビープ音を鳴らします。
ev3 = EV3Brick()
ev3.speaker.beep()

# 接続を作成します。SPIKEハブのアドレスはREADME.mdを参照してください。
spike = SpikePrimeStreamReader('F4:84:4C:AA:C8:A4')

# あとは値を読み取るだけです。
for i in range(100):
    print(spike.orientation())
    print(spike.device('B'))
    wait(100)
