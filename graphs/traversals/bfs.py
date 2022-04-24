from collections import deque

from graphs.graph import build_graph

def bfs(graph, visited, queue, in_queue, path):
    while queue:
        current = queue.popleft()
        if not visited.get(current):
            visited[current] = True
            path.append(current)
            for pair in graph.adj_list.get(current, []):
                adj, _ = pair
                if not in_queue.get(adj):
                    queue.append(adj)
    return path

def traverse(start_node):
    visited = {}
    in_queue = {}
    path = []
    queue = deque()
    queue.append(start_node)
    graph, _ = build_graph()
    return bfs(graph, visited, queue, in_queue, path)

start_node = 'A'
path = traverse(start_node)
print('bfs traversal.')
print(path)
print()
