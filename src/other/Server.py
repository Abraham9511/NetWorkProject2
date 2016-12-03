import socket, commands

if __name__=="__main__":
    HOST = ""
    PORT = 7211
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((HOST, PORT))
    data, address = s.recvfrom(4096)
    print data
