import package.Listening.Listening
import package.Forwarding.send_hello
import threading

router_Table = {
  'u':{'u': 0, 'v': 2, 'w': 5, 'x': 1}
}

ip_Mapping = {
  'u': '192.168.199.2',
  'v': '192.168.199.3',
  'w': '192.168.199.4',
  'x': '192.168.199.5'
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
