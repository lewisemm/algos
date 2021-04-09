from linkedlist.nodelist import NodeList


class Graph:
    """
    Represent an undirected graph via adjacency list.
    """
    def __init__(self, no_vertices):
        self.no_vertices = no_vertices
        self.label_to_index = {}
        self.index_to_label = {}
        self.vertices = [None] * no_vertices
        # vertice index
        self.vi = 0
    
    def set_edge(self, label1, label2):
        index1 = self.label_to_index[label1]
        index2 = self.label_to_index[label2]
        print(f'index1: {index1}, index2: {index2}')

        if self.vertices[index1]:
            nl = self.vertices[index1]
            nl.insert(index2)
        else:
            nl = NodeList()
            nl.insert(index2)
            self.vertices[index1] = nl

        if self.vertices[index2]:
            nl = self.vertices[index2]
            nl.insert(index1)
        else:
            nl = NodeList()
            nl.insert(index1)
            self.vertices[index2] = nl

    def set_vertex(self, label):
        if 0 <= self.vi <= self.no_vertices:
            self.label_to_index[label] = self.vi
            self.index_to_label[self.vi] = label
            self.vi += 1

g = Graph(7)
g.set_vertex('A')
g.set_vertex('B')
g.set_vertex('C')
g.set_vertex('D')
g.set_vertex('E')
g.set_vertex('F')
g.set_vertex('G')
g.set_edge('A', 'B')
g.set_edge('A', 'E')
g.set_edge('A', 'F')
g.set_edge('B', 'C')
g.set_edge('C', 'D')
g.set_edge('F', 'G')
