from pybricks.parameters import Port
from pybricks.pupdevices import ColorSensor
from pybricks.tools import wait

# センサーを初期化する。
sensor = ColorSensor(Port.A)


def main():
    # メインのコードを実行する。
    while True:
        print(sensor.color())
        wait(500)


# メインのコードを try/finally で囲むと、例外が起きても
# プログラム終了時にクリーンアップが必ず走る。
try:
    main()
finally:
    # ここにクリーンアップ処理を書く。
    print("Cleaning up.")
    sensor.lights.off()
