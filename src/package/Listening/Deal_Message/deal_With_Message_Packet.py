import socket, threading
# import package.settings.U
# import package.settings.V
# import package.settings.W
# import package.settings.X
# import package.settings.Y
import package.settings.setting

def deal_With_Message_Packet(goal_ip, content):
    global ip_Mapping
    content = content.decode('utf-8')

    print('DEBUG:----------')
    print('content is %s' %content)

    if goal_ip == ip_Mapping[package.settings.setting.HOST]:
        print(content)
    else:
        print('Forwarding')

    # lock = threading.RLock()
    flag = False
    next_ip = None
    # lock.require()

    try:
      for path in package.settings.setting.path_Table:
        dest = path[-1]
        if ip_Mapping.get(dest) == goal_ip:
          next_ip = path[1]
          break
    except Exception as e:
      print('except: ', e)
    # finally:
    #   lock.release()

    if flag:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      s.sendto(content, (next_ip, package.settings.setting.Port))
      s.close()




