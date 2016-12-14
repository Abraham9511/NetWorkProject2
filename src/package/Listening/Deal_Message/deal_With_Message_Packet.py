import socket, threading
import package.settings.setting as setting

def deal_With_Message_Packet(goal_ip, content, new_packet):
    print('DEBUG:----------')
    print('content is %s' %content)

    # 如果目的节点是自身，则将数据包进行输出
    # 否则，根据迪杰特斯拉路径取得下一个节点，将数据包发出
    if goal_ip == setting.ip_Mapping[setting.HOST]:
        print('Get message: ', content)
    else:
        print('Forwarding')
    flag = False
    next_ip = None
    try:
      for path in setting.path_Table:
        dest = path[-1]
        # 取得下一个节点
        if setting.ip_Mapping[dest] == goal_ip:
          next_ip = setting.ip_Mapping[path[1]]
          break
    except Exception as e:
      print('except: ', e)
    if flag:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      s.sendto(content, (next_ip, setting.Port))
      s.close()




