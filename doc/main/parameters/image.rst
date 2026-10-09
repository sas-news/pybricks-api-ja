.. pybricks-requirements:: image

Image
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |this image| replace:: この画像

.. autoclass:: pybricks.parameters.Image
    :no-members:

    .. automethod:: pybricks.parameters.Image.empty

    .. rubric:: テキストの描画

    画像にテキストを描画する方法は2つあります。 :meth:`draw_text` では
    テキストを画像上に正確に配置でき、 :meth:`print` では新しい行に
    テキストを自動的に出力できます。

    .. automethod:: pybricks.parameters.Image.draw_text

    .. automethod:: pybricks.parameters.Image.print

    .. automethod:: pybricks.parameters.Image.set_font

    .. rubric:: 画像の描画

    別の画像のコピーを画像上に描画できます。また、サブ画像を使って
    画像の一部をコピーすることも検討してください。

    .. automethod:: pybricks.parameters.Image.draw_image

    .. rubric:: 図形の描画

    これらは点、直線、矩形、円などの基本的な図形を描画するメソッドです。

    .. automethod:: pybricks.parameters.Image.draw_pixel

    .. automethod:: pybricks.parameters.Image.draw_line

    .. automethod:: pybricks.parameters.Image.draw_box

    .. automethod:: pybricks.parameters.Image.draw_circle

    .. rubric:: 画像のプロパティ

    .. autoattribute:: pybricks.parameters.Image.width

    .. autoattribute:: pybricks.parameters.Image.height

    .. rubric:: 画像全体の置き換え

    .. automethod:: pybricks.parameters.Image.clear

    .. automethod:: pybricks.parameters.Image.load_image
