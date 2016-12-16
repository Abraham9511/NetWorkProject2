import socket,json, threading
from .Deal_Hello.deal_With_Hello_Packet import *
from .Deal_Message.deal_With_Message_Packet import *
import package.settings.setting


def Listening():
    # 传输曾采用UDP
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(("", package.settings.setting.Port))
    except socket.error:
        print("DEBUG::Listenning Cant't bind port")
    #
    while True:
        try:
            # 获取线程锁，因为以下部分需门需要对setting文件中的全局变量进行读写操作
            rlock = threading.RLock()
            rlock.acquire()
            new_packet, address = s.recvfrom(package.settings.setting.Port)
            # 若是空消息，忽略
            if new_packet == '':
                rlock.release()
                continue
            # 对取到的文件二进制流先utf-8解码，再反序列化
            packet = json.loads(new_packet.decode('utf-8'))
            # 根据头部type判断是hello，message，heartbeat包，类型分别对应的是00 01 11
            if (packet['type'] == '01'):
                print("DEBUG::This is Hello Packet")
                packet_router_table = packet['router_Table']
                packet_ip_mapping = packet['ip_Mapping']
                deal_With_Hello_Packet(packet_router_table, packet_ip_mapping)
            elif packet['type'] == '00':
                print("DEBUG::This is Message Packet")
                goal_ip = packet['goal_ip']
                content = packet['content']
                # 此处传递new_packet是方便方便整个包直接转发
                deal_With_Message_Packet(goal_ip, content, new_packet)
            elif packet['type'] == '11':
                print("DEBUG::This is Heartbeat Packet")
                name = getName(address[0])
                package.settings.setting.receiver[name] = True
            # 在控制台输出router_Table更新之后信息
            print(package.settings.setting.router_Table)
            rlock.release()
        except socket.error:
            print("DEBUG::Fail to Listening\n")

# 获取ip对应的HOST
def getName(source_ip):
    if package.settings.setting.ip_Mapping != None:
        for name in package.settings.setting.ip_Mapping:
            if package.settings.setting.ip_Mapping[name] == source_ip:
                return name
