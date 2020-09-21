# representation using Adjacency Matrix
class Graph(object):
    def __init__(self, numvertex):
        self.adjMatrix = [[-1] * numvertex for x in range(numvertex)]
        self.numvertex = numvertex
        self.vertices = {}
        self.vertices_list = [0] * numvertex

    def set_vertex(self, vtx, id):
        if 0 <= vtx <= self.numvertex:
            self.vertices[id] = vtx
            self.vertices_list[vtx] = id

    def set_edge(self, fro, to, cost=0):
        fro = self.vertices[fro]
        to = self.vertices[to]
        self.adjMatrix[fro][to] = cost
        # don't add this for directed graphs
        self.adjMatrix[to][fro] = cost
    
    def get_vertex(self):
        return self.vertices_list
    
    def get_edges(self):
        edges = []
        for i in range(self.numvertex):
            for j in range(self.numvertex):
                if self.adjMatrix[i][j] != -1:
                    edges.append((
                        self.vertices_list[i],
                        self.vertices_list[j],
                        self.adjMatrix[i][j]
                    ))
        return edges
    
    def get_matrix(self):
        return self.adjMatrix

g = Graph(6)
# add nodes
g.set_vertex(0, 'a')
g.set_vertex(1, 'b')
g.set_vertex(2, 'c')
g.set_vertex(3, 'd')
g.set_vertex(4, 'e')
g.set_vertex(5, 'f')

# add edges
g.set_edge('a', 'e', 10)
g.set_edge('a', 'c', 20)
g.set_edge('c', 'b', 30)
g.set_edge('b', 'e', 40)
g.set_edge('e', 'd', 50)
g.set_edge('f', 'e', 60)

print('Vertices of graph g')
print(g.get_vertex())

print('Edges of graph g')
print(g.get_edges())

print('Adjacency Matrix of graph g')
print(g.get_matrix())
