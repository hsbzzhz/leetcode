class UnionFind(object):
    """并查集"""
    def __init__(self, n):
        self.uf = [-1 for i in range(n + 1)]  # 列表0位置空出
        self.sets_count = n  # 判断并查集里共有几个集合, 初始化默认互相独立

    def find_root(self, p):
        """查找p的根结点(祖先)"""
        r = p                                   # 初始p
        while self.uf[p] > 0:
            p = self.uf[p]
        while r != p:                           # 路径压缩, 把搜索下来的结点祖先全指向根结点
            self.uf[r], r = p, self.uf[r]
        return p

    def union(self, p, q):
        """连通p,q 让q指向p"""
        proot = self.find_root(p)
        qroot = self.find_root(q)
        if proot == qroot:
            return
        elif self.uf[proot] > self.uf[qroot]:  # 负数比较, 左边规模更小
            self.uf[qroot] += self.uf[proot]
            self.uf[proot] = qroot
        else:
            self.uf[proot] += self.uf[qroot]  # 规模相加
            self.uf[qroot] = proot
        self.sets_count -= 1  # 连通后集合总数减一

    def is_connected(self, p, q):
        """判断pq是否已经连通"""
        return self.find_root(p) == self.find_root(q)   # 即判断两个结点是否是属于同一个祖先
# https://www.cnblogs.com/asdfknjhu/p/12515480.html