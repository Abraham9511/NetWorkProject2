import socket, threading, time


def send_hello_single():
    lock = threading.RLock()
    lock.acquire()
    global router_Table
    global ip_Mapping
    global myself
    global Local_PORT
    try:
        msg = '1|'
        msg = msg + str(router_Table) + '|' + str(ip_Mapping)
        directNode = router_Table[myself]
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        for i in directNode.keys():
            ip = ip_Mapping[i]
            s.sendto(msg, (ip, Local_PORT))
        s.close()
    finally:
        lock.release()

def send_hello():
    while True:
        send_hello_single()
        time.sleep(5)
