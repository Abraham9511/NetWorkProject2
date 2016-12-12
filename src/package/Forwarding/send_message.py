from tkinter import *
import tkinter.messagebox as messagebox
import socket, threading, json
import package.settings.setting


def messages_to_json(type, goal_ip, content):
  message = dict()
  message['type'] = type
  message['goal_ip'] = goal_ip
  message['content'] = content
  json_object = json.dumps(message)
  return json_object

class Application(Frame):
  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.pack()
    self.createWidgets()

  def createWidgets(self):
    self.destInput = Entry(self)
    self.destInput.pack(side = LEFT)
    self.messageInput = Entry(self)
    self.messageInput.pack(side = LEFT)
    self.quitButton = Button(self, text='SEND', command=self.send_message)
    self.quitButton.pack(side = BOTTOM)

  def send_message(self):
    dest = self.destInput.get() or None
    message = self.messageInput.get() or None

    lock = threading.RLock()
    lock.acquire()
    try:
      if dest == None:
        messagebox.showinfo('Message', 'Please input the destination ip address!')
      elif package.settings.setting.ip_Mapping[dest] == None:
        messagebox.showinfo('Message', 'The destination ip address does not exist!')
      elif message == None:
        messagebox.showinfo('Message', 'Please input the message!')
      else:
        destIp = package.settings.setting.ip_Mapping[dest]
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        for dst in package.settings.setting.path_Table:
          if dst[-1] == dest:
            path = dst
            print("PATH %s" % path)
            break
        ip = package.settings.setting.ip_Mapping[path[1]]
        s.sendto(messages_to_json("0",destIp, message).encode('utf-8'), (ip, package.settings.setting.Port))
        s.close()
    finally:
      lock.release()

