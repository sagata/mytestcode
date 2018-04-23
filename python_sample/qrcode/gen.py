# encoding=utf-8

import qrcode 
img = qrcode.make('http://192.168.40.195:8009/get_ip')
img.save('test.png')