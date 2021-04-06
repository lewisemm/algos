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

# representation using Adjacency Lists
class AdjNode(object):
    """
    A class to represent the adjacency list of the node.
    """
    def __init__(self, data):
        self.vertex = data
        self.next = None

    def __repr__(self):
        return '<AdjNode: {}>'.format(self.vertex)


class GraphAdjList(object):
    """
    A graph representation using adjacency lists.
    """
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    def add_edge(self, src, dest):
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i))
            temp = self.graph[i]
            while temp:
                print('-> {}'.format(temp.vertex))
                temp = temp.next
            print('\n')

    def print_g(self):
        print(self.graph)

grrr = GraphAdjList(5)
grrr.add_edge(0, 1)
grrr.add_edge(0, 4)
grrr.add_edge(1, 2)
grrr.add_edge(1, 3)
grrr.add_edge(1, 4)
grrr.add_edge(2, 3)
grrr.add_edge(3, 4)

grrr.print_g()
