from pybricks.parameters import Color

# 2つの色は、h, s, v 属性がすべて等しいとき同じ色とみなされる。
if Color.BLUE == Color(240, 100, 100):
    print("Yes, these colors are the same.")

# 色をスケールして明るさを変えられる。
red_dark = Color.RED * 0.5

# 色をシフトして色相を変えられる。
red_shifted = Color.RED >> 30

# 色は変更不可なので、既存オブジェクトの h, s, v は書き換えられない。
try:
    Color.GREEN.h = 125
except AttributeError:
    print("Sorry, can't change the hue of an existing color object!")

# でも、丸ごと新しい色を定義すれば組み込みの色を上書きできる。
Color.GREEN = Color(h=125)

# 色はクラス属性としても辞書としても読み書きできる。
print(Color.BLUE)
print(Color["BLUE"])
print(Color["BLUE"] is Color.BLUE)
print(Color)
print([c for c in Color])

# これでループ内で既存の色を更新できる。
for name in ("BLUE", "RED", "GREEN"):
    Color[name] = Color(1, 2, 3)
