from graphs.linkedlist.nodelist import NodeList


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

    def bfs(self, start_vertex):
        queue = [self.label_to_index[start_vertex]]
        visited = {
            queue[0]: True
        }
        nodes = ''
        while queue:
            current = queue.pop(0)
            adj_list = self.vertices[current]
            try:
                gen = adj_list.adjacent()
                while gen:
                    index = next(gen).index
                    if not visited.get(index, False):
                        queue.append(index)
                        visited[index] = True
            except StopIteration:
                pass
            nodes += f'{self.index_to_label[current]}, '
        return nodes

    def dfs(self, start_vertex):
        stack = [self.label_to_index[start_vertex]]
        visited = {
            stack[0]: True
        }
        nodes = ''
        while stack:
            current = stack.pop()
            adj_list = self.vertices[current]
            try:
                gen = adj_list.adjacent()
                while gen:
                    index = next(gen).index
                    if not visited.get(index, False):
                        stack.append(index)
                        visited[index] = True
            except StopIteration:
                pass
            nodes += f'{self.index_to_label[current]}, '
        return nodes
