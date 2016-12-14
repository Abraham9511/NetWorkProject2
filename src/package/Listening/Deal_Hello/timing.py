import time
import package.settings.setting

def timing():
  for name in package.settings.setting.receiver:
    package.settings.setting.receiver[name] = False
  time.sleep(30)
  router_Self = package.settings.setting.router_Table[package.settings.setting.HOST]
  router_Names = []
  if package.settings.setting.receiver != None:
    for name in package.settings.setting.receiver:
      if package.settings.setting.receiver[name] == False:
        router_Self.pop(name)
        router_Names.append(name)

  for name in router_Names:
    package.settings.setting.router_Table.pop(name)
