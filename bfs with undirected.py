from collections import defaultdict, deque

def has_cycle(graph):
    visited = set()
    
    for node in graph:
        if node not in visited:
            queue = deque([(node, None)])  # Tuple format: (current_node, parent_node)
            visited.add(node)
            
            while queue:
                current, parent = queue.popleft()
                
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, current))
                    elif neighbor != parent:
                        return True  # Cycle detected
                    
    return False

# Example undirected graph with a cycle
graph_with_cycle = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 5],
    4: [2, 6],
    5: [3],
    6: [4]
}

# Example undirected graph without a cycle
graph_without_cycle = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 5],
    4: [2],
    5: [3]
}

# Test the function with graphs
if has_cycle(graph_with_cycle):
    print("The graph with a cycle contains a cycle.")
else:
    print("The graph with a cycle does not contain a cycle.")

if has_cycle(graph_without_cycle):
    print("The graph without a cycle contains a cycle.")
else:
    print("The graph without a cycle does not contain a cycle.")
