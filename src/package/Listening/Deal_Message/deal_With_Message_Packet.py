import socket, threading,sys
sys.path.append("../../../")

# from settings import U
# from settings import V
# from settings import W
# from settings import X
# from settings import Y
from settings.Z import *

def deal_With_Message_Packet(goal_ip, content):
    global HOST
    global Port
    global ip_Mapping
    dataStr = data.decode('utf-8')

    print('DEBUG:----------')
    print('data is %s' %dataStr)

    if goal_ip == ip_Mapping[HOST]:
        print(content)
    else:
        print('Forwarding')

    lock = threading.RLock()
    flag = False
    next_ip = None
    lock.require()

    try:
      global path_Table
      for path in path_Table:
        dest = path[-1]
        if ip_Mapping.get(dest) == goal_ip:
          next_ip = path[1]
          break
    except Exception as e:
      print('except: ', e)
    finally:
      lock.release()

    if flag:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      s.sendto(data, (next_ip, Port))
      s.close()


if __name__ == '__main__':
  HOST = ""
  PORT = 7211
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.bind((HOST, PORT))
  print('listening...')

  while True:
    data, address = s.recvfrom(4096)
    print(data.decode('utf-8'))
    t = threading.Thread(target = handleMessage, args = (data, address))
    t.start()
    t.join()

