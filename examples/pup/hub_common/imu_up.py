# ThisHub = TechnicHub PrimeHub MoveHub EssentialHub
from pybricks.hubs import ThisHub
from pybricks.parameters import Color, Side
from pybricks.tools import wait

# ハブを初期化する。
hub = ThisHub()

# 面ごとの色を辞書で定義する。
SIDE_COLORS = {
    Side.TOP: Color.RED,
    Side.BOTTOM: Color.BLUE,
    Side.LEFT: Color.GREEN,
    Side.RIGHT: Color.YELLOW,
    Side.FRONT: Color.MAGENTA,
    Side.BACK: Color.BLACK,
}

# 上を向いている面に応じて色を更新し続ける。
while True:
    # ハブのどの面が上を向いているか調べる。
    up_side = hub.imu.up()

    # 検出した面に応じて色を変える。
    hub.light.on(SIDE_COLORS[up_side])

    # 結果もprintする。
    print(up_side)
    wait(50)
