import sys
sys.path.insert(0, '../practice_dataStructure/')

import graph

def dfs(graph, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start]:
        if not next in visited:
            dfs(graph, next, visited)
    return visited

print(graph.indirectGraph)

print("DFS traversal")
dfs(graph.indirectGraph, "a", None)


def bfs(graph, startnode):
# Track the visited and unvisited nodes using queue
    visited = set(startnode)
    queue = [startnode]

    while queue:
        curr = queue.pop(0)
        print(curr)
        if curr in graph:
            for v in graph[curr]:
                if not v in visited:
                    visited.add(v)
                    queue.append(v)


print("BFS traversal")
bfs(graph.indirectGraph, "a")

