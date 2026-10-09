from pybricks.parameters import Button, Direction, Port
from pybricks.pupdevices import Motor, Remote
from pybricks.robotics import Car
from pybricks.tools import wait

# モーターをセットアップする。
front = Motor(Port.A, Direction.COUNTERCLOCKWISE)
rear = Motor(Port.B, Direction.COUNTERCLOCKWISE)
steer = Motor(Port.C, Direction.CLOCKWISE)

# リモコンに接続する。
remote = Remote()

# 車をセットアップする。
car = Car(steer, [front, rear])

# メインプログラムはここから。
while True:
    # リモコンの状態を読み取る。
    pressed = remote.buttons.pressed()

    # 左パッドでステアリング。量は初期化時に
    # 決めた角度に対する割合(%)。
    steering = 0
    if Button.LEFT_PLUS in pressed:
        steering += 100
    elif Button.LEFT_MINUS in pressed:
        steering -= 100
    car.steer(steering)

    # 右パッドで運転する。
    power = 0
    if Button.RIGHT_PLUS in pressed:
        power += 100
    elif Button.RIGHT_MINUS in pressed:
        power -= 100
    car.drive_power(power)

    # 少し待つ。
    wait(10)
