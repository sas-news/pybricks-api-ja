#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Port
from pybricks.iodevices import Ev3devSensor


class MySensor(Ev3devSensor):
    """Example of extending the Ev3devSensor class."""

    def __init__(self, port):
        """Initialize the sensor."""

        # 親クラスを初期化する。
        super().__init__(port)

        # sysfsパスを取得する。
        self.path = '/sys/class/lego-sensor/sensor' + str(self.sensor_index)

    def get_modes(self):
        """Get a list of mode strings so we don't have to look them up."""

        # modesファイルのパス。
        modes_path = self.path + '/modes'

        # modesファイルを開く。
        with open(modes_path, 'r') as m:

            # 内容を読み取る。
            contents = m.read()

            # 改行文字を取り除き、空白文字で分割する。
            return contents.strip().split(' ')


# センサーを初期化
sensor = MySensor(Port.S3)

# このセンサーの場所を表示
print(sensor.path)

# 利用可能なモードを表示
modes = sensor.get_modes()
print(modes)

# このセンサーのモード0を読み取る
val = sensor.read(modes[0])
print(val)
