from collections import defaultdict


class Edge:
    def __init__(self, source, dest, weight):
        self.source = source
        self.dest = dest
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __le__(self, other):
        return self.weight <= other.weight

    def __repr__(self):
        return f'<Edge: [{self.source} - {self.dest}, w: {self.weight}]>'


class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_edge(self, source, dest, weight):
        self.adj_list[source].append((dest, weight))


def build_graph():
    graph = Graph()
    edges = (
        ('A', 'B', 4),
        ('B', 'A', 4),
        ('A', 'D', 6),
        ('D', 'A', 6),
        ('A', 'G', 16),
        ('G', 'A', 16),
        ('B', 'C', 24),
        ('C', 'B', 24),
        ('C', 'D', 23),
        ('D', 'C', 23),
        ('C', 'E', 18),
        ('E', 'C', 18),
        ('C', 'F', 9),
        ('F', 'C', 9),
        ('D', 'E', 5),
        ('E', 'D', 5),
        ('D', 'G', 8),
        ('G', 'D', 8),
        ('E', 'F', 11),
        ('F', 'E', 11),
        ('E', 'G', 10),
        ('G', 'E', 10),
        ('F', 'H', 7),
        ('H', 'F', 7),
        ('G', 'H', 21),
        ('H', 'G', 21),
    )
    edges_obj = []
    for source, dest, weight in edges:
        graph.add_edge(source, dest, weight)
        edges_obj.append(Edge(source, dest, weight))
    return graph, edges_obj
