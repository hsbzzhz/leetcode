from typing import List


"""
https://leetcode-cn.com/problems/satisfiability-of-equality-equations/
给你一个数组 equations，装着若干字符串表示的算式。每个算式 equations[i] 长度都是 4，而且只有这两种情况：a==b 或者 a!=b，其中 a,b 可以是任意小写字母。你写一个算法，如果 equations 中所有算式都不会互相冲突，返回 true，否则返回 false。

比如说，输入 ["a==b","b!=c","c==a"]，算法返回 false，因为这三个算式不可能同时正确。
再比如，输入 ["c==c","b==d","x!=z"]，算法返回 true，因为这三个算式并不会造成逻辑冲突。
"""


class UnionFind(object):
    def __init__(self):
        self.parent = list(range(26))

    def find(self, index):
        if index == self.parent[index]:
            return index
        self.parent[index] = self.find(self.parent[index])
        return self.parent[index]

    def union(self, index1, index2):
        self.parent[self.find(index1)] = self.find(index2)


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind()
        for st in equations:
            # 这个循环把所有相等的等连起来，构建图
            if st[1] == "=":
                index1 = ord(st[0]) - ord("a")  # ord用于获取 ASCII 的值
                index2 = ord(st[3]) - ord("a")  # 为什么要减 ord('a')，因为数组范围是26，acii 减去一个a才不会数组越界
                uf.union(index1, index2)
        for st in equations:
            # 判断不等式中，有没有相等
            if st[1] == "!":
                index1 = ord(st[0]) - ord("a")
                index2 = ord(st[3]) - ord("a")
                if uf.find(index1) == uf.find(index2):
                    return False
        return True

"""
https://leetcode-cn.com/problems/satisfiability-of-equality-equations/solution/deng-shi-fang-cheng-de-ke-man-zu-xing-by-leetcode-/

"""