import package.Listening.Deal_Hello.dijkstra
import package.settings.setting


def deal_With_Hello_Packet(packet_Router_table, packet_Ip_Mapping):
    flag = True
    # 当收到的hello包中包含的router_Table或者是ip_Mapping有自己没有包含的条目，增加之
    if package.settings.setting.ip_Mapping != packet_Ip_Mapping:
        for item in packet_Ip_Mapping.keys():
            if packet_Ip_Mapping[item] not in package.settings.setting.ip_Mapping:
                package.settings.setting.ip_Mapping[item] = packet_Ip_Mapping[item]
    if packet_Router_table != package.settings.setting.router_Table:
        for item in packet_Router_table.keys():
            if package.settings.setting.router_Table.get(item) != None:
                if package.settings.setting.router_Table[item] != packet_Router_table[item]:
                    for item2 in packet_Router_table[item].keys():
                        package.settings.setting.router_Table[item][item2] = packet_Router_table[item][item2]
            else:
                for item in packet_Router_table[item].keys():
                    package.settings.setting.router_Table[item] = packet_Router_table[item]
    else:
        flag = False
    # 当链路拓扑发生改变的时候才运行dijkstra
    if flag == True:
        print("DEBUG::Produce New Shortest Path")
        package.Listening.Deal_Hello.dijkstra.generate_Shortest_Path()







