#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Color
from pybricks.tools import DataLog

# my_file.txt というデータログファイルを作成する
data = DataLog('time', 'angle', name='my_file', timestamp=False, extension='txt')

# logメソッドは print() メソッドで1行のテキストを追加する。
# つまり、数値の保存以外にもいろいろできる。例:
data.log('Temperature', 25)
data.log('Sunday', 'Monday', 'Tuesday')
data.log({'Kiwi': Color.GREEN}, {'Banana': Color.YELLOW})

# ファイルをコンピューターにアップロードできるが、データを直接表示することもできる:
print(data)
