import socket,json, threading
from .Deal_Hello.deal_With_Hello_Packet import *
from .Deal_Message.deal_With_Message_Packet import *
import package.settings.setting as setting

def Listening():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        port = setting.Port
        s.bind(("", port))
    except socket.error:
        print("DEBUG:: Listenning Cant't bind port")
    while True:
        try:
            rlock = threading.RLock()
            rlock.acquire()
            new_packet, address = s.recvfrom(setting.Port)
            if new_packet == '':
                continue
            packet = json.loads(new_packet.decode('utf-8'))
            print(packet)
            if (packet['type'] == '1'):
                print("DEBUG::This is Hello Packet")
                name = getName(address[0])
                packet.settings.setting.receiver[name] = True
                packet_router_table = packet['router_Table']
                packet_ip_mapping = packet['ip_Mapping']
                deal_With_Hello_Packet(packet_router_table, packet_ip_mapping)
            else:
                print("DEBUG::This is Message Packet")
                goal_ip = packet['goal_ip']
                content = packet['content']
                deal_With_Message_Packet(goal_ip, content, new_packet)
            rlock.release()
        except socket.error:
            print("DEBUG::Fail to Listening\n")


def getName(source_ip):
    for name, ip in packet.settings.setting.ip_Mapping:
        if ip == source_ip:
            return name
