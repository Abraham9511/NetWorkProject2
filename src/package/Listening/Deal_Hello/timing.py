import time
import package.settings.setting as setting

def timing():
  for name in setting.receiver:
    setting.receiver[name] = False
  time.sleep(30)
  router_Self = setting.router_Table[setting.HOST]
  router_Names = []
  for name, value in setting.receiver:
    if value == False:
      router_Self.pop(name)
      router_Names.append(name)

  for name in router_Names:
    setting.router_Table.pop(name)
