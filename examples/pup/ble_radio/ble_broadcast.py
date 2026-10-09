from pybricks.messaging import BLERadio
from pybricks.parameters import Port
from pybricks.pupdevices import Motor
from pybricks.tools import wait

# ハブを初期化する。
radio = BLERadio(broadcast_channel=1)

# モーターを初期化する。
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)

while True:
    # 相手側のハブに送るモーターの角度を読み取る。
    left_angle = left_motor.angle()
    right_angle = right_motor.angle()

    # ブロードキャストするデータを設定し、まだ送信中でなければ開始する。
    data = (left_angle, right_angle)
    radio.broadcast(data)

    # ブロードキャストは100ミリ秒ごとにしか送信されないので、
    # それより頻繁に broadcast() を呼んでも意味はない。
    wait(100)
