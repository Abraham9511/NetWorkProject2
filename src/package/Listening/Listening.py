import socket,sys, json, threading
from .Deal_Hello.deal_With_Hello_Packet import *
from .Deal_Message.deal_With_Message_Packet import *

# import package.settings.U
# import package.settings.V
# import package.settings.W
# import package.settings.X
# import package.settings.Y
import package.settings.Z

def Listening():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        port = package.settings.Z.Port
        s.bind(("", port))
    except socket.error:
        print("DEBUG:: Listenning Cant't bind port")
    while True:
        try:
            rlock = threading.RLock()
            rlock.acquire()
            packet, address = s.recvfrom(package.settings.Z.Port)
            if packet == '':
                continue
            packet = json.loads(packet.decode('utf-8'))
            print(packet)
            if (packet['type'] == '1'):
                print("DEBUG::This is Hello Packet")
                packet_router_table = packet['router_Table']
                packet_ip_mapping = packet['ip_Mapping']
                deal_With_Hello_Packet(packet_router_table, packet_ip_mapping)
            else:
                print("DEBUG::This is Message Packet")
                goal_ip = packet['goal_ip']
                content = packet['content']
                deal_With_Message_Packet(goal_ip, content)
            rlock.release()
        except socket.error:
            print("DEBUG::Fail to Listening\n")
