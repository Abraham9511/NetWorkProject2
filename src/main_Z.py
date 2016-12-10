from package.Listening.Listening import *
from package.Forwarding.send_hello import *
import threading


if __name__=="__main__":

    forwarding = threading.Thread(target = send_hello)
    forwarding.start()
    print("DEBUG: Start forwarding")

    listening = threading.Thread(target = Listening)
    listening.start()
    print("DEBUG: Start listening")

    forwarding.join()
    listening.join()
