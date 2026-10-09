:mod:`tools <pybricks.tools>` -- 時間計測とデータロギング
=======================================================================

.. automodule:: pybricks.tools
    :no-members:

.. autofunction:: wait

.. autoclass:: pybricks.tools.StopWatch
    :no-members:

    .. automethod:: pybricks.tools.StopWatch.time

    .. automethod:: pybricks.tools.StopWatch.pause

    .. automethod:: pybricks.tools.StopWatch.resume

    .. automethod:: pybricks.tools.StopWatch.reset

.. autoclass:: pybricks.tools.DataLog
    :no-members:

    .. automethod:: pybricks.tools.DataLog.log

    デフォルトでは、このクラスはEV3ブロック上に ``log`` という名前と
    現在の日時を含む ``csv`` ファイルを作成します。たとえば、
    2020年2月13日10時07分44.431260秒にこのクラスを使用すると、
    ファイル名は ``log_2020_02_13_10_07_44_431260.csv`` になります。

    ログファイルをコンピューターにアップロードする方法については、
    :ref:`EV3上のファイル管理 <managefiles>` を参照してください。

.. toggle-header::
    :header: **例を表示/非表示: 測定値の記録と可視化**



    **例**

    この例では、時間の経過とともに回転するホイールの角度を記録する
    方法を示します。

    .. literalinclude:: ../../pybricks-projects/snippets/ev3/datalog/main.py

    この例では、生成されたファイルの内容は次のとおりです::

        time, angle
        3, 0
        108, 6
        212, 30
        316, 71
        419, 124
        523, 176
        628, 228
        734, 281
        838, 333
        942, 385

    上記のようにファイルをコンピューターにアップロードすると、
    スプレッドシートエディターで開くことができます。そこでデータの
    グラフを作成できます（ :numref:`fig_datalog_graph` 参照）。

    この例では、モーター角度が最初はゆっくり変化していることが
    わかります。その後、角度の変化が速くなり、グラフは直線になります。
    これは、モーターが一定速度に達したことを意味します。角度が
    毎秒500度ずつ増加していることが確認できます。

    .. _fig_datalog_graph:

    .. figure:: ../api/images/datalog_graph.png
        :width: 100 %

        元のファイル内容（左）と生成されたグラフ（右）。


.. toggle-header::
    :header: **例を表示/非表示: オプション引数の使用**

    **例**

    この例では、数値以外のデータを記録する方法を示します。また、
    ``DataLog`` クラスのオプション引数を使ってファイル名と拡張子を
    選択する方法も示します。

    この例では ``timestamp=False`` となっており、日付と時刻は
    ファイル名に追加されません。ファイル名が常に同じになるため
    便利ですが、このスクリプトを実行するたびに ``my_file.txt`` の
    内容が上書きされることになります。

    .. literalinclude:: ../../pybricks-projects/snippets/ev3/datalog_extra/main.py
