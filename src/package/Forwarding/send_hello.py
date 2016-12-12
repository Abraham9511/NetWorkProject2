import socket, threading, time,json
# import package.settings.U
# import package.settings.V
# import package.settings.W
# import package.settings.X
# import package.settings.Y
import package.settings.Z

def messages_to_json(type, router_table, ip_mapping):
    message = dict()
    message['type'] = type
    message['router_Table'] = router_table
    message['ip_Mapping'] = ip_mapping
    json_object = json.dumps(message)
    return json_object


def send_hello_single():
    # lock = threading.RLock()
    # lock.acquire()
    try:
        msg = messages_to_json('1', package.settings.Z.router_Table, package.settings.Z.ip_Mapping)
        directNode = package.settings.Z.router_Table[package.settings.Z.HOST]
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        for i in directNode.keys():
            if package.settings.Z.HOST != i:
                ip = package.settings.Z.ip_Mapping[i]
                s.sendto(msg.encode('utf-8'), (ip, package.settings.Z.Port))
        s.close()
    except Exception as e:
      print('DEBUG::Except: ', e)
    # finally:
    #     lock.release()


def send_hello():
    while True:
        send_hello_single()
        time.sleep(5)
