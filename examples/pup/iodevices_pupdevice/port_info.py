from pybricks.iodevices import PUPDevice
from pybricks.parameters import Port
from uerrno import ENODEV

# デバイスIDとその名前の対応表。
device_names = {
    # pybricks.pupdevices.DCMotor
    1: "Wedo 2.0 Medium Motor",
    2: "Powered Up Train Motor",
    # pybricks.pupdevices.Light
    8: "Powered Up Light",
    # pybricks.pupdevices.Motor
    38: "BOOST Interactive Motor",
    46: "Technic Large Motor",
    47: "Technic Extra Large Motor",
    48: "SPIKE Medium Angular Motor",
    49: "SPIKE Large Angular Motor",
    65: "SPIKE Small Angular Motor",
    75: "Technic Medium Angular Motor",
    76: "Technic Large Angular Motor",
    # pybricks.pupdevices.TiltSensor
    34: "Wedo 2.0 Tilt Sensor",
    # pybricks.pupdevices.InfraredSensor
    35: "Wedo 2.0 Infrared Motion Sensor",
    # pybricks.pupdevices.ColorDistanceSensor
    37: "BOOST Color Distance Sensor",
    # pybricks.pupdevices.ColorSensor
    61: "SPIKE Color Sensor",
    # pybricks.pupdevices.UltrasonicSensor
    62: "SPIKE Ultrasonic Sensor",
    # pybricks.pupdevices.ForceSensor
    63: "SPIKE Force Sensor",
    # pybricks.pupdevices.ColorLightMatrix
    64: "SPIKE 3x3 Color Light Matrix",
}

# 既知のポートのリストを作る。
ports = [Port.A, Port.B]

# 対応するハブでは、さらにポートを追加する。
try:
    ports.append(Port.C)
    ports.append(Port.D)
except AttributeError:
    pass

# 対応するハブでは、さらにポートを追加する。
try:
    ports.append(Port.E)
    ports.append(Port.F)
except AttributeError:
    pass

# 使えるポートをすべて調べる。
for port in ports:
    # デバイスが付いていれば取得を試みる。
    try:
        device = PUPDevice(port)
    except OSError as ex:
        if ex.args[0] == ENODEV:
            # このポートにはデバイスが見つからなかった。
            print(port, ": ---")
            continue
        else:
            raise

    # デバイスIDを取得する
    id = device.info()["id"]

    # 名前を引く。
    try:
        print(port, ":", device_names[id])
    except KeyError:
        print(port, ":", "Unknown device with ID", id)
