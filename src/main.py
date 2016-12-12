from package.Listening.Listening import *
from package.Forwarding.send_hello import *
from package.Forwarding.send_message import *
from package.Listening.Deal_Hello.deal_With_Hello_Packet import *

# import package.settings.U
# import package.settings.V
# import package.settings.W
# import package.settings.X
# import package.settings.Y
import package.settings.Z

import threading


if __name__=="__main__":

    deal_With_Hello_Packet(package.settings.Z.router_Table, package.settings.Z.ip_Mapping)

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
