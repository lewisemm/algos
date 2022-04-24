from disjoint_set.disjoint_set import DisjointSet
from graphs.graph import build_graph, Edge
from heap.min_heap import MinHeap


def build_heap():
    heap = MinHeap()
    return heap


def prims_algorithm(start_node):
    graph, _ = build_graph()
    if graph.adj_list.get(start_node):
        heap = build_heap()
        dj = DisjointSet()
        cost = 0
        path = []
        adjacents = []
        for dest, weight in graph.adj_list[start_node]:
            adjacents.append(Edge(start_node, dest, weight))
        heap.bulk_insert(adjacents)
        while heap.get_size() > 0:
            edge = heap.extract_min()
            intersection, parent1, parent2 = dj.intersection(edge.source, edge.dest)
            if not intersection:
                dj.add_edge(parent1, parent2)
                cost += edge.weight
                path.append(edge)
                adjacents = []
                if graph.adj_list.get(edge.dest):
                    for dest, weight in graph.adj_list[edge.dest]:
                        adjacents.append(Edge(edge.dest, dest, weight))
                    heap.bulk_insert(adjacents)
    return path, cost


path, cost = prims_algorithm('A')
print(f'cost: {cost}')
print(f'path: {path}')
