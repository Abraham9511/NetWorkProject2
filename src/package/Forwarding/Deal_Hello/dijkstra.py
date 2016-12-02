import threading

def Initiallizatoin_For_LS(u,G):
    global INF
    D = dict()
    pre = dict()
    curNode = set([u])
    for v in G.keys():
        if v in G['u'] and v != u:
            D[v] = G[u][v]
            pre[v] = u
        else:
            D[v] = INF
    return D, curNode, pre

def min_D_w(D,curNode):
    global INF
    min_Index = 'NO'
    min_Value = INF
    for node in D.keys():
        if D[node] < min_Value and node not in curNode:
            min_Index = node
            min_Value = D[node]
    return min_Index

def shortest_Path(u, end, pre):
    path = list()
    path.append(end)
    print(pre)
    while pre[end] != u:
        path.append(pre[end])
        end = pre[end]
    path.append(u)
    path.reverse()
    return path

# u is the first node for this LS
def Link_State_Agorithm(u, G):
    D, curNode, pre= Initiallizatoin_For_LS(u,G);
    while curNode != set(G.keys()) :
        w = min_D_w(D, curNode)
        curNode.add(w)
        for v in G[w].keys():
            if v not in curNode:
                if (D[v] > D[w]+G[w][v]):
                    D[v] = D[w]+G[w][v]
                    pre[v] = w
    return D, pre

G = { 'u': {'u':0, 'w':5, 'v':2, 'x':1} ,
      'v': {'v':0, 'w':3, 'x':2, 'u':2} ,
      'x': {'x':0, 'w':3, 'y':1, 'u':1, 'v':2},
      'w': {'w':0, 'z':5, 'y':1, 'u':5, 'v':3, 'x':3},
      'y': {'y':0, 'z':2, 'w':1, 'x':1},
      'z': {'z':0, 'w':5, 'y':2}
     }
INF = 99999999

def generate_Shortest_Path():
    global router_Table
    global myself
    G = router_Table
    D, pre= Link_State_Agorithm(myself,G);

    print("----------New-Cost----------")
    rlock = threading.RLock()
    rlock.acquire()
    global path_Table
    path_Table = list()
    for key in D.keys():
        if D[key] == INF:
            print(key+' INF')
        else:
            print(key+' '+str(D[key]))
            if key != myself:
                path = shortest_Path(myself, key, pre)
                path_Table.append(path)
                print('Shortest path from '+myself+ ' to '+key+' is')
                output_path = ''
                for item in path:
                    if item == myself:
                        output_path += item
                    else:
                        output_path += ' => '+item
                    print(output_path)
    rlock.realease()

if __name__=="__main__":
    print('Elect u as the center node')
    print('Run LS')
    D, pre= Link_State_Agorithm('u',G);
    for key in D.keys():
        if D[key] == INF:
            print(key+' INF')
        else:
            print(key+' '+str(D[key]))
    path = shortest_Path('u', 'z', pre)
    print('Shortest path from '+'u'+ ' to '+'z'+' is')
    output_path = ''
    for item in path:
        if item == 'u':
            output_path += item
        else:
            output_path += ' => '+item
    print(output_path)



