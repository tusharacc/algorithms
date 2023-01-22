graph = {
    1: [(1,2), (1,3)],
    2: [(2,4), (2,5), (2,3)],
    3: [(3,5), (3,2), (3,8), (3,1), (3,7)],
    4: [(4,2), (4,5)],
    5: [(5,6), (5,4), (5,3), (5,2)],
    6: [],
    7: [(7,3), (7,8)],
    8: [(8,3), (8,7)],
    9: [(9,10)],
    10: [(10,9)],
    11: [(11,12)],
    12: [(12,13), (12,11)],
    13: []
}

def BFS(s,discovered):
    discovered[vertex] = True
    L = [[s]]
    T = {}
    i = 0
    while len(L[i]) != 0:
        temp = []
        for node in L[i]:
            for edge in graph[node]:
                if not discovered.get(edge[1], False):
                    discovered[edge[1]] = True
                    if T.get(node,False) == False:
                        T[node] = [edge]
                    else:
                        T[node].append(edge)
                    temp.append(node)
        i += 1
        L.append(temp)
    print (T)

discovered = {}
vertices = graph.keys()
for vertex in vertices:
    BFS(vertex,discovered)