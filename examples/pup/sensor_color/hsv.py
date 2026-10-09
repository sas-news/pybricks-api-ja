from pybricks.parameters import Port
from pybricks.pupdevices import ColorSensor
from pybricks.tools import wait

# センサーを初期化する。
sensor = ColorSensor(Port.A)

while True:
    # 標準の color() メソッドは常に測定値を
    # いちばん近い「きっちりした」色に丸める。
    # 多くの用途ではこれで十分。

    # でも、丸めずに元の色相・彩度・
    # 明度をそのまま取ることもできる:
    color = sensor.hsv()

    # 結果をprintする。
    print(color)

    # 値を読み取れるよう少し待つ。
    wait(500)
