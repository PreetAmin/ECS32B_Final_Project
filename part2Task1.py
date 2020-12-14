"""
BFS #Milap
"""
def bfs(map, office):



"""
DFS #Dave
"""
def dfs(map, office):
    path = {}
    stack = [(office, [office])]
    visited = set()
    while stack:
        (v, p) = stack.pop()
        if v not in visited:
            path[v] = p
        visited.add(v)
        temp = []
        temp2 = []
        for e in map:
            if e[0] == v:
                temp2.append((e[1], p + [e[1]]))
                temp.append(e)
            if e[1] == v:
                temp2.append((e[0], p + [e[0]]))
                temp.append(e)
        map = [e for e in map if e not in temp]
        temp2 = sorted(temp2)
        for i in temp2:
            stack.append(i)
    return path
"""
Dijkstra's #Preet 
"""
def dijkstra(map, office):
