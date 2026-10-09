#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Port
from pybricks.nxtdevices import VernierAdapter

from math import log


# Surface Temperature Sensor の変換式
def convert_raw_to_temperature(voltage):

    # 生の電圧を NTC 抵抗値に変換します。
    # Vernier Adapter EV3 ブロックに従います。
    counts = voltage/5000*4096
    ntc = 15000*(counts)/(4130-counts)

    # log(0) を安全に処理: ntc の値が正になるようにします。
    if ntc <= 0:
        ntc = 1

    # センサーのドキュメントにある Steinhart-Hart の式を適用します。
    K0 = 1.02119e-3
    K1 = 2.22468e-4
    K2 = 1.33342e-7
    return 1/(K0 + K1*log(ntc) + K2*log(ntc)**3)


# ポート1でアダプターを初期化
thermometer = VernierAdapter(Port.S1, convert_raw_to_temperature)

# 測定値を取得して表示
temp = thermometer.value()
print(temp)
