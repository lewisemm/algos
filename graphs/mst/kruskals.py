from disjoint_set.disjoint_set import DisjointSet
from graphs.graph import build_graph
from heap.min_heap import MinHeap


def build_heap(edges):
    heap = MinHeap()
    heap.bulk_insert(edges)
    return heap


def kruskals_algorithm():
    graph, edges = build_graph()
    heap = build_heap(edges)

    dj = DisjointSet()
    cost = 0
    path = []

    while heap.get_size() > 0:
        edge = heap.extract_min()
        intersection, parent1, parent2 = dj.intersection(edge.source, edge.dest)
        if not intersection:
            dj.add_edge(parent1, parent2)
            cost += edge.weight
            path.append(edge)
    return path, cost


path, cost = kruskals_algorithm()
print(f'cost: {cost}')
print(f'path: {path}')
