import socket, time, json
import package.settings.setting as setting

def messages_to_json(type, router_table, ip_mapping):
    message = dict()
    message['type'] = type
    message['router_Table'] = router_table
    message['ip_Mapping'] = ip_mapping
    json_object = json.dumps(message)
    return json_object


def send_hello_single():
    try:
        msg = messages_to_json("1", setting.router_Table, setting.ip_Mapping)
        directNode = setting.router_Table[setting.HOST]
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        me = setting.ip_Mapping[setting.HOST]
        for num in range(2, 254):
            ip = '192.168.199.' + str(num)
            if ip != me:
                s.sendto(msg.encode('utf-8'), (ip, setting.Port))
        # for i in directNode.keys():
        #     if setting.HOST != i:
        #         ip = setting.ip_Mapping[i]
        #         s.sendto(msg.encode('utf-8'), (ip, setting.Port))
        s.close()
    except Exception as e:
      print('DEBUG::Except: ', e)

def send_hello():
    while True:
        send_hello_single()
        time.sleep(5)
