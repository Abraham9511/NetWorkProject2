import socket, threading, time,json
import package.settings.setting

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
        msg = messages_to_json('1', package.settings.setting.router_Table, package.settings.setting.ip_Mapping)
        directNode = package.settings.setting.router_Table[package.settings.setting.HOST]
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        for i in directNode.keys():
            if package.settings.setting.HOST != i:
                ip = package.settings.setting.ip_Mapping[i]
                s.sendto(msg.encode('utf-8'), (ip, package.settings.setting.Port))
        s.close()
    except Exception as e:
      print('DEBUG::Except: ', e)

def send_hello():
    while True:
        send_hello_single()
        time.sleep(5)
