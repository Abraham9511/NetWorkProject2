from tkinter import *
import tkinter.messagebox as messagebox
import socket, threading, time,sys, json
sys.path.append("../../")

# from settings.U import *
# from settings.V import *
# from settings.W import *
# from settings.X import *
# from settings.Y import *
from settings.Z import *


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
    global router_Table
    global ip_Mapping
    global HOST
    global Port
    try:
      if dest == None:
        messagebox.showinfo('Message', 'Please input the destination ip address!')
      elif ip_Mapping.get(dest) == None:
        messagebox.showinfo('Message', 'The destination ip address does not exist!')
      elif message == None:
        messagebox.showinfo('Message', 'Please input the message!')
      else:
        destIp = ip_Mapping.get(dest)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(json.dumps(message).encode('utf-8'), (ip, Port))
        s.close()
    finally:
      lock.release()


app = Application()
app.master.title('Send Message')
app.mainloop()
