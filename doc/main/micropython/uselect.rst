.. pybricks-requirements:: stm32-extra

:mod:`uselect` -- イベントの待機
=================================

.. automodule:: uselect
    :no-members:

    .. rubric:: Pollインスタンスとクラス

    .. autofunction:: poll

    .. autoclass:: Poll
        :no-members:

        .. automethod:: register

        .. automethod:: unregister

        .. automethod:: modify

        .. automethod:: poll

        .. automethod:: ipoll

    .. rubric:: イベントマスクフラグ

    .. autodata:: POLLIN

    .. autodata:: POLLOUT

    .. autodata:: POLLERR

    .. autodata:: POLLHUP

使用例
---------------

このモジュールを使用したデモについては、`projects website`_ を参照してください。

.. _projects website: https://pybricks.com/projects/tutorials/wireless/hub-to-device/pc-keyboard/
