import random

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

    def randGenGraph(self, nVert, nEdge):
        weights = [int(random.random()*10) for i in range(nEdge)]
        verts = [chr(97+i) for i in range(nVert)]
        self.gdict = {}
        visit = set()
        
        for w in weights:
            fromV, toV = verts[int(random.random()*nVert)], verts[int(random.random()*nVert)]
            while fromV==toV or (fromV, toV) in visit:
                toV = fromV
                fromV = verts[int(random.random()*nVert)]
                # print(fromV)

            visit.add((fromV, toV))
            if not fromV in self.gdict:
                self.gdict[fromV] = {}

            self.gdict[fromV][toV] = w

        # print(self.gdict)

    def checkLoop(self):
        for v in self.gdict:
            
            Q = [[v]]
            while Q:
                path = Q.pop(0)
                for n in self.gdict[v]:
                    # print(v, n)
                    if n in path:
                        print(path)
                        return True
                        break
                    Q.append(path+[n])    






# Create the dictionary with graph elements
indirectGraph = { "a" : {"b":12,"c":3},     #direction, a->b a->c
                "b" : {"a":12, "d":4},
                "c" : {"a":3, "d":5, "g":9},
                "d" : {"e":6, "b":4, "c":5, "f":7},
                "g" : {"e":8, "c":9},
                "f" : {"d":7, "e":10},
                "e" : {"d":6, "g":8, "f":10}
                }

directGraph = { "a" : {"b":2,"c":3},     #direction, a->b a->c
                "b" : {"a":2, "d":4},
                "c" : {"d":5, "g":9},
                "d" : {"e":6, "f":7},
                "g" : {"e":8, "c":9},
                "f" : {"d":7, "e":10},
                "e" : {"d":6, "f":10}
                }


g = graph(directGraph)
if __name__ == "__main__":
    print(g.gdict)
    print("edges:", g.edges())
    print("vertices:", g.getVertices())
    # g.addVertex("f")
    # print(g.getVertices())
    # g.AddEdge('a','e', 7)
    # g.AddEdge('f','c', 8)
    # print("adding edges:", g.edges())
    g.randGenGraph(5, 5)
    print("random graph", g.gdict)
    print("show loop in graph:", g.checkLoop())

