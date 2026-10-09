from pybricks.parameters import Port, Stop
from pybricks.pupdevices import Motor
from pybricks.tools import wait

# ポートAのモーターを初期化する。
example_motor = Motor(Port.A)

# デフォルトではモーターは位置を保持する。
# 動かそうとすると角度が補正され続ける。
example_motor.run_angle(500, 360)
wait(1000)

# これは上とまったく同じことをする。
example_motor.run_angle(500, 360, then=Stop.HOLD)
wait(1000)

# ブレーキも使える。抵抗はかかるが、
# 動かしてもモーターは元に戻らない。
example_motor.run_angle(500, 360, then=Stop.BRAKE)
wait(1000)

# これでモーターは停止後に自由に惰行する。
example_motor.run_angle(500, 360, then=Stop.COAST)
wait(1000)
