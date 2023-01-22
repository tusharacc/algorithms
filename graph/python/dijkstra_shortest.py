from dataclasses import dataclass
from tracemalloc import start
from turtle import end_fill

@dataclass
class Node:
    value
    shortest_distance = 0
    predesessor = None

@dataclass
class Edge:
    start
    end
    weight


graph = {
    Node("s") : [Edge("s","v",1), Edge("s","w",4)],
    Node("v") : [Edge("v","w",2), Edge("v","t",6)],
    Node("w") : [Edge("w","t",3)],
    Node("t") : []
}

