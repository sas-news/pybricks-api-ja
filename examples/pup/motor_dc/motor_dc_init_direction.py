from pybricks.parameters import Direction, Port
from pybricks.pupdevices import DCMotor
from pybricks.tools import wait

# ポートAの回転センサー無しモーターを、
# 反時計回りを正方向として初期化する。
example_motor = DCMotor(Port.A, Direction.COUNTERCLOCKWISE)

# 正のデューティ比を指定すると、モーターは反時計回りに回る。
example_motor.dc(70)

# (列車用の)モーターが逆向きや上下逆に付いているときに便利。
# 正方向を変えておくとスクリプトが読みやすくなる。
# 正の値が列車やロボットを前進させるからだ。

# 3秒待つ。
wait(3000)
