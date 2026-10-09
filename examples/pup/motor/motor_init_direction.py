from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor
from pybricks.tools import wait

# ポートAのモーターを、反時計回りを正方向として初期化する。
example_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)

# 正の速度を指定すると、モーターは反時計回りに回る。
example_motor.run(500)

# モーターが逆向きや上下逆に付いているときに便利。
# 正方向を変えておくとスクリプトが読みやすくなる。
# 正の値がロボットや機構を前進させるからだ。

# 3秒待つ。
wait(3000)
