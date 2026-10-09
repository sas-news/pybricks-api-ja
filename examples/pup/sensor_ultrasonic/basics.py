from pybricks.parameters import Port
from pybricks.pupdevices import UltrasonicSensor
from pybricks.tools import wait

# センサーを初期化する。
eyes = UltrasonicSensor(Port.A)

while True:
    # 測った距離をprintする。
    print(eyes.distance())

    # 500mmより近くに物体を検出したら:
    if eyes.distance() < 500:
        # ライトを付ける。
        eyes.lights.on(100)
    else:
        # ライトを消す。
        eyes.lights.off()

    # 出力を読み取れるよう少し待つ。
    wait(100)
