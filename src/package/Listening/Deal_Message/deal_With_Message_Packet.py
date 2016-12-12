import socket, threading
# import package.settings.U
# import package.settings.V
# import package.settings.W
# import package.settings.X
# import package.settings.Y
import package.settings.setting

def deal_With_Message_Packet(goal_ip, content, new_packet):
    print('DEBUG:----------')
    print('content is %s' %content)

    if goal_ip == package.settings.setting.ip_Mapping[package.settings.setting.HOST]:
        print(content)
    else:
        print('Forwarding')
    flag = False
    next_ip = None
    try:
      for path in package.settings.setting.path_Table:
        dest = path[-1]
        if package.settings.setting.ip_Mapping[dest] == goal_ip:
          next_ip = package.settings.setting.ip_Mapping[path[1]]
          break
    except Exception as e:
      print('except: ', e)
    if flag:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      s.sendto(content, (next_ip, package.settings.setting.Port))
      s.close()




