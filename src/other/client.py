import socket, commands, uuid

def get_Local_Ip():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(('8.8.8.8', 80))
        (addr, port) = sock.getsockname()
        sock.close()
        return str(addr)
    except socket.error:
        return "Get Local IP Error"

if __name__=="__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    Local_PORT=7211
    #s.bind(('127.0.0.1', Local_PORT))
    prefix = '192.168.199.'
    for i in range(1,255):
#        ip = prefix + str(i)
        my_Ip = get_Local_Ip()
        print(my_Ip)
#        s.sendto("Hello, i am "+ my_Ip,(ip, Local_PORT))
    s.close()







