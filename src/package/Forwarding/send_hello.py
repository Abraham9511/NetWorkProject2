import socket, threading, time,sys
sys.path.append("../../")

# from settings import U
# from settings import V
# from settings import W
# from settings import X
# from settings import Y
from settings.Z import *

def send_hello_single():
    lock = threading.RLock()
    lock.acquire()
    global router_Table
    global ip_Mapping
    global HOST
    global Port
    try:
        msg = '1|'
        msg = msg + str(router_Table) + '|' + str(ip_Mapping)
        directNode = router_Table[HOST]
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        for i in directNode.keys():
            ip = ip_Mapping[i]
            s.sendto(msg, (ip, Port))
        s.close()
    finally:
        lock.release()


def send_hello():
    while True:
        send_hello_single()
        time.sleep(5)
