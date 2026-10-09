#!/usr/bin/env pybricks-micropython

# このプログラムを実行する前に、クライアントとサーバーのEV3ブロックが
# Bluetoothでペアリング済みであることを確認してください。ただし接続はしないこと。
# 接続の確立はプログラムが行います。

# サーバーはクライアントより先に起動する必要があります！

from pybricks.messaging import BluetoothMailboxServer, TextMailbox

server = BluetoothMailboxServer()
mbox = TextMailbox('greeting', server)

# サーバーはクライアントより先に起動する必要があります！
print('waiting for connection...')
server.wait_for_connection()
print('connected!')

# このプログラムでは、サーバーはクライアントからの最初のメッセージを待ち、
# その後に返信を送信します。
mbox.wait()
print(mbox.read())
mbox.send('hello to you!')
