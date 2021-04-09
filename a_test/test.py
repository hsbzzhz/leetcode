def dfs(graph: [], start):
    stack = list()
    # initial it
    stack.append(start)
    visited = set()
    visited.add(start)
    while stack:
        top_item = stack.pop()
        vertex = graph[top_item]
        for each in vertex:
            if each not in visited:
                stack.append(each)
                visited.add(each)
        print(top_item)


graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}

dfs(graph, 'A')
