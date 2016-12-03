import socket, threading

def handleMessage(data):
    global myself
    global PORT
    dataStr = data.decode('utf-8')

    print('DEBUG:----------')
    print('data is %s' %dataStr)

    dataArray = dataStr.split('|');
    if dataArray[1] == myself:
        print(dataArray[2])
    else:
        print('转发')

    lock = threading.RLock()
    flag = False
    next_ip = None
    lock.require()

    try:
      global path_Table
      global ip_Mapping
      for path in path_Table:
        dest = path[-1]
        if ip_Mapping.get(dest) == dataArray[1]:
          next_ip = path[1]
          break
    except Exception as e:
      print('except: ', e)
    finally:
      lock.release()

    if flag:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      s.sendto(data, (next_ip, PORT))
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

