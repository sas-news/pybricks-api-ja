# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2020 The Pybricks Authors

"""時間計測とデータロギングのための共通ツール。"""


def wait(time):
    """指定した時間だけユーザープログラムを一時停止します。

    Arguments:
        time (:ref:`time`): 待機する時間。

    """
    pass


class StopWatch:
    """時間間隔を測定するストップウォッチです。携帯電話の
    ストップウォッチ機能に似ています。"""

    def __init__(self):
        pass

    def time(self):
        """ストップウォッチの現在の時間を取得します。

        Returns:
            :ref:`time`: 経過時間。
        """
        pass

    def pause(self):
        """ストップウォッチを一時停止します。"""
        pass

    def resume(self):
        """ストップウォッチを再開します。"""
        pass

    def reset(self):
        """ストップウォッチの時間を0にリセットします。

        実行状態は影響を受けません:

        * 一時停止していた場合は、一時停止のままです（ただし0になります）。
        * 実行中だった場合は、実行中のままです（ただし0から再開します）。
        """
        pass


class DataLog:
    """ファイルを作成してデータを記録します。"""

    def __init__(self, *headers, name='log', timestamp=True, extension='csv',
                 append=False):
        """

        Arguments:
            headers (`col1`, `col2`, `...`): 列ヘッダー。データ列の
                名前です。たとえば、 ``'time'`` や ``'angle'`` を選びます。
            name (str): ファイル名。
            timestamp (bool): ``True`` を選択すると、ファイル名に日付と
                時刻が追加されます。これにより、ファイルが一意の名前に
                なります。 ``False`` を選択すると、タイムスタンプは
                省略されます。
            extension (str): ファイルの拡張子。
            append (bool): ``True`` を選択すると、既存のデータログファイルを
                再び開いてデータを追記します。 ``False`` を選択すると、
                既存のデータを消去します。ファイルがまだ存在しない場合は、
                どちらの場合でも空のファイルが作成されます。
        """
        pass

    def log(self, *values):
        """1つ以上の値をファイルの新しい行に保存します。

        Arguments:
            values (object, object, `...`): 1つ以上のオブジェクトまたは値。
        """
        pass
