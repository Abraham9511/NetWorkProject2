import socket, time, json,threading
import package.settings.setting

def messages_to_json(type, router_table, ip_mapping):
    message = dict()
    message['type'] = type
    message['router_Table'] = router_table
    message['ip_Mapping'] = ip_mapping
    json_object = json.dumps(message)
    return json_object

def heartbeat_to_json(type):
    message = dict()
    message['type'] = type
    json_object = json.dumps(message)
    return json_object

def send_hello_single():
    try:
        directNode = package.settings.setting.router_Table[package.settings.setting.HOST]
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        me = package.settings.setting.ip_Mapping[package.settings.setting.HOST]
        msg = messages_to_json("01", package.settings.setting.router_Table, package.settings.setting.ip_Mapping)
        hp = heartbeat_to_json("11")
        for num in range(2, 254):
            ip = '192.168.199.' + str(num)
            if ip != me:
                s.sendto(hp.encode('utf-8'), (ip, package.settings.setting.Port))
        for i in directNode.keys():
            if package.settings.setting.HOST != i:
                ip = package.settings.setting.ip_Mapping[i]
                s.sendto(msg.encode('utf-8'), (ip, package.settings.setting.Port))
        s.close()
    except Exception as e:
      print('DEBUG::Except: ', e)

def send_hello():
    while True:
        rlock = threading.RLock()
        rlock.acquire()
        send_hello_single()
        rlock.release()
        time.sleep(5)
