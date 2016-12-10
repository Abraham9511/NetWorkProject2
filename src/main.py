from package.Listening.Listening import *
from package.Forwarding.send_hello import *
from package.Listening.Deal_Hello.deal_With_Hello_Packet import *

import settings.Z
# import settings.X
# import settings.Y
# import settings.U
# import settings.V
# import settings.W

import threading


if __name__=="__main__":
    global router_Table
    global ip_Mapping
    deal_With_Hello_Packet(router_Table, ip_Mapping)

    forwarding = threading.Thread(target = send_hello)
    forwarding.start()
    print("DEBUG: Start forwarding")

    listening = threading.Thread(target = Listening)
    listening.start()
    print("DEBUG: Start listening")


    forwarding.join()
    listening.join()
