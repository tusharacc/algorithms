from pickle import TRUE


class Node:

    def __init__(self,value,shortest_distance):
        self.value = value
        self.shortest_distance = shortest_distance
        self.predesessor = None

    def update_shortest_distance(self,dist,pred):
        self.shortest_distance = dist
        self.predesessor = pred

    def to_string(self):
        print (f"Node: {self.value}, Shortest Distance: {self.shortest_distance} from Node: {self.predesessor}")


class Edge:
    def __init__(self,start,end,weight):
        self.start = start
        self.end = end
        self.weight = weight

nodes = {
    "s": Node("s",float('inf')),
    "u": Node("u",float('inf')),
    "v": Node("v",float('inf')),
    "w": Node("w",float('inf')),
    "t": Node("t",float('inf')),
}


graph = {
    "s" : [Edge("s","v",4), Edge("s","u",2)],
    "v" : [Edge("v","t",4), ],
    "u" : [Edge("u","v",-1),Edge("u","w",2)],
    "w" : [Edge("w","t",2)],
    "t" : []
}

node_list = nodes.keys()
nodes["s"].update_shortest_distance(0,"s")

for node in node_list:
    stable = TRUE
    for edge in graph[node]:
        destination = edge.end
        print (nodes[node].shortest_distance, type(nodes[node].shortest_distance))
        print (edge.weight, type(edge.weight))
        if (nodes[node].shortest_distance + edge.weight) < nodes[destination].shortest_distance:
            nodes[destination].update_shortest_distance(edge.weight + nodes[node].shortest_distance,node)


for key in nodes:
    nodes[key].to_string()




