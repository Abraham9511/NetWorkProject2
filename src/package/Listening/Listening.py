import socket,sys, json
from Deal_Hello.deal_With_Hello_Packet import *
from Deal_Message.deal_With_Message_Packet import *
sys.path.append("../../")

# from settings.U import *
# from settings.V import *
# from settings.W import *
# from settings.X import *
# from settings.Y import *
from settings.Z import *

def Listening():
    global HOST
    global Port
    global ip_Mapping
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((ip_Mapping[HOST], Port))
    except socket.error:
        print("DEBUG:: Listenning Cant't bind port")
    while True:
        try:
            packet, address = s.recvfrom(Port)
            print("DEBUG:PACKET:"+packet)
            if packet == '':
                continue
            packet = json.loads(packet.decode('utf-8'))
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
        except socket.error:
            print("DEBUG::Fail to Listening\n")
