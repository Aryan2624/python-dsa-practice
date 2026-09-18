def has_cycle(graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                if dfs(neighbour, node):
                    return True
            elif neighbour != parent:
                return True

        return False

    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True

    return False


graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

if has_cycle(graph):
    print("Cycle detected in the graph")
else:
    print("No cycle detected")




#Expected OUTPUT

#Cycle detected in the graph
