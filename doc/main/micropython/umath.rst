.. pybricks-requirements:: stm32-extra stm32-float

:mod:`umath <umath>` -- 数学関数
============================================================

.. module:: umath

このMicroPythonモジュールは、Pythonの `math module`_ に似ています。

何もインポートせずに使用できる :ref:`built-in math functions<builtinmath>`
も参照してください。

丸めと符号
-------------------------------------

.. blockimg:: pybricks_blockMathOp_roundup

.. autofunction:: umath.ceil

.. blockimg:: pybricks_blockMathOp_rounddown

.. autofunction:: umath.floor

.. autofunction:: umath.trunc

.. autofunction:: umath.fmod

.. autofunction:: umath.fabs

.. autofunction:: umath.copysign

べき乗と対数
-------------------------------

.. autodata:: umath.e

.. blockimg:: pybricks_blockMathOp_exp

.. autofunction:: umath.exp

.. blockimg:: pybricks_blockMathArithmetic_power

.. blockimg:: pybricks_blockMathOp_pow10

.. autofunction:: umath.pow

.. blockimg:: pybricks_blockMathOp_ln

.. blockimg:: pybricks_blockMathOp_log10

.. autofunction:: umath.log

.. blockimg:: pybricks_blockMathOp_root

.. autofunction:: umath.sqrt

三角関数
-------------------------------

.. autodata:: umath.pi

.. autofunction:: umath.degrees

.. autofunction:: umath.radians

.. blockimg:: pybricks_blockMathOp_sin

.. autofunction:: umath.sin

.. blockimg:: pybricks_blockMathOp_asin

.. autofunction:: umath.asin

.. blockimg:: pybricks_blockMathOp_cos

.. autofunction:: umath.cos

.. blockimg:: pybricks_blockMathOp_acos

.. autofunction:: umath.acos

.. blockimg:: pybricks_blockMathOp_tan

.. autofunction:: umath.tan

.. blockimg:: pybricks_blockMathOp_atan

.. autofunction:: umath.atan

.. blockimg:: pybricks_blockMathOp_atan2

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
