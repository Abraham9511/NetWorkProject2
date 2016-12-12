from package.Listening.Listening import *
from package.Forwarding.send_hello import *
from package.Forwarding.send_message import *
from package.Listening.Deal_Hello.deal_With_Hello_Packet import *

import package.settings.setting

import threading


if __name__=="__main__":

    deal_With_Hello_Packet(package.settings.setting.router_Table, package.settings.setting.ip_Mapping)

    forwarding = threading.Thread(target = send_hello)
    forwarding.start()
    print("DEBUG: Start forwarding")

    listening = threading.Thread(target = Listening)
    listening.start()
    print("DEBUG: Start listening")

    app = Application()
    app.master.title('Send Message')
    app.mainloop()

    forwarding.join()
    listening.join()
