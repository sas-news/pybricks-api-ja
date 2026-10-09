from pybricks.pupdevices import Remote

# 見つかったリモコンに接続する。
my_remote = Remote()

# リモコンの現在の名前をprintする。
print(my_remote.name())

# 新しい名前を決める。
my_remote.name("truck2")

print("Done!")
