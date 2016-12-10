import threading, sys
from dijkstra import *
sys.path.append("../../../")
# from settings import U
# from settings import V
# from settings import W
# from settings import X
# from settings import Y
from settings.Z import *


def deal_With_Hello_Packet(hello_Packet):
    flag = True
    rlock = threading.RLock()
    rlock.acquire()
    global router_Table
    global ip_Mapping
    packet_Router_table = hello_Packet.split('|')[1]
    packet_Ip_Mapping = hello_Packet.split('|')[2]
    if ip_Mapping != packet_Ip_Mapping:
        for item in packet_Ip_Mapping.keys():
            if packet_Ip_Mapping[item] not in ip_Mapping:
                ip_Mapping[item] = packet_Ip_Mapping[item]
    if packet_Router_table != router_Table:
        for item in packet_Router_table.key():
            if router_Table.has_key(item) == True:
                if router_Table[item] != packet_Router_table[item]:
                    for item2 in packet_Router_table[item].keys():
                        router_Table[item][item2] = packet_Router_table[item][item2]
            else:
                for item2 in packet_Router_table[item].keys():
                    router_Table[item][item2] = packet_Router_table[item][item2]
    else:
        flag = False
    rlock.release()
    if flag == True:
        generate_Shortest_Path()









