import sys
sys.path.insert(0, '../practice_dataStructure/')
import graph
import numpy as np


def dijkstraAlgo(inputGraph, startNode):
    # treat None as inf. distance
    unvisited = {node: None for node in inputGraph}
    visited = {}
    current = startNode
    currentDistance = 0
    unvisited[current] = currentDistance  # set start distance to 0

    while True:
        del unvisited[current]
        # set the best result from previous round
        visited[current] = currentDistance
        if not unvisited:  # end of func
            break

        for neighbour, distance in inputGraph[current].items():
            if neighbour not in unvisited:
                continue

            # traverse all neighbors, update with shorter path
            newDistance = currentDistance + distance
            if unvisited[neighbour] == None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance

        # get all nodes accessable but unvisited
        candidates = [node for node in unvisited.items() if node[1]]
        # retrive node with least cost for next round
        current, currentDistance = sorted(candidates, key=lambda x: x[1])[0]

    print(visited)


# BFS, min path in directed graph problem
print(graph.directGraph)
print("dijkstra traversal")
dijkstraAlgo(graph.directGraph, "a")


def dijkstraAlgoMatrix(start=0):
    #graph = np.array([[0,8,3,5,100],[8,0,2,100,5],[100,1,0,3,4],[6,100,150,0,7],[100,5,100,100,0]])
    graph = np.array([[0,2,100,3,100,100,100],[100,0,7,100,1,100,100],[100,100,0,100,100,2,100],[100,1,100,0,100,100,100],[100,100,7,100,0,100,4],[100,100,100,100,4,0,2],[1,100,100,1,100,100,0]])
    #graph = np.array([[0,3,8,100,-4],[100,0,100,1,7],[100,4,0,100,100],[2,100,-5,0,100],[100,100,100,6,0]])



    print("Adjacency matrix")
    print(graph)
    v = len(graph)

    # path reconstruction matrix
    p = np.zeros(graph.shape)
    for i in range(0,v):
        for j in range(0,v):
            p[i,j] = graph[i,j]
            
    visited = [start]

    while len(visited)!= len(graph): 
        best = sys.maxsize
        bestInd = -1   
        for k in range(0,v):    
            #since it is full-connected graph, no need to create a set of unvisited "neighbours"
            if k in visited:
                continue
            if p[start, k]<best:
                bestInd = k
                best = p[start, k]

        visited.append(bestInd)
        start = bestInd

    print(visited) 

dijkstraAlgoMatrix(0)
