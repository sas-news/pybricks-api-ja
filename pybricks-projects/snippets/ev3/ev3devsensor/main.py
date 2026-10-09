#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.iodevices import Ev3devSensor

# Ev3devSensorを初期化する。
# この例では
# LEGO MINDSTORMS EV3カラーセンサーを使用する。
sensor = Ev3devSensor(Port.S3)

while True:
    # 生のRGB値を読み取る
    r, g, b = sensor.read('RGB-RAW')

    # 結果を表示
    print('R: {0}\t G: {1}\t B: {2}'.format(r, g, b))

    # 待機
    wait(200)
