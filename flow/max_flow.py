from copy import deepcopy
from graph import Node, Edge, Graph

G = Graph()
start_node = Node("Vancouver","s")
G.add_vertices_edges(start_node,[Edge("s","v1",16),Edge("s","v2",13)])
G.add_vertices_edges(Node("Edmonton","v1"),[Edge("v1","v3",12)])
G.add_vertices_edges(Node("Calgary","v2"),[Edge("v2","v1",4),Edge("v2","v4",14)])
G.add_vertices_edges(Node("Saskatoon","v3"),[Edge("v3","v2",9),Edge("v3","t",20)])
G.add_vertices_edges(Node("Regina","v4"),[Edge("v4","v3",7),Edge("v4","t",4)])
G.add_vertices_edges(Node("Winnipeg","t"),[])

#G.draw_graph()

def dfs(graph,node,visited,path_found):
    for edge in graph.get_children(node):
        if not visited.get(edge.destination, False):
            visited[edge.destination] = True
            graph.update_node(node,'next',edge.destination)
            graph.update_node(node,'capacity',edge.weight)
            if edge.destination == 't':
                path_found = True
            path_found = dfs(graph=graph,node=graph.get_node(edge.destination),visited=visited,path_found=path_found)

    return path_found

def get_path(graph,node):
    start = node.symbol
    path = [start]
    #graph.draw_graph()
    while True:
        #print (start)
        next_vertex = graph.get_node(start).next
        path.append(next_vertex)
        if next_vertex == "t":
            print (next_vertex)
            break
        #path.append(next_vertex)
        start = next_vertex
    return path

def get_minimum_capacity(graph,path):
    minimum = float('inf')
    for vertex in path[:-1]:
        #graph.get_node(vertex).to_string()
        if graph.get_node(vertex).input_capacity < minimum:
            minimum = graph.get_node(vertex).input_capacity

    return minimum

def create_residual_flow(G_prime, path, alpha):
    for i in range(len(path)-1):
        current_path = (path[i], path[i+1])
        for k,v in enumerate(G_prime.get_children(G_prime.get_node(path[i]))):
            if v.start == current_path[0] and v.destination == current_path[1]:
                if v.weight < alpha:
                    import sys
                    print ("Invalid", v,path,alpha)
                    sys.exit(1)
                elif v.weight == alpha:
                    G_prime.remove_edge(G_prime.get_node(current_path[0]),current_path[1])
                    G_prime.add_edge(G_prime.get_node(current_path[1]),Edge(current_path[1],current_path[0],alpha))
                    break
                else:
                    G_prime.remove_edge(G_prime.get_node(current_path[0]),current_path[1])
                    G_prime.add_edge(G_prime.get_node(current_path[1]),Edge(current_path[1],current_path[0],alpha))
                    G_prime.add_edge(G_prime.get_node(current_path[0]),Edge(current_path[0],current_path[1],v.weight - alpha))
                    break

    
                    

#Get a flow path
# visited ={}
# dfs(G,start_node,visited)
# path = get_path(G,start_node)
# print (path)
# #Ford-Fulkerson
# #get minimum capacity
# alpha = get_minimum_capacity(G,path)
# print (alpha)


# G_prime = deepcopy(G)
# create_residual_flow(G_prime,path,alpha)
# print ("printing G prime")
# G_prime.to_string()

G_prime = deepcopy(G)
alpha = 0
graph_list = [G_prime]
counter = 0
while True:
    visited = {start_node.symbol: True}
    path_found = False
    path_found = dfs(graph_list[counter],start_node,visited,path_found)
    if path_found:
        path = get_path(graph_list[counter],start_node)
        if len(path) == 1:
            break
        print ("Path is",path)
        alpha = get_minimum_capacity(graph_list[counter],path)
        print ("Capacity is ", alpha)
        graph_list.append(deepcopy(graph_list[counter]))
        counter += 1
        graph_list[counter].update_nodes()
        create_residual_flow(graph_list[counter],path,alpha)
    else:
        break

import random
graph = graph_list[counter]

number_of_edges = 3

while number_of_edges > 0:
    
    choices = random.choices(list(graph.nodes.values()),k=2)

    if choices[0].symbol == "t" or choices[0].symbol == choices[1].symbol:
        pass
    else:
        number_of_edges -= 1
        source_node, destination_node = choices
        print ("Edges added",source_node.symbol,destination_node.symbol)
        G.add_edge(source_node,Edge(source_node.symbol,destination_node.symbol,1))

graph.draw_graph()

while True:
    visited = {start_node.symbol: True}
    path_found = False
    path_found = dfs(graph_list[counter],start_node,visited,path_found)
    if path_found:
        path = get_path(graph_list[counter],start_node)
        if len(path) == 1:
            break
        print ("Path is",path)
        alpha = get_minimum_capacity(graph_list[counter],path)
        print ("Capacity is ", alpha)
        graph_list.append(deepcopy(graph_list[counter]))
        counter += 1
        graph_list[counter].update_nodes()
        create_residual_flow(graph_list[counter],path,alpha)
    else:
        break