import socket, time, json,threading
import package.settings.setting
import copy

# 用于将三个字段序列化
def messages_to_json(type, router_table, ip_mapping, receiver):
    message = dict()
    message['type'] = type

    # 判断，只发送存活节点的信息
    router_Names = []
    for name in receiver:
        if name in router_table[package.settings.setting.HOST]:
            if receiver[name] == False and name != package.settings.setting.HOST:
                router_table[package.settings.setting.HOST].pop(name)
                router_Names.append(name)
        else:
            if receiver[name] == False:
                router_Names.append(name)

    for name in router_Names:
        if name in router_table:
            router_table.pop(name)

    # print("router_table", router_table)
    message['router_Table'] = router_table
    message['ip_Mapping'] = ip_mapping
    json_object = json.dumps(message)
    return json_object

# 用于将heartbeat包序列化
def heartbeat_to_json(type):
    message = dict()
    message['type'] = type
    json_object = json.dumps(message)
    return json_object

# 只向直接连接的节点发送hello包,heartbear包
def send_hello_heartbeat_single():
    directNode = package.settings.setting.router_Table[package.settings.setting.HOST]
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    me = package.settings.setting.ip_Mapping[package.settings.setting.HOST]
    msg = messages_to_json("01", copy.deepcopy(package.settings.setting.router_Table), copy.deepcopy(package.settings.setting.ip_Mapping),copy.deepcopy(package.settings.setting.receiver))
    # print("HERE!!", msg)
    hp = heartbeat_to_json("11")
    # 广播心跳包
    for num in range(2, 254):
        ip = '192.168.199.' + str(num)
        if ip != me:
            s.sendto(hp.encode('utf-8'), (ip, package.settings.setting.Port))
    # 向直接连接的节点发送hello包
    for i in directNode.keys():
        if package.settings.setting.HOST != i:
            ip = package.settings.setting.ip_Mapping[i]
            s.sendto(msg.encode('utf-8'), (ip, package.settings.setting.Port))
    s.close()

# 每隔5秒发送hello和heartbeat包
def send_hello_hearbeat():
    while True:
        rlock = threading.RLock()
        rlock.acquire()
        send_hello_heartbeat_single()
        rlock.release()
        time.sleep(5)
