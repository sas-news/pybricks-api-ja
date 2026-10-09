from pybricks.tools import hub_menu

# このサンプルは、Pybricks Code に他の3つのプログラム
# "fly_mission" "drive_mission" "zigzag" が入っている前提。
# 実行するものを選べるメニューを作るサンプル。

# 文字を選ぶ。
selected = hub_menu("F", "D", "Z")

# 選ばれたものに応じてプログラムを実行する。
if selected == "F":
    import fly_mission
elif selected == "D":
    import drive_mission
elif selected == "Z":
    import zigzag
