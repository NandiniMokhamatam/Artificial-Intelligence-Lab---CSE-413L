from collections import deque

def has_cycle(graph):
    def bfs(node):
        visited[node] = True
        parent[node] = None

        queue = deque([node])

        while queue:
            current = queue.popleft()

            for neighbor in graph[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    parent[neighbor] = current
                    queue.append(neighbor)
                elif parent[current] != neighbor:
                    return True

        return False

    visited = {node: False for node in graph}
    parent = {node: None for node in graph}

    for node in graph:
        if not visited[node]:
            if bfs(node):
                return True

    return False

# Example directed graph with a cycle
graph_with_cycle = {
    5: [6],
    6: [33],
    33: [5, 44],
    44: []
}

# Example directed graph without a cycle
graph_without_cycle = {
    46: [26],
    26: [36],
    36: [46],
    56: []
}
if has_cycle(graph_with_cycle):
    print("The graph with a cycle contains a cycle.")
else:
    print("The graph with a cycle does not contain a cycle.")

if has_cycle(graph_without_cycle):
    print("The graph without a cycle contains a cycle.")
else:
    print("The graph without a cycle does not contain a cycle.")
