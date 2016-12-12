# import package.settings.U
# import package.settings.V
# import package.settings.W
# import package.settings.X
# import package.settings.Y
import package.settings.Z

def Initiallizatoin_For_LS(u,G):
    D = dict()
    pre = dict()
    curNode = set([u])
    for v in G.keys():
        if v in G[u] and v != u:
            D[v] = G[u][v]
            pre[v] = u
        else:
            D[v] = package.settings.Z.INF
    return D, curNode, pre

def min_D_w(D,curNode):
    min_Index = 'NO'
    min_Value = package.settings.Z.INF
    for node in D.keys():
        if D[node] < min_Value and node not in curNode:
            min_Index = node
            min_Value = D[node]
    return min_Index

def shortest_Path(u, end, pre):
    path = list()
    path.append(end)
    # print(pre)
    while pre[end] != u:
        path.append(pre[end])
        end = pre[end]
    path.append(u)
    path.reverse()
    return path

# u is the first node for this LS
def Link_State_Agorithm(u, G):
    D, curNode, pre= Initiallizatoin_For_LS(u,G)
    while curNode != set(G.keys()) :
        w = min_D_w(D, curNode)
        curNode.add(w)
        for v in G[w].keys():
            if v not in curNode:
                if (D[v] > D[w]+G[w][v]):
                    D[v] = D[w]+G[w][v]
                    pre[v] = w
    return D, pre

# G = { 'u': {'u':0, 'w':5, 'v':2, 'x':1} ,
#       'v': {'v':0, 'w':3, 'x':2, 'u':2} ,
#       'x': {'x':0, 'w':3, 'y':1, 'u':1, 'v':2},
#       'w': {'w':0, 'z':5, 'y':1, 'u':5, 'v':3, 'x':3},
#       'y': {'y':0, 'z':2, 'w':1, 'x':1},
#       'z': {'z':0, 'w':5, 'y':2}
#      }
# package.settings.Z.INF = 99999999

def generate_Shortest_Path():
    package.settings.Z.path_Table = list()
    G = package.settings.Z.router_Table
    D, pre= Link_State_Agorithm(package.settings.Z.HOST ,G)

    print("----------New-Cost----------")
    # rlock = threading.RLock()
    # rlock.acquire()
    for key in D.keys():
        if D[key] == package.settings.Z.INF:
            continue
        else:
            if key != package.settings.Z.HOST :
                path = shortest_Path(package.settings.Z.HOST , key, pre)
                package.settings.Z.path_Table.append(path)
                print("Shortest path from "+package.settings.Z.HOST + " to "+key+" is: ", end="")
                output_path = ''
                for item in path:
                    if item == package.settings.Z.HOST :
                        output_path += item
                    else:
                        output_path += ' => '+item
                print(output_path)

# if __name__=="__main__":
#     print('Elect u as the center node')
#     print('Run LS')
#     D, pre= Link_State_Agorithm('u',G)
#     for key in D.keys():
#         if D[key] == package.settings.Z.INF:
#             print(key+' package.settings.Z.INF')
#         else:
#             print(key+' '+str(D[key]))
#     path = shortest_Path('u', 'z', pre)
#     print('Shortest path from '+'u'+ ' to '+'z'+' is')
#     output_path = ''
#     for item in path:
#         if item == 'u':
#             output_path += item
#         else:
#             output_path += ' => '+item
#     print(output_path)



