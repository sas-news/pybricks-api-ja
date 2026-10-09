from pybricks.parameters import Color, Port
from pybricks.pupdevices import ColorDistanceSensor, PFMotor
from pybricks.tools import wait

# センサーを初期化する。
sensor = ColorDistanceSensor(Port.B)

# チャンネル1の赤い出力につながるモーターを初期化する。
motor = PFMotor(sensor, 1, Color.RED)

# 回転して止まる。
motor.dc(100)
wait(1000)
motor.stop()
wait(1000)

# 半分の速さで逆回転して止まる。
motor.dc(-50)
wait(1000)
motor.stop()
