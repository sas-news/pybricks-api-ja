from pybricks.parameters import Port
from pybricks.pupdevices import Motor

# ポートAのモーターを初期化する。
example_motor = Motor(Port.A)

# 角度を0にリセットする。
example_motor.reset_angle(0)

# 角度を1234にリセットする。
example_motor.reset_angle(1234)

# 角度を絶対角度にリセットする。
# これは絶対エンコーダー搭載モーターでのみ使える。
# それ以外のモーターでは
# エラーになる。
example_motor.reset_angle()
