.. pybricks-requirements:: stm32-extra

:mod:`micropython` -- MicroPythonの内部機能
============================================================

.. automodule:: micropython
    :no-members:

.. autofunction:: micropython.const

.. autofunction:: micropython.heap_lock

.. autofunction:: micropython.heap_unlock

.. autofunction:: micropython.kbd_intr

.. autofunction:: micropython.mem_info

.. autofunction:: micropython.opt_level

.. autofunction:: micropython.qstr_info

.. autofunction:: micropython.stack_use


使用例
---------------------

効率化のための定数の使用
******************************

.. literalinclude::
    ../../../examples/micropython/const.py

空きRAMの確認
******************************

.. literalinclude::
    ../../../examples/micropython/memuse.py

これにより、以下に示す形式で情報が出力されます。このSPIKE Primeハブの例では、
コード内の変数が使用できるメモリとして257696バイト（251 KB）が
残っています。 ::

    stack: 372 out of 40184
    GC: total: 258048, used: 352, free: 257696
    No. of 1-blocks: 4, 2-blocks: 2, max blk sz: 8, max free sz: 16103


さらに詳しいメモリ統計の取得
******************************

.. literalinclude::
    ../../../examples/micropython/memstat.py
