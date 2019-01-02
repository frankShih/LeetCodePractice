import sys
sys.path.insert(0, '../practice_dataStructure/')
import graph
import numpy as np

def primAlgo(inputGraph, startNode):
    neighbors = set()
    visited = [startNode]
    for v in inputGraph[startNode]:
        neighbors.add((startNode, v))

    while len(visited)!= len(inputGraph): 
        bestVal = sys.maxsize
        best = None   
        # print("neighbors: \n", neighbors)
        for x, y in neighbors:
            if y in visited:
                continue    
            if inputGraph[x][y]<bestVal:
                bestVal = inputGraph[x][y]
                best = (x, y)
        # print("best", best)
        visited.append(best[1])
        neighbors.remove(best)
        for v in inputGraph[best[1]]:
            if v in visited:
                continue
            # print("add neighbor", (y, v))
            neighbors.add((best[1], v))

    print(visited)

# create minSpanningTree begin at certain point, in a weighted-undirected graph
#   
print(graph.indirectGraph)
print("prim traversal")
primAlgo(graph.indirectGraph, "a")