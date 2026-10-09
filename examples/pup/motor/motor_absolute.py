from pybricks.parameters import Port
from pybricks.pupdevices import Motor
from pybricks.tools import wait

# ポートAのモーターを初期化する。
example_motor = Motor(Port.A)

while True:
    # デフォルトの角度の値を取得する。
    angle = example_motor.angle()

    # 0〜360の範囲で角度を取得する。
    absolute_angle = example_motor.angle() % 360

    # -180〜179の範囲で角度を取得する。
    wrapped_angle = (example_motor.angle() + 180) % 360 - 180

    # 結果をprintする。
    print(angle, absolute_angle, wrapped_angle)
    wait(100)
