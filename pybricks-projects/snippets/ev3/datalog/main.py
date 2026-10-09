#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.tools import DataLog, StopWatch, wait

# EV3ブロックのプロジェクトフォルダにデータログファイルを作成する。
# * デフォルトでは、ファイル名に現在の日付と時刻が含まれる。例:
#   log_2020_02_13_10_07_44_431260.csv
# * データ列のタイトルをオプションで指定できる。たとえば、
#   ある時刻のモーター角度を記録したい場合は、次のようにする:
data = DataLog('time', 'angle')

# モーターを初期化して動かす
wheel = Motor(Port.B)
wheel.run(500)

# 経過時間を測定するストップウォッチを開始する
watch = StopWatch()

# 時刻とモーター角度を10回記録する
for i in range(10):
    # 角度と時刻を読み取る
    angle = wheel.angle()
    time = watch.time()

    # log() メソッドを使うたびに、データを含む新しい行が
    # ファイルに追加される。値はいくつでも追加できる。
    # この例では、現在の時刻とモーター角度を保存する:
    data.log(time, angle)

    # モーターが少し動けるようしばらく待つ
    wait(100)

# これでファイルをコンピューターにアップロードできる
