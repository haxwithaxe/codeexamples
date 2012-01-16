#!/usr/bin/env python

## License:
#	Public Domain
#
## Example of basic socket usage

import socket

mysock = socket.socket()
mysock.connect(('kuppa.ctrlaltirc.net',6667))
mysock.send('NICK examplenick\r\nUSER examplenick kuppa.ctrlaltirc.net bla :examplenick\r\nJOIN :#lobby\r\nPRIVMSG #lobby :\x01ACTION is an example\x01\r\nQUIT :bye :)\r\n')
recvdata = mysock.recv(1024)
repr(recvdata)
mysock.close()
