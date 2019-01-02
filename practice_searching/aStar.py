import sys
sys.path.insert(0, '../practice_dataStructure/')
import graph
import numpy as np



def aStarAlgoMatrix(start=0, end=6):
    #graph = np.array([[0,8,3,5,100],[8,0,2,100,5],[100,1,0,3,4],[6,100,150,0,7],[100,5,100,100,0]])
    # graph = np.array([[0,2,100,3,100,100,100],[100,0,7,100,1,100,100],[100,100,0,100,100,2,100],[100,1,100,0,100,100,100],[100,100,7,100,0,100,4],[100,100,100,100,4,0,2],[1,100,100,1,100,100,0]])
    graph = np.array([[0,2,45,3,22,54,33],[77,0,7,98,66,11,89],[78,56,0,11,23,2,87],[32,1,111,0,9,65,68],[44,34,7,86,0,43,4],[22,35,21,12,4,0,44],[1,11,53,88,76,67,0]])
    #graph = np.array([[0,3,8,100,-4],[100,0,100,1,7],[100,4,0,100,100],[2,100,-5,0,100],[100,100,100,6,0]])

    
    print("Adjacency matrix")
    print(graph)
    v = len(graph)

    # path reconstruction matrix
    
    visited = [start]

    while not end in visited: 
        best = sys.maxsize
        bestInd = -1   
        for k in range(0,v):    
            #since it is full-connected graph, no need to create a set of unvisited "neighbours"
            if k in visited:
                continue

            # evaluate function: cost from start point + cost to end point   
            if graph[start, k]+graph[k, end]<best:
                bestInd = k
                best = graph[start, k]

        visited.append(bestInd)
        start = bestInd

    print(visited) 

aStarAlgoMatrix(0, 6)
