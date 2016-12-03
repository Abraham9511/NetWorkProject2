import Deal_Message.deal_With_Hello_Packet
import Deal_Message.deal_With_Message_Packet
import socket

def Listening():
    while(True):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.bind((HOST, PORT))
            packet, address = s.recvfrom(PORT)
            if (packet[0] == '1'):
                deal_With_Hello_Packet(packet)
            else:
                deal_With_Message_Packet(packet)
        except socket.error:
            return "Fail to Listening"
