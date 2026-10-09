#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.iodevices import I2CDevice
from pybricks.parameters import Port

# EV3を初期化
ev3 = EV3Brick()

# I2Cセンサーを初期化
device = I2CDevice(Port.S2, 0xD2 >> 1)

# デバイスから1バイト読み取る。
# このデバイスでは、Who Am I
# レジスタ (0x0F) を読み取ると期待値 211 が返る。
if 211 not in device.read(0x0F):
    raise OSError("Device is not attached")

# データを書き込むには、1バイト以上の
# bytesオブジェクトを作成する。例:
# data = bytes((1, 2, 3))

# レジスタ 0x22 に1バイト (値 0x08) を書き込む
device.write(0x22, bytes((0x08,)))
