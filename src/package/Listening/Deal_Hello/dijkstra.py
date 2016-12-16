import package.settings.setting

# 初始化
def initiallizatoin_for_ls(u,G):
    D = dict()
    pre = dict()
    curNode = set([u])
    for v in G.keys():
        if v in G[u] and v != u:
            D[v] = G[u][v]
            pre[v] = u
        else:
            D[v] = package.settings.setting.INF
    return D, curNode, pre

# 计算最短的路径
def min_D_w(D,curNode):
    min_Index = 'NO'
    min_Value = package.settings.setting.INF
    for node in D.keys():
        if D[node] < min_Value and node not in curNode:
            min_Index = node
            min_Value = D[node]
    return min_Index


def shortest_Path(u, end, pre):
    path = list()
    path.append(end)
    while pre[end] != u:
        path.append(pre[end])
        end = pre[end]
    path.append(u)
    path.reverse()
    return path

def Link_State_Agorithm(u, G):
    D, curNode, pre= initiallizatoin_for_ls(u,G)
    while curNode != set(G.keys()) :
        w = min_D_w(D, curNode)
        curNode.add(w)
        for v in G[w].keys():
            if v not in curNode:
                if (D[v] > D[w]+G[w][v]):
                    D[v] = D[w]+G[w][v]
                    pre[v] = w
    return D, pre

# 调用该函数能应用dijstra生成最短路径并且更新到path_Table
def generate_Shortest_Path():
    # 更新之前清空path_Table的过往数据
    package.settings.setting.path_Table = list()
    # 为了方便使用，且该函数中不会修改router_Table放心赋值
    G = package.settings.setting.router_Table
    # 调用该函数可以生成最短路径，D存储该点到所有其他点的最短路径的cost，pre记录每个节点的父节点
    D, pre= Link_State_Agorithm(package.settings.setting.HOST,G)

    # 以下在控制台输出从该点到其他点的最低cost的路径
    print("----------New-Cost----------")
    for key in D.keys():
        if D[key] == package.settings.setting.INF:
            continue
        else:
            if key != package.settings.setting.HOST :
                # 调用该函数能从已经生成的path_Table中找到从HOST到key的最短路径返回
                path = shortest_Path(package.settings.setting.HOST , key, pre)
                package.settings.setting.path_Table.append(path)
                print("Shortest path from "+package.settings.setting.HOST + " to "+key+" is: ", end="")
                output_path = ''
                for item in path:
                    if item == package.settings.setting.HOST :
                        output_path += item
                    else:
                        output_path += ' => '+item
                print(output_path)



