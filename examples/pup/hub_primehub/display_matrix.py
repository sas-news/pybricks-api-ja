from pybricks.hubs import PrimeHub
from pybricks.tools import Matrix, wait

# ハブを初期化する。
hub = PrimeHub()

# 外側が明るく中央が暗い四角を作る。
SQUARE = Matrix(
    [
        [100, 100, 100, 100, 100],
        [100, 50, 50, 50, 100],
        [100, 50, 0, 50, 100],
        [100, 50, 50, 50, 100],
        [100, 100, 100, 100, 100],
    ]
)

# 四角を表示する。
hub.display.icon(SQUARE)
wait(3000)

# Pythonのリスト内包表記で画像を作る。この画像では、
# 各ピクセルの明るさは行と列のインデックスの合計。つまり
# 左上が暗く、右下が明るい。
GRADIENT = Matrix([[(r + c) for c in range(5)] for r in range(5)]) * 12.5

# 生成したグラデーションを表示する。
hub.display.icon(GRADIENT)
wait(3000)
