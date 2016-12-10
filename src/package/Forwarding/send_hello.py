import socket, threading, time,sys, json
sys.path.append("../../")

# from settings.U import *
# from settings.V import *
# from settings.W import *
# from settings.X import *
# from settings.Y import *
from settings.Z import *

def messages_to_json(type, router_table, ip_mapping):
    message = dict()
    message['type'] = type
    message['router_Table'] = router_table
    message['ip_Mapping'] = ip_mapping
    json_object = json.dumps(message)
    return json_object


def send_hello_single():
    lock = threading.RLock()
    lock.acquire()
    global router_Table
    global ip_Mapping
    global HOST
    global Port
    try:
        msg = messages_to_json('1', router_Table, ip_Mapping)
        directNode = router_Table[HOST]
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        for i in directNode.keys():
            if HOST != i:
                ip = ip_Mapping[i]
                s.sendto(msg, (ip, Port))
        s.close()
    finally:
        lock.release()


def send_hello():
    while True:
        send_hello_single()
        time.sleep(5)
