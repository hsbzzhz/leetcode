class UnionFind(object):

    # def __init__(self, edges: [], parent: [], rank: []):
    #     self.edges = edges
    #     self.parent = parent
    #     self.rank = rank


    def find_root(self, x, parent: []):
        # 找到根结点
        x_root = x
        while parent[x_root] != -1:
            x_root = parent[x_root]
        return x_root

    def union_vertices(self, x, y, parent, rank):
        # 合并两个集合
        x_root = self.find_root(x, parent)
        y_root = self.find_root(y, parent)

        if x_root == y_root:
            return 0
        else:
            if rank[x_root] > rank[y_root]:
                parent[y_root] = x_root
            elif rank[x_root] < rank[y_root]:
                parent[x_root] = y_root
            else:
                parent[x_root] = y_root
                rank[y_root] +=1
            return 1


if __name__ == '__main__':
    union_find = UnionFind()
    edges = [[0,1],[1,2],[1,3],[3,4],[2,5]]
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