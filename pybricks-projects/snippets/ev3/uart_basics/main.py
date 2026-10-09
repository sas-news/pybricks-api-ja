#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.iodevices import UARTDevice
from pybricks.parameters import Port
from pybricks.media.ev3dev import SoundFile

# EV3を初期化
ev3 = EV3Brick()

# センサーポート2をUARTデバイスとして初期化
ser = UARTDevice(Port.S2, baudrate=115200)

# データを書き込む
ser.write(b'\r\nHello, world!\r\n')

# データの受信を待つ間、サウンドを再生する
for i in range(3):
    ev3.speaker.play_file(SoundFile.HELLO)
    ev3.speaker.play_file(SoundFile.GOOD)
    ev3.speaker.play_file(SoundFile.MORNING)
    print("Bytes waiting to be read:", ser.waiting())

# サウンド再生中に受信したすべてのデータを読み取る
data = ser.read_all()
print(data)
