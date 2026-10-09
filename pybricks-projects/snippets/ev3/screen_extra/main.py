#!/usr/bin/env pybricks-micropython

import math

from pybricks.hubs import EV3Brick
from pybricks.parameters import Color
from pybricks.tools import wait
from pybricks.media.ev3dev import Font, Image


# EV3を初期化します。
ev3 = EV3Brick()


# 画面分割 ##################################################################

# 画面の左半分用のサブイメージを作成します
left = Image(ev3.screen, sub=True, x1=0, y1=0,
             x2=ev3.screen.width // 2 - 1, y2=ev3.screen.height - 1)

# 画面の右半分用のサブイメージを作成します
right = Image(ev3.screen, sub=True, x1=ev3.screen.width // 2, y1=0,
              x2=ev3.screen.width - 1, y2=ev3.screen.height - 1)

# 等幅フォントを使うと、printしたテキストが縦に揃います
right.set_font(Font(size=8, monospace=True))


# y = sin(x) のグラフを描きます
def f(x):
    return math.sin(x)


for t in range(200):
    # 左側にグラフを描きます

    # tをx軸の値に換算してy値を計算します
    x0 = (t - 1) * 2 * math.pi / left.width
    y0 = f(x0)
    x1 = t * 2 * math.pi / left.width
    y1 = f(x1)

    # y値を画面座標に換算します
    sy0 = (-y0 + 1) * left.height / 2
    sy1 = (-y1 + 1) * left.height / 2

    # 現在のグラフを左に1ピクセルずらします
    left.draw_image(-1, 0, left)
    # 前のプロット点を消すため、最後の列を白で塗りつぶします
    left.draw_line(left.width - 1, 0, left.width - 1, left.height - 1, 1, Color.WHITE)
    # 新しいグラフの値を最後の列に描きます
    left.draw_line(left.width - 2, int(sy0), left.width - 1, int(sy1), 3)

    # 10個おきの値を右側に表示します
    if t % 10 == 0:
        right.print('{:10.2f}{:10.2f}'.format(x1, y1))

    wait(100)


# スプライトアニメーション ############################################################

# ダブルバッファリング用に画面のコピーを作成します
buf = Image(ev3.screen)

# ファイルから画像を読み込みます
bg = Image('background.png')
sprite = Image('sprite.png')

# スプライトアニメーションのコマ数
NUM_CELLS = 8

# スプライトの各コマは75 x 100ピクセル
CELL_WIDTH, CELL_HEIGHT = 75, 100

# 各コマをサブイメージとして取得します。
# 個別の画像を読み込むより効率的です
walk_right = [Image(sprite, sub=True, x1=x * CELL_WIDTH, y1=0,
                    x2=(x + 1) * CELL_WIDTH - 1, y2=CELL_HEIGHT - 1)
              for x in range(NUM_CELLS)]
walk_left = [Image(sprite, sub=True, x1=x * CELL_WIDTH, y1=CELL_HEIGHT,
                   x2=(x + 1) * CELL_WIDTH - 1, y2=2 * CELL_HEIGHT - 1)
             for x in range(NUM_CELLS)]


# 左から右へ歩かせます
for x in range(-100, 200, 2):
    # 背景画像を描きます
    buf.draw_image(0, 0, bg)
    # 現在のコマを描きます。紫は透明として扱われます
    buf.draw_image(x, 5, walk_right[x // 5 % NUM_CELLS], Color.PURPLE)
    # ダブルバッファを画面にコピーします
    ev3.screen.draw_image(0, 0, buf)
    # 毎秒20フレーム
    wait(50)

# 右から左へ歩かせます
for x in range(200, -100, -2):
    buf.draw_image(0, 0, bg)
    buf.draw_image(x, 5, walk_left[x // 5 % NUM_CELLS], Color.PURPLE)
    ev3.screen.draw_image(0, 0, buf)
    wait(50)

wait(1000)
