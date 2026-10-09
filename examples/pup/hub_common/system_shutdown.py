# ThisHub = MoveHub CityHub TechnicHub PrimeHub EssentialHub
from pybricks.hubs import ThisHub
from pybricks.tools import wait

# ハブを初期化する。
hub = ThisHub()

# 別れのメッセージを出して、送信されるまで少し待つ。
print("Goodbye!")
wait(100)

# ハブをシャットダウンする。
hub.system.shutdown()
