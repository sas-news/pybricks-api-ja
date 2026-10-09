from pybricks.pupdevices import Remote

# 見つかったリモコンに接続する。見つかるまでずっと探し続ける。
my_remote = Remote(timeout=None)

print("Connected!")
