class Graph:
    """
    Represent an undirected graph via adjacency matrix.
    """
    def __init__(self, no_vertices):
        rnge = range(no_vertices)
        # vi ==> vertice index
        self.vi = 0
        # map of vertix index to vertix label
        self.vertice_label_to_int = {}
        # map of vertix label to vertix index
        self.vertice_int_to_label = {}
        self.no_vertices = no_vertices
        self.matrix = [[None] * no_vertices for n in rnge]

    def set_edge(self, source, dest):
        s = self.vertice_label_to_int[f'{source}']
        d = self.vertice_label_to_int[f'{dest}']
        self.matrix[s][d] = 1
        # this line should be removed if the graph is directed
        self.matrix[d][s] = 1
    
    def set_vertex(self, vertex, label):
        if 0 <= vertex <= self.no_vertices:
            self.vertice_label_to_int[label] = vertex
            self.vertice_int_to_label[vertex] = label
            self.vi += 1
    
    def bfs(self, start_vertice):
        stack = [start_vertice]
        visited = {start_vertice: True}
        nodes = [start_vertice]
        while stack:
            current = stack.pop(0)
            adj_list = self.matrix[self.vertice_label_to_int[current]]
            for col, data in enumerate(adj_list):
                label = self.vertice_int_to_label[col]
                if data == 1 and not visited.get(label, False):
                    stack.append(label)
                    nodes.append(label)
                    visited[label] = True
        return nodes
    
    def dfs(self, start_vertice):
        stack = [start_vertice]
        visited = {start_vertice: True}
        nodes = []
        while stack:
            current = stack.pop()
            nodes.append(current)
            adj_list = self.matrix[self.vertice_label_to_int[current]]
            # adjacency list index
            ali = len(adj_list) - 1
            while ali >= 0:
                label = self.vertice_int_to_label[ali]
                if adj_list[ali] == 1 and not visited.get(label, False):
                    stack.append(label)
                    visited[label] = True
                ali -= 1
        return nodes
