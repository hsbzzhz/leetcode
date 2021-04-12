class Solution:
    """
    """

    def bfs(self, graph: [], start):
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

    def dfs(self, graph: [], start):
        stack = list()
        # 入栈
        stack.append(start)  # 从头节点开始遍历
        visited = set()
        visited.add(start)
        while stack:
            vertex = stack.pop(-1)  # 弹出栈顶元素
            nodes = graph[vertex]  # 出队节点队的相邻节

            for w in nodes:
                if w not in visited:  # 确保不重复
                    stack.append(w)
                    visited.add(w)
            print(vertex)  # 打印出stack元素

    def dfs_recursion(self, graph: [], start):
        """
        不需要用到栈
        :param graph:
        :param start:
        :return:
        """

        def dfs(node):
            visited.add(node)
            print(node)
            children = graph[node]
            for each in children:
                if not each in visited:
                    dfs(each)

        visited = set()
        dfs(start)

    """
    判断一个图中是否存在环
    """

    def find_circle(self, graph: []) -> bool:
        # 应该是如果该结点为-1即有环，但也要考虑父节点
        # color = 0 该节点暂未访问
        # color = -1 该节点访问了一次
        # color = 1 该节点的所有孩子节点都已访问,就不会再对它做DFS了
        def dfs(node, color):
            is_circle = False
            color[node] = -1
            for each in graph[node]:
                if color[each] == 1:
                    return True
                elif color[each] == 0:
                    is_circle = dfs(each, color)
            color[node] = 1
            return is_circle

        color = {i: 0 for i in graph.keys()}
        for each in graph:
            if color[each] == 0:
                has_circle = dfs(each, color)
                if has_circle:
                    return True
        return False


demo = Solution()
graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}

graph1 = {
    "A": ["B", "E"],
    "B": ["A", "C", "E"],
    "C": ["B", "D"],
    "D": ["C", "F"],
    "E": ["A", "B"],
    "F": ["D"]
}

# demo.dfs(graph, 'A')
# demo.dfs_recursion(graph1, "A")
res = demo.find_circle(graph1)
print(res)
