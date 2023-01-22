from draw import Draw

class Node:
    def __init__(self,name, symbol):
        self.name = name
        self.next = None
        self.input_capacity = None
        self.symbol = symbol

    def to_string(self):
        print (f"Name: {self.name}, Next: {self.next}, Capacity: {self.input_capacity}. Symbol is - {self.symbol}")

class Edge:
    def __init__(self,start,destination, weight):
        self.start = start
        self.destination = destination
        self.weight = weight

    def to_string(self):
        print (f"Start: {self.start}, End: {self.destination}, Weight: {self.weight}")



class Graph:
    def __init__(self):
        self.G = {}
        self.nodes = {}

    def add_vertices_edges(self,node, edges):
        #print (node, type(node))
        self.G[node.symbol] = edges
        self.__add_to_nodes(node)
    
    def __add_to_nodes(self,node):
        if not self.nodes.get(node.symbol, False):
            self.nodes[node.symbol] = node

    def add_edge(self,node,edge):
        for k,v in enumerate(self.G[node.symbol]):
            if v.destination == edge.destination and v.start == edge.start:
                self.G[node.symbol].pop(k)
        self.G[node.symbol].append(edge)
        self.__add_to_nodes(node)

    def add_additional_edge(self,node,edge):
        previous_edge_weight = 0
        for k,v in enumerate(self.G[node.symbol]):
            if v.destination == edge.destination and v.start == edge.start:
                previous_edge_weight = v.weight
                self.G[node.symbol].pop(k)
        edge.weight += previous_edge_weight
        self.G[node.symbol].append(edge)
        self.__add_to_nodes(node)


    def remove_edge(self,node,destination):
        for i,v in enumerate(self.G[node.symbol]):
            if v.destination == destination:
                self.G[node.symbol].pop(i)

    def update_node(self,node,field,value):
        #print (f"Node: {node.to_string()}, Field: {field}, Value: {value}")
        #self.nodes[node.symbol].to_string()
        if field == 'next':
            self.nodes[node.symbol].next = value
        elif field == 'capacity':
            self.nodes[node.symbol].input_capacity = value
        #self.nodes[node.symbol].to_string()
    
    def get_node(self,symbol):
        return self.nodes[symbol]

    def get_children(self,node):
        return self.G.get(node.symbol)

    def get_edges(self,node):
        return self.G[node.symbol]

    def to_string(self):
        for node in self.nodes.values():
            node.to_string()
        for k,v in self.G.items():
            print ("For Key,", k)
            for i in v:
                i.to_string()

    def update_nodes(self):
        for node in self.nodes:
            self.nodes[node].input_capacity = None
            self.nodes[node].next = None

    def draw_graph(self):
        d = Draw(self)
        if d.user_input == None:
            del d
        elif d.user_input.lower() == 'yes' or d.user_input.lower() == 'y':
            d.draw()
        else:
            del d