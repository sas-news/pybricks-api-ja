#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.iodevices import I2CDevice
from pybricks.parameters import Port

# EV3を初期化
ev3 = EV3Brick()

# I2Cセンサーを初期化
device = I2CDevice(Port.S2, 0xD2 >> 1)

# 読み取りの推奨方法
result, = device.read(reg=0x0F, length=1)

# 特定のレジスタを指定せずに1バイト読み取る:
device.read(reg=None, length=1)

# 特定のレジスタを指定せずに0バイト読み取る:
device.read(reg=None, length=0)

# I2Cの書き込み操作は、レジスタバイトと
# それに続く一連のデータバイトで構成される。デバイスによっては、
# 以下のようにレジスタやデータを省略できる:

# 書き込みの推奨方法:
device.write(reg=0x22, data=b'\x08')

# 特定のレジスタを指定せずに1バイト書き込む:
device.write(reg=None, data=b'\x08')

# 特定のレジスタに0バイト書き込む:
device.write(reg=0x08, data=None)

# 特定のレジスタを指定せずに0バイト書き込む:
device.write(reg=None, data=None)
