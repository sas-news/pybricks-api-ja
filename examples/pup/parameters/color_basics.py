from pybricks.parameters import Color

# 色はprintできる。色はColorクラスからも、
# 色を測定するセンサーからも得られる。
print(Color.RED)

# 色相・彩度・明度の各プロパティを読み取れる。
print(Color.RED.h, Color.RED.s, Color.RED.v)

# 自分で色を作れる。彩度と明度のデフォルトは100。
my_green = Color(h=125)
my_dark_green = Color(h=125, s=80, v=30)

# カスタム色をprintすると、どう定義されたかがそのまま見える。
print(my_dark_green)

# 組み込みの色に新しい色を追加することもできる。
Color.MY_DARK_BLUE = Color(h=235, s=80, v=30)

# このように追加した色は、printすると名前しか出ない。でも
# 属性を読めば h, s, v の値を取得できる。
print(Color.MY_DARK_BLUE)
print(Color.MY_DARK_BLUE.h, Color.MY_DARK_BLUE.s, Color.MY_DARK_BLUE.v)
