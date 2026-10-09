#!/usr/bin/env pybricks-micropython

# このプログラムを実行する前に、クライアントとサーバーのEV3ブロックが
# Bluetoothでペアリング済みであることを確認してください。ただし接続はしないこと。
# 接続の確立はプログラムが行います。

# サーバーはクライアントより先に起動する必要があります！

from pybricks.messaging import BluetoothMailboxClient, TextMailbox

# これは接続先のリモートEV3またはPCの名前です。
SERVER = 'ev3dev'

client = BluetoothMailboxClient()
mbox = TextMailbox('greeting', client)

print('establishing connection...')
client.connect(SERVER)
print('connected!')

# このプログラムでは、クライアントが最初のメッセージを送信し、その後
# サーバーからの返信を待ちます。
mbox.send('hello!')
mbox.wait()
print(mbox.read())
