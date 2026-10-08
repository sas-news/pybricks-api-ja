.. pybricks-requirements:: stm32-extra

:mod:`usys` -- システム固有の関数
============================================================

このMicroPythonモジュールは、Pythonの `sys module`_ のサブセットです。

.. rubric:: 入出力ストリーム

.. module:: usys

.. autodata:: usys.stdin
    :annotation:

.. autodata:: usys.stdout
    :annotation:

.. autodata:: usys.stderr
    :annotation:

.. rubric:: バージョン情報

.. autodata:: implementation
    :annotation:

.. autodata:: version
    :annotation:

.. autodata:: version_info
    :annotation:

使用例
---------------

バージョン情報の表示
*******************************

.. literalinclude::
    ../../../examples/micropython/usys/pybricks_version.py

.. literalinclude::
    ../../../examples/micropython/usys/micropython_version.py

標準入出力
*******************************

``stdin`` ストリームは、Pybricks Codeの入出力ウィンドウ経由で入力を
キャプチャするために使用できます。その仕組みについては、
`キーボード入力 <keyboard input_>`_ プロジェクトを参照してください。
このアプローチは、あらゆる `他のデバイス <other device_>`_ との
データ交換にも拡張できます。

.. _keyboard input: https://pybricks.com/projects/tutorials/wireless/hub-to-device/pc-keyboard/
.. _other device: https://pybricks.com/projects/tutorials/wireless/hub-to-device/

.. _sys module: https://docs.python.org/3.5/library/sys.html
