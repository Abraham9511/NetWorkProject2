import package.Listening.Listening
import package.Forwarding.send_hello
import threading

router_Table = {
  'w':{'u': 5, 'v': 3, 'w': 0, 'x': 3, 'y': 1, 'z': 5}
}

ip_Mapping = {
  'u': '192.168.199.2',
  'v': '192.168.199.60',
  'w': '192.168.199.208',
  'x': '192.168.199.5',
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
