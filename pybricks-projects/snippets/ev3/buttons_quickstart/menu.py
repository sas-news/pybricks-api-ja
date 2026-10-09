def wait_for_button(ev3):
    """
    This function shows a picture of the buttons on the EV3 screen.

    Then it waits until you press a button.

    It returns which button was pressed.
    """

    # ボタンの画像を画面に表示します。
    ev3.screen.load_image('buttons.png')

    # ヒント: 画像にテキストやアイコンを追加すると、プログラムで
    # 各ボタンが何をするか覚えやすくなります。

    # ボタンが1つ押されるまで待ち、結果を保存します。
    pressed = []
    while len(pressed) != 1:
        pressed = ev3.buttons.pressed()
    button = pressed[0]

    # 押されたボタンを画面に表示します
    ev3.screen.draw_text(2, 100, button)

    # ボタンが離されるまで待ちます。
    while any(ev3.buttons.pressed()):
        pass

    # 押されたボタンを返します。
    return button
