from pybricks.messaging import BLERadio
from pybricks.parameters import Port
from pybricks.pupdevices import Motor
from pybricks.tools import wait

# ハブを初期化する。
radio = BLERadio(observe_channels=[1])

# モーターを初期化する。
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)

while True:
    # 相手側のハブからのブロードキャストを受信する。

    data = radio.observe(1)

    if data is not None:
        # データを受信していて、それが1秒以内のものなら、
        # その中身は相手側のハブで
        # radio.broadcast() に渡した値と
        # 同じ順序で入っている。
        left_angle, right_angle = data

        # このハブのモーターを、相手側ハブの
        # モーターと同じ位置に追従させる。
        left_motor.track_target(left_angle)
        right_motor.track_target(right_angle)

    # ブロードキャストは100ミリ秒ごとにしか送信されないので、
    # それより頻繁に observe() を呼んでも意味はない。
    wait(100)
