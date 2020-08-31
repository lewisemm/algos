graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['C'],
    'E': ['F'],
    'F': ['C']
}

def find_path(graph, start, end, path=[]):
    """
    This implementation can be found here.
    https://www.python.org/doc/essays/graphs/
    """
    path = path + [start]
    if (start == end):
        return path
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if not node in path:
            new_path = find_path(graph, node, end, path)
            if new_path:
                return new_path
    return None

print(find_path(graph, 'A', 'D'))
