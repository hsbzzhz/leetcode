def bfs(graph: [], start):
    queue = list()
    # 入队
    queue.append(start)  # 从头节点开始遍历
    visited = set()
    visited.add(start)
    while queue:
        vertex = queue.pop(0)  # FIFO
        nodes = graph[vertex]  # 出队节点队的相邻节点
        for w in nodes:
            if w not in visited:  # 确保不重复
                queue.append(w)
                visited.add(w)
        print(vertex)  # 打印出队元素


def dfs(graph: [], start):
    stack = list()
    # 入栈
    stack.append(start)  # 从头节点开始遍历
    visited = set()
    visited.add(start)
    while stack:
        vertex = stack.pop(-1)  # 弹出栈顶元素
        nodes = graph[vertex]   # 出队节点队的相邻节点
        for w in nodes:
            if w not in visited:  # 确保不重复
                stack.append(w)
                visited.add(w)
        print(vertex)   # 打印出stack元素


# graph = {
# "A": ["B", "C"],
# “B”: [“A”, “C”, “D”],
# “C”: [“A”, “B”, “D”, “E”],
# “D”: [“B”, “C”, “E”, “F”],
# “E”: [“C”, “D”],
# “F”: [“D”]
# }