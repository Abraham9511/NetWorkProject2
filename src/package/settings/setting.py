# ## u setting ##
# HOST = 'u'
# Port = 2711
# INF = 9999
#
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
# path_Table = list()
#
# ## v ##
# HOST = 'v'
# Port = 2711
# INF = 9999
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
# path_Table = list()
#
# ## w ##
# HOST = 'w'
# Port = 2711
# INF = 9999
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
# path_Table = list()
#
# ## x ##
# HOST = 'x'
# Port = 2711
# INF = 9999
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
# path_Table = list()
#
# ## y ##
# HOST = 'y'
# Port = 2711
# INF = 9999
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
# path_Table = list()
#
## z ##
HOST = 'z'
Port = 2711
INF = 9999

router_Table = {
    'z':{'w': 5, 'z': 0, 'y':2},
    'w':{'w': 0, 'z': 5},
    'y':{'y': 0, 'z':2}
}

ip_Mapping = {
      'w': '192.168.199.208',
      'y': '192.168.199.5',
      'z': '192.168.199.6'
}

path_Table = list()