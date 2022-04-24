from graphs.graph import build_graph

def dfs(graph, stack, visited, in_stack, path):
    while stack:
        current = stack.pop()
        if not visited.get(current):
            visited[current] = True
            path.append(current)
            for pair in graph.adj_list.get(current, []):
                adj, _ = pair
                if not in_stack.get(adj):
                    stack.append(adj)
                    in_stack[adj] = True
    return path

def traverse(start_node):
    stack = [start_node]
    in_stack = {start_node: True}
    visited = {}
    path = []
    graph, _ = build_graph()
    return dfs(graph, stack, visited, in_stack, path)

start_node = 'A'
path = traverse(start_node)
print(f'dfs traversal')
print(path)
print()
