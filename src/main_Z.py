import package.Listening.Listening
import package.Forwarding.send_hello
import threading

router_Table = {
  'z':{'w': 5, 'y': 2, 'z': 0}
}

ip_Mapping = {
  'w': '192.168.199.208',
  'y': '192.168.199.6',
  'z': '192.168.199.6'
}

path_Table = list()

if __name__=="__main__":

    forwarding = threading.Thread(target = package.Forwarding.send_hello)
    forwarding.start()
    print("DEBUG: Start forwarding")

    listening = threading.Thread(target = package.Listening.Listening)
    listening.start()
    print("DEBUG: Start listening")

    forwarding.join()
    listening.join()
