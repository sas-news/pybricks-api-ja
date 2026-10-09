from pybricks.parameters import Port
from pybricks.pupdevices import ColorSensor
from pybricks.tools import wait

# センサーを初期化する。
sensor = ColorSensor(Port.A)

# ずっと繰り返す。
while True:
    # 環境光の色の値を取得する。表面の色ではなく、
    # ランプや画面などの光源の色を測れる。
    hsv = sensor.hsv(surface=False)
    color = sensor.color(surface=False)

    # 環境光の強さを取得する。
    ambient = sensor.ambient()

    # 測定値をprintする。
    print(hsv, color, ambient)

    # センサーをパソコンの画面や色付きの光に向けて、色の値を見てみよう。
    # 手でセンサーを覆って、環境光の値の変化も見てみよう。

    # 出力された行を読めるよう少し待つ
    wait(100)
