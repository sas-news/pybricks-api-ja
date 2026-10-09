.. pybricks-requirements:: stm32-extra stm32-float

:mod:`umath <umath>` -- 数学関数
============================================================

.. module:: umath

このMicroPythonモジュールは、Pythonの `math module`_ に似ています。

何もインポートせずに使用できる :ref:`built-in math functions<builtinmath>`
も参照してください。

丸めと符号
-------------------------------------

.. autofunction:: umath.ceil

.. autofunction:: umath.floor

.. autofunction:: umath.trunc

.. autofunction:: umath.fmod

.. autofunction:: umath.fabs

.. autofunction:: umath.copysign

べき乗と対数
-------------------------------

.. autodata:: umath.e

.. autofunction:: umath.exp

.. autofunction:: umath.pow

.. autofunction:: umath.log

.. autofunction:: umath.sqrt

三角関数
-------------------------------

.. autodata:: umath.pi

.. autofunction:: umath.degrees

.. autofunction:: umath.radians

.. autofunction:: umath.sin

.. autofunction:: umath.asin

.. autofunction:: umath.cos

.. autofunction:: umath.acos

.. autofunction:: umath.tan

.. autofunction:: umath.atan

.. autofunction:: umath.atan2

その他の数学関数
-------------------------------

.. autofunction:: umath.isfinite

.. autofunction:: umath.isinfinite

.. autofunction:: umath.isnan

.. autofunction:: umath.modf

.. autofunction:: umath.frexp

.. autofunction:: umath.ldexp

.. _math module: https://docs.python.org/3.5/library/math.html#module-math
