import sys

from collections import OrderedDict

from graph import build_graph, Edge
from heap.min_heap import MinHeap


def add_to_heap(graph, node, heap, visited, distances):
    visited[node] = True
    for pair in graph.adj_list[node]:
        adj, weight = pair
        if not visited.get(adj):
            heap.single_insert(Edge(node, adj, weight))
        if distances.get(adj, float('inf')) > distances[node] + weight:
            distances[adj] = distances[node] + weight
    return heap, visited, distances
    

def dijkstras(graph, heap, visited, distances):
    while heap.get_size():
        edge = heap.extract_min()
        current = edge.dest
        heap, visited, distances = add_to_heap(graph,
                                        current, heap, visited, distances)
    return distances
    

def traverse(start_node):
    graph, _ = build_graph()
    heap = MinHeap()
    visited, distances = {}, OrderedDict()
    visited[start_node] = 0
    distances[start_node] = 0
    # initialize heap with start_node's adjacent edges
    heap, visited, distances = add_to_heap(graph,
                                    start_node, heap, visited, distances)
    return dijkstras(graph, heap, visited, distances)

start_node = 'A'
distances = traverse(start_node)
print(f'distances from {start_node}')
for key in distances:
    print(f'{key}: {distances[key]} km.')
