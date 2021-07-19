# class UnionFind(object):
#     def find_root(self, x, parent: []):
#         # 一层层往上找到根结点
#         x_root = x
#         while parent[x_root] != -1:
#             x_root = parent[x_root]
#         return x_root
#
#     def union_vertices(self, x, y, parent, rank):
#         # 合并两个集合
#         x_root = self.find_root(x, parent)
#         y_root = self.find_root(y, parent)
#
#         if x_root == y_root:
#             # 合并失败
#             return 0
#         else:
#             if rank[x_root] > rank[y_root]:
#                 parent[y_root] = x_root
#             elif rank[x_root] < rank[y_root]:
#                 parent[x_root] = y_root
#             else:
#                 parent[x_root] = y_root
#                 rank[y_root] +=1
#             return 1


class UF(object):
    def __init__(self, n):
        """长度为n的并查集"""

        self.count = n  # 判断并查集里共有几个集合, 初始化默认互相独立
        self.parent = [
            -1 for _ in range(n)
        ]  # 用 parent 数组记录每个节点的父节点，相当于指向父节点的指针，所以 parent 数组内实际存储着一个森林（若干棵多叉树）
        self.size = [
            0 for _ in range(n)
        ]  # 用 size 数组记录着每棵树的重量，目的是让 union 后树依然拥有平衡性，而不会退化成链表，影响操作效率

    def union_two_vertices(self, p, q):
        """

        :param p:
        :param q:
        :return:
        """
        root_p = self.find_root(p)
        root_q = self.find_root(q)
        if root_p == root_q:
            return  # 不用合并
        # 小树挂再大树下面，小树根节点的parent等于大树根结点
        if self.size[root_p] > self.size[root_q]:
            self.parent[root_q] = root_p
            self.size[root_p] += self.size[root_q]
        else:
            self.parent[root_p] = root_q
            self.size[root_q] += self.size[root_p]
        # 两个数合并后，子集必然减少1
        self.count -= 1

    def find_root(self, x):
        while parent[x] != -1:  # 因为初始化就是-1
            # 路径压缩, 也可以省略，最后把自己的父节点指向自己
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x  # 和入参x不是一个东西

    def is_connected(self, p, q):
        # 判断两个结点是不是同一个根节点
        root_p = self.find_root(p)
        root_q = self.find_root(q)
        return root_p == root_q

    def count(self):
        return self.count


if __name__ == "__main__":
    union_find = UnionFind()
    edges = [[0, 1], [1, 2], [1, 3], [3, 4], [2, 5]]
    vertice_nums = 5
    parent = [-1 for _ in range(vertice_nums)]
    rank = [0 for _ in range(vertice_nums)]

    for i in range(vertice_nums):
        print(i)
        x = edges[i][0]
        y = edges[i][1]
        if union_find.union_vertices(x, y, parent, rank) == 0:
            print("cycle detected!")
            exit(0)
    print("no cycle found")


# https://www.cnblogs.com/asdfknjhu/p/12515480.html
# https://www.cnblogs.com/yscl/p/10185293.html
# https://github.com/labuladong/fucking-algorithm/blob/master/%E7%AE%97%E6%B3%95%E6%80%9D%E7%BB%B4%E7%B3%BB%E5%88%97/UnionFind%E7%AE%97%E6%B3%95%E8%AF%A6%E8%A7%A3.md
