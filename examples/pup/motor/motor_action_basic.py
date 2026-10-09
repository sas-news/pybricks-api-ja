from pybricks.parameters import Port
from pybricks.pupdevices import Motor
from pybricks.tools import wait

# ポートAのモーターを初期化する。
example_motor = Motor(Port.A)

# 毎秒500度で回してから惰行で止める。
print("Demo of run")
example_motor.run(500)
wait(1500)
example_motor.stop()
wait(1500)

# 50%のデューティ比(「パワー」)で回してから惰行で止める。
print("Demo of dc")
example_motor.dc(50)
wait(1500)
example_motor.stop()
wait(1500)

# 毎秒500度で2秒間回す。
print("Demo of run_time")
example_motor.run_time(500, 2000)
wait(1500)

# 毎秒500度で90度回す。
print("Demo of run_angle")
example_motor.run_angle(500, 90)
wait(1500)

# 毎秒500度で角度0まで戻る
print("Demo of run_target to 0")
example_motor.run_target(500, 0)
wait(1500)

# 毎秒500度で角度-90まで戻る
print("Demo of run_target to -90")
example_motor.run_target(500, -90)
wait(1500)

# 毎秒500度でモーターがストールするまで回す
print("Demo of run_until_stalled")
example_motor.run_until_stalled(500)
print("Done")
wait(1500)
