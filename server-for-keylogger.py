# -*- coding: utf-8 -*-
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = ('192.168.1.187', 5050)

try:
   s.bind(server)
except OSError:
   try:
      server = ('', 5050)

      s.bind(server)
   except OSError:
      print('Неверный хост')
      exit()

data, addr = s.recvfrom(1024)
if data.decode('utf-8') == '13554':
   s.sendto('13554', (addr, 5050))

   path = 'log' + addr + '.txt'
   f = open(path, 'a')
   f.write('\n[CONNECT]\n')
   f.close()

