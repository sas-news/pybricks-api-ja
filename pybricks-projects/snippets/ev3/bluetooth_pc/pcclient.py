#!/usr/bin/env python3
from pybricks.messaging import BluetoothMailboxClient, TextMailbox

# このデモは、PCからBluetooth経由でEV3と通信します。
#
# ../bluetooth_client のEV3クライアント例と同じ内容です。
#
# 違うのは、こちらに同梱したmessagingモジュールのPython3実装を使って
# コンピューター上のPython3で動かす点だけです。
# EV3からは、普通のEV3クライアントと通信しているように見えます。
#
# そのためEV3側のサーバー例は変更不要です。接続手順も
# messagingモジュールのドキュメントと同じです:
# https://docs.pybricks.com/en/latest/messaging.html
#
# PCとEV3のBluetoothをオンにしてください。EV3側でBluetoothを
# 検出可能にする必要があるかもしれません。EV3のアドレスが
# 分かっている場合はペアリングを省略できます。

# 接続先のサーバーEV3のアドレスです。
SERVER = 'CC:78:AB:D8:4E:F6'

client = BluetoothMailboxClient()
mbox = TextMailbox('greeting', client)

print('establishing connection...')
client.connect(SERVER)
print('connected!')

# このプログラムでは、クライアントが最初にメッセージを送信し、
# サーバーからの返信を待ちます。
mbox.send('hello!')
mbox.wait()
print(mbox.read())
