import package.Listening.Deal_Hello.dijkstra
import package.settings.setting as setting

def deal_With_Hello_Packet(packet_Router_table, packet_Ip_Mapping):
    flag = True
    if setting.ip_Mapping != packet_Ip_Mapping:
        for item in packet_Ip_Mapping.keys():
            if packet_Ip_Mapping[item] not in setting.ip_Mapping:
                setting.ip_Mapping[item] = packet_Ip_Mapping[item]
    if packet_Router_table != setting.router_Table:
        for item in packet_Router_table.keys():
            if setting.router_Table.get(item) != None:
                if setting.router_Table[item] != packet_Router_table[item]:
                    for item2 in packet_Router_table[item].keys():
                        setting.router_Table[item][item2] = packet_Router_table[item][item2]
            else:
                for item2 in packet_Router_table[item].keys():
                    setting.router_Table[item] = packet_Router_table[item]
    else:
        flag = False
    if flag == True:
        print("DEBUG::Produce New Shortest Path")
        package.Listening.Deal_Hello.dijkstra.generate_Shortest_Path()







