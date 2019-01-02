import sys
sys.path.insert(0, '../practice_dataStructure/')
import graph
import numpy as np

def kruskalAlgo(inputGraph):
    visited = []
    edges = []
    while len(visited)!= len(inputGraph): 
        bestVal = sys.maxsize
        best = None   
        for x in inputGraph:
            for y in inputGraph[x]:
                if y in visited:
                    continue
                if inputGraph[x][y]<bestVal:
                    bestVal = inputGraph[x][y]
                    best = (x, y)
        print("add edge: ", best)
        edges.append(best)
        if not best[0] in visited:
            visited.append(best[0])
        if not best[1] in visited:
            visited.append(best[1])

    print(visited)
    print(edges)


# create minSpanningTree (process may have >1 sub-trees), in a weighted-undirected graph
print(graph.indirectGraph)
print("kruskal traversal")
kruskalAlgo(graph.indirectGraph)