
# graph = {
#     "a": ("b","c","d"),
#     "b": ("e","f"),
#     "e": ("k",),
#     "f": ("l",),
#     "l": ("p","q",),
#     "p": ("r",),
#     "c": ("g",),
#     "d": ("h","i","j",),
#     "h": ("m",),
#     "i": ("n","o"),
#     "j": ("o")
# }

graph = {
    "a": ("b","c","d"),
    "b": ("c"),
    "d": ("c"),
    "c": ("e"),
    "e": ("f"),
    "g":()
}

visited = {}
def dfs():
    visited["a"] = 1
    do_dfs("a",["a"])
    print (visited)

def return_neighbour(node):
    return graph.get(node, ())

def do_dfs(node,ancestory):
    neighbour_found = False
    for neighbour in return_neighbour(node):
        neighbour_found = True
        #print (neighbour)
        if visited.get(neighbour,None) == None:
            visited[neighbour] = 1
            do_dfs(neighbour,[*ancestory,neighbour])
        else:
            visited[neighbour] += 1
    # if not neighbour_found:
    #     print (ancestory)

def get_all_path(start,end):
    visited[start] = 1
    all_path = []
    search_all_path(start,end,[start],all_path)
    print (all_path)

def search_all_path(start,end,ancestory,all_path):
    neighbour_found = False
    end_found = False
    for neighbour in return_neighbour(start):
        neighbour_found = True
        if neighbour == end:
            all_path.append(ancestory)
        #print (neighbour)
        if visited.get(neighbour,None) == None:
            visited[neighbour] = 1
            search_all_path(neighbour,end,[*ancestory,neighbour],all_path)


        
#dfs()
get_all_path("a","f")