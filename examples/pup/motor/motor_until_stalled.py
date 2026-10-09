from pybricks.parameters import Port
from pybricks.pupdevices import Motor

# ポートAのモーターを初期化する。
example_motor = Motor(Port.A)

# すべてのコマンドで毎秒200度の速さを使う。
speed = 200

# 機械的ストッパーに当たるまでモーターを逆回転させる。
# duty_limit=30 とすると、機械的ストッパーに対して
# 最大トルクの30%しかかからない。つまり、
# 強すぎる力で押し付けずに済む。
example_motor.run_until_stalled(-speed, duty_limit=30)

# 角度を0にリセットする。これで角度が0なら、
# 機械的な端点に達したと分かる。
example_motor.reset_angle(0)

# 次はモーターを往復させるループ。
# 常に機械的な端点から始まるので、
# モーターの初期角度に関係なく
# 同じ動作になる。
for count in range(10):
    example_motor.run_target(speed, 180)
    example_motor.run_target(speed, 90)
