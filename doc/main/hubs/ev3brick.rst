EV3 Brick
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/cad/output/ev3device-ev3.png
    :width: 50%

.. autoclass:: pybricks.hubs.EV3Brick
    :no-members:

    .. rubric:: ボタンを使う

    .. automethod:: pybricks.hubs::EV3Brick.buttons.pressed

    .. rubric:: ブリックのステータスライトを使う

    .. automethod:: pybricks.hubs::EV3Brick.light.on

    .. automethod:: pybricks.hubs::EV3Brick.light.off

    .. automethod:: pybricks.hubs::EV3Brick.light.blink

    .. automethod:: pybricks.hubs::EV3Brick.light.animate

    .. rubric:: スピーカーを使う

    .. automethod:: pybricks.hubs::EV3Brick.speaker.volume

    .. automethod:: pybricks.hubs::EV3Brick.speaker.beep

    .. automethod:: pybricks.hubs::EV3Brick.speaker.play_notes

    .. rubric:: スクリーンを使う

    .. |this image| replace:: スクリーン

    .. automethod:: pybricks.hubs::EV3Brick.screen.clear

    .. automethod:: pybricks.hubs::EV3Brick.screen.draw_text
        :noindex:

    .. automethod:: pybricks.hubs::EV3Brick.screen.print
        :noindex:

    .. automethod:: pybricks.hubs::EV3Brick.screen.set_font
        :noindex:

    .. automethod:: pybricks.hubs::EV3Brick.screen.load_image

    .. automethod:: pybricks.hubs::EV3Brick.screen.draw_image
        :noindex:

    .. automethod:: pybricks.hubs::EV3Brick.screen.draw_pixel

    .. automethod:: pybricks.hubs::EV3Brick.screen.draw_line

    .. automethod:: pybricks.hubs::EV3Brick.screen.draw_box

    .. automethod:: pybricks.hubs::EV3Brick.screen.draw_circle

    .. autoattribute:: pybricks.hubs::EV3Brick.screen.width
        :annotation: = 178

    .. autoattribute:: pybricks.hubs::EV3Brick.screen.height
        :annotation: = 128

    .. rubric:: バッテリーを使う

    .. automethod:: pybricks.hubs::EV3Brick.battery.voltage

    .. automethod:: pybricks.hubs::EV3Brick.battery.current

    .. rubric:: システム制御

    .. automethod:: pybricks.hubs::EV3Brick.system.info

    .. automethod:: pybricks.hubs::EV3Brick.system.set_stop_button

    .. automethod:: pybricks.hubs::EV3Brick.system.storage

    .. automethod:: pybricks.hubs::EV3Brick.system.reset_storage

    .. automethod:: pybricks.hubs::EV3Brick.system.shutdown

ステータスライトの例
---------------------

ライトを点灯して色を変える
**************************************

.. literalinclude::
    ../../../examples/ev3/light_color/main.py

スクリーンの例
---------------------

スクリーンに図形を描く
****************************

.. literalinclude::
    ../../../examples/ev3/screen_draw/main.py
