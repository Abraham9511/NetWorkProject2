import socket,sys
from Deal_Hello.deal_With_Hello_Packet import *
from Deal_Message.deal_With_Message_Packet import *
sys.path.append("../../")
# from settings import U
# from settings import V
# from settings import W
# from settings import X
# from settings import Y
from settings.Z import *

def Listening():
    global HOST
    global Port
    while(True):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.bind((HOST, Port))
            packet, address = s.recvfrom(Port)
            if (packet[0] == '1'):
                deal_With_Hello_Packet(packet)
            else:
                deal_With_Message_Packet(packet)
        except socket.error:
            return "Fail to Listening"
