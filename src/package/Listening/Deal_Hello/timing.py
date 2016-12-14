import time, threading
import package.settings.setting

def timing():
  router_Names = []
  for name in package.settings.setting.receiver:
    if name in package.settings.setting.router_Table[package.settings.setting.HOST]:
      if package.settings.setting.receiver[name] == False:
        package.settings.setting.router_Table[package.settings.setting.HOST].pop(name)
        router_Names.append(name)
    else:
      if package.settings.setting.receiver[name] == False:
        router_Names.append(name)
  for name in router_Names:
    if name in package.settings.router_Table:
      package.settings.setting.router_Table.pop(name)

  for name in package.settings.setting.receiver:
    package.settings.setting.receiver[name] = False

def cycle():
    while True:
      time.sleep(30)
      rlock = threading.RLock()
      rlock.acquire()
      timing()
      rlock.release()

