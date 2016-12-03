import package.Listening.Listening
import package.Forwarding.send_hello
import threading

router_Table = {
  'y':{'w': 1, 'x': 1, 'y': 0, 'z': 2}
}

ip_Mapping = {
  'w': '192.168.199.4',
  'x': '192.168.199.5',
  'y': '192.168.199.6',
  'z': '192.168.199.7'
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
