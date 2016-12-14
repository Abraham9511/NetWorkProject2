## All make sense ##
Port = 2711
INF = 9999
path_Table = list()

# ## u setting ##
# HOST = 'u'
# router_Table = {
#   'u': {'u': 0, 'v': 2, 'w': 5, 'x': 1},
#   'v': {'v': 0, 'u': 2},
#   'w': {'w': 0, 'u': 5},
#   'x': {'x': 0, 'u': 1}
# }
#
# ip_Mapping = {
#   'u': '192.168.199.69',
#   'v': '192.168.199.138',
#   'w': '192.168.199.208',
#   'x': '192.168.199.69'
# }
# 
# receiver = {
#   'v': False,
#   'w': False,
#   'x': False,
#   'y': False,
#   'z': False
# }
#
#
# ## v ##
# HOST = 'v'
#
# router_Table = {
#   'v': {'u': 2, 'v': 0, 'w': 3, 'x': 2},
#   'u': {'u': 0, 'v': 2},
#   'w': {'w': 0, 'v': 3},
#   'x': {'x': 0, 'v': 2}
# }
#
# ip_Mapping = {
#   'u': '192.168.199.69',
#   'v': '192.168.199.138',
#   'w': '192.168.199.208',
#   'x': '192.168.199.60'
# }
# 
# receiver = {
#   'u': False,
#   'w': False,
#   'x': False,
#   'y': False,
#   'z': False
# }
#
#
# ## w ##
# HOST = 'w'
#
# router_Table = {
#     'w': {'v': 3, 'w': 0,'z': 5, 'x':3, 'u':5, 'y':1},
#     'v': {'v': 0, 'w': 3},
#     'z': {'w': 5, 'z': 0},
#     'x': {'w': 3, 'x': 0},
#     'u': {'w': 5, 'u': 0},
#     'y': {'w': 1, 'y':0}
# }
#
# ip_Mapping = {
#   'u': '192.168.199.69',
#   'v': '192.168.199.138',
#   'w': '192.168.199.208',
#   'x': '192.168.199.60',
#   'y': '192.168.199.5',
#   'z': '192.168.199.6'
# }
#
# receiver = {
#   'u': False,
#   'v': False,
#   'x': False,
#   'y': False,
#   'z': False
# }
#
#
# ## x ##
# HOST = 'x'
#
# router_Table = {
#   'x': {'u': 1, 'v': 2, 'w': 3, 'x': 0, 'y': 1},
#   'u': {'u': 0, 'x': 1},
#   'v': {'v': 0, 'x': 2},
#   'w': {'w': 0, 'x': 3},
#   'y': {'y': 0, 'x': 1}
# }
#
# ip_Mapping = {
#   'u': '192.168.199.69',
#   'v': '192.168.199.138',
#   'w': '192.168.199.208',
#   'x': '192.168.199.60',
#   'y': '192.168.199.5'
# }
#
# receiver = {
#   'u': False,
#   'v': False,
#   'w': False,
#   'y': False,
#   'z': False
# }
#
#
# ## y ##
# HOST = 'y'
#
# router_Table = {
#     'y':{'y':0, 'x': 1, 'w': 1, 'z': 2},
#     'x':{'x': 0, 'y': 1},
#     'z':{'z': 0, 'y': 2},
#     'w':{'w': 0, 'y': 1}
# }
#
# ip_Mapping = {
#     'w': '192.168.199.208',
#     'y': '192.168.199.5',
#     'z': '192.168.199.6',
#     'x': '192.168.199.60'
# }
# 
# receiver = {
#   'u': False,
#   'v': False,
#   'w': False,
#   'x': False,
#   'z': False
# }
#
#
## z ##
HOST = 'z'

router_Table = {
    'z':{'w': 5, 'z': 0, 'y':2},
    'w':{'w': 0, 'z': 5},
    'y':{'y': 0, 'z': 2}
}

ip_Mapping = {
      'w': '192.168.199.208',
      'y': '192.168.199.5',
      'z': '192.168.199.6'
}

receiver = {
  'u': False,
  'v': False,
  'w': False,
  'x': False,
  'y': False
}

