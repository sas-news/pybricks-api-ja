from pybricks.pupdevices import Remote
from pybricks.tools import wait

# truck2 という名前のリモコンに接続する。
truck_remote = Remote("truck2", timeout=None)

print("Connected!")

wait(2000)
