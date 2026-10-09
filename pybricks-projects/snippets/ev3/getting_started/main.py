#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port

# ここにオブジェクトを作成します

# EV3 Brickを初期化します。
ev3 = EV3Brick()

# ポートBのモーターを初期化します。
test_motor = Motor(Port.B)

# ここにプログラムを書きます

# 音を鳴らします。
ev3.speaker.beep()

# モーターを毎秒500度の速さで、目標角度90度まで回転させます。
test_motor.run_target(500, 90)

# もう一度ビープ音を鳴らします。
ev3.speaker.beep(frequency=1000, duration=500)
