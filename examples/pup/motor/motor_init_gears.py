from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor
from pybricks.tools import wait

# ポートAのモーターを、反時計回りを正方向として初期化する。
# さらに、12歯と36歯のギアからなるギア列を1つ指定する。12歯の
# ギアはモーター軸に、36歯のギアは出力軸に付いている。
geared_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE, [12, 36])

# 出力軸を毎秒100度で回す。ギア分を補うため、
# モーターの回転速度は自動的に上げられる。
geared_motor.run(100)

# 3秒待つ。
wait(3000)
