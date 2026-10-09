from pybricks.pupdevices import Remote

try:
    # 5秒間リモコンを探す。
    my_remote = Remote(timeout=5000)

    print("Connected!")

    # ここでリモコンを使うコードを書ける。

except OSError:
    print("Could not find the remote.")

    # ここではリモコンを使わずに
    # ロボットを動かせる。
