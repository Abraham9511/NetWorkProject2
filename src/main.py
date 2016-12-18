from package.Listening.Listening import *
from package.Forwarding.send_hello import *
from package.Forwarding.send_message import *
from package.Listening.Deal_Hello.deal_With_Hello_Packet import *
from package.Listening.Deal_Hello.timing import *
import package.settings.setting
import threading


if __name__=="__main__":
    timing_start = threading.Thread(target = cycle)
    timing_start.start()
    print("DEBUG: Start timing")

    package.Listening.Deal_Hello.dijkstra.generate_Shortest_Path()

    forwarding = threading.Thread(target = send_hello_hearbeat)
    forwarding.start()
    print("DEBUG: Start forwarding")

    listening = threading.Thread(target = Listening)
    listening.start()
    print("DEBUG: Start listening")

    app = Application()
    app.master.title('Send Message')
    app.mainloop()

    timing_start.join()
    forwarding.join()
    listening.join()
