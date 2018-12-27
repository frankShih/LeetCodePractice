class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def edges(self):
        return self.findedges()
    
    # Find the distinct list of edges
    def findedges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if (nxtvrtx, vrtx) not in edgename:
                    edgename.append((vrtx, nxtvrtx, self.gdict[vrtx][nxtvrtx]))
        return edgename
    
    # Add the new edge
    def AddEdge(self, fr, to, weight):
        if fr in self.gdict:
            self.gdict[fr][to]=weight

        else:
            self.gdict[fr] = {to:weight}


    # Get the keys of the dictionary
    def getVertices(self):
        return list(self.gdict.keys())

    # Add the vertex as a key
    def addVertex(self, vrtx):
       if vrtx not in self.gdict:
            self.gdict[vrtx] = {}




# Create the dictionary with graph elements
graph_elements = { "a" : {"b":2,"c":3},     #direction, a->b a->c
                "b" : {"a":2, "d":4},
                "c" : {"a":3, "d":5},
                "d" : {"e":6},
                "e" : {"d":6}
                }

g = graph(graph_elements)
print(g.edges())
print(g.getVertices())
g.addVertex("f")
print(g.getVertices())
g.AddEdge('a','e', 7)
g.AddEdge('f','c', 8)
print(g.edges())