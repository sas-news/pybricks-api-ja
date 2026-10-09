from pybricks.parameters import Port
from pybricks.pupdevices import Motor
from pybricks.tools import wait

# ポートAのモーターを初期化する。
example_motor = Motor(Port.A)

# 先に前のサンプルを見てほしい。このサンプルでは
# 2つの端点を見つけて、その中間をゼロ点にする。

# run_until_stalled はストールしたときの角度を返す。
# 両方の端点でこの値を知りたい。
left_end = example_motor.run_until_stalled(-200, duty_limit=30)
right_end = example_motor.run_until_stalled(200, duty_limit=30)

# ここまでで右端のストッパーまで動いた。なので、
# この角度を両端点間の距離の半分にリセットできる。
# そうすると中間が0度に対応する。
example_motor.reset_angle((right_end - left_end) / 2)

# これ以降は、0に向かって回れば中央に着く。
example_motor.run_target(200, 0)

wait(1000)
