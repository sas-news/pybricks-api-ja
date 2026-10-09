from pybricks.hubs import MoveHub

# ハブを初期化する。
hub = MoveHub()

# 「乱数」の種を初期化する。
_rand = hub.battery.voltage() + hub.battery.current()


# a <= N <= b を満たす整数Nをランダムに返す。
def randint(a, b):
    global _rand
    _rand = 75 * _rand % 65537  # Lehmer 方式
    return _rand * (b - a + 1) // 65537 + a


# いくつか試しに生成してみる。
for i in range(5):
    print(randint(0, 1000))
