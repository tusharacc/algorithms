


graph = {
    "a": ("b","c","d"),
    "b": ("e","f"),
    "e": ("k",),
    "f": ("l",),
    "l": ("p","q",),
    "p": ("r",),
    "c": ("g",),
    "d": ("h","i","j",),
    "h": ("m",),
    "i": ("n","o"),
}

def return_neighbour(node):
    return graph.get(node, ())

def bfs_all():
    queue_explore = []
    visited = {}
    queue_explore.append("a")
    while len(queue_explore) > 0:
        current = queue_explore.pop(0)
        print ("Being processed",current)
        for neighbour in return_neighbour(current):
            if visited.get(neighbour,None) == None:
                visited[neighbour] = 1
                queue_explore.append(neighbour)

def find_shortest_path(start,end):
    queue_explore = []
    visited = {}
    queue_explore.append({"processed":start,"ancestory":[start]})
    exit = False

    while len(queue_explore) > 0:
        current = queue_explore.pop(0)
        print ("Being processed",current)
        for neighbour in return_neighbour(current["processed"]):  

            if visited.get(neighbour,None) == None:
                visited[neighbour] = 1
                queue_explore.append({"processed":neighbour,"ancestory":[*current["ancestory"],neighbour]})

                if neighbour == end:
                    print ([*current["ancestory"],neighbour])
                    exit = True
                    break

        if exit:
            break


if __name__ == '__main__':
    find_shortest_path("i","n")
    #bfs_all()