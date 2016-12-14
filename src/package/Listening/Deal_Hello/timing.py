import time, threading
import package.settings.setting

def timing():
  try:
    router_Names = []
    if package.settings.setting.receiver != None:
      for name in package.settings.setting.receiver:
        if name in package.settings.setting.router_Table.keys() and package.settings.setting.receiver[name] == False:
          package.settings.setting.router_Table[package.settings.setting.HOST].pop(name)
          router_Names.append(name)
    for name in router_Names:
      package.settings.setting.router_Table.pop(name)

    for name in package.settings.setting.receiver:
      package.settings.setting.receiver[name] = False
  except Exception as e:
    print('DEBUG::except: ', e)


def cycle():
    while True:
      time.sleep(30)
      rlock = threading.RLock()
      rlock.acquire()
      timing()
      print(package.settings.setting.router_Table)
      rlock.release()

