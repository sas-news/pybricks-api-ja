from pybricks.parameters import Button, Color
from pybricks.pupdevices import Remote


def button_to_color(buttons):

    # ボタンに応じた色を返す。
    if Button.LEFT_PLUS in buttons:
        return Color.RED
    if Button.LEFT_MINUS in buttons:
        return Color.GREEN
    if Button.LEFT in buttons:
        return Color.ORANGE
    if Button.RIGHT_PLUS in buttons:
        return Color.BLUE
    if Button.RIGHT_MINUS in buttons:
        return Color.YELLOW
    if Button.RIGHT in buttons:
        return Color.CYAN
    if Button.CENTER in buttons:
        return Color.VIOLET

    # デフォルトでは色無しを返す。
    return Color.NONE


# リモコンに接続する。
remote = Remote()

while True:
    # ボタンが押されるまで待つ。
    pressed = ()
    while not pressed:
        pressed = remote.buttons.pressed()

    # ボタンのコードを色に変換する。
    color = button_to_color(pressed)

    # リモコンのライトの色を設定する。
    remote.light.on(color)

    # すべてのボタンが離されるまで待つ。
    while pressed:
        pressed = remote.buttons.pressed()
