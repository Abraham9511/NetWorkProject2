import threading, sys
from .dijkstra import *
sys.path.append("../../../")

# from settings.U import *
# from settings.V import *
# from settings.W import *
# from settings.X import *
# from settings.Y import *
from settings.Z import *


def deal_With_Hello_Packet(packet_Router_table, packet_Ip_Mapping):
    flag = True
    rlock = threading.RLock()
    rlock.acquire()
    global router_Table
    global ip_Mapping
    if ip_Mapping != packet_Ip_Mapping:
        for item in packet_Ip_Mapping.keys():
            if packet_Ip_Mapping[item] not in ip_Mapping:
                ip_Mapping[item] = packet_Ip_Mapping[item]
    if packet_Router_table != router_Table:
        for item in packet_Router_table.keys():
            if router_Table.get(item) != None:
                if router_Table[item] != packet_Router_table[item]:
                    for item2 in packet_Router_table[item].keys():
                        router_Table[item][item2] = packet_Router_table[item][item2]
            else:
                for item2 in packet_Router_table[item].keys():
                    router_Table[item][item2] = packet_Router_table[item][item2]
    else:
        flag = False
    rlock.release()
    # if flag == True:
    print("DEBUG::Produce New Shortest Path")
    generate_Shortest_Path()









