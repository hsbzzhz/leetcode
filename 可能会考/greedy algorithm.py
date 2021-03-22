"""
单元最短路径
最小生成树
哈夫曼编码
"""
from typing import List


class Solution:
    """
    对每个孩子 i，都有一个胃口值 g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j，都有一个尺寸 s[j] 。如果 s[j] >= g[i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。

 
    示例 1:

    输入: g = [1,2,3], s = [1,1]
    输出: 1
    解释:
    你有三个孩子和两块小饼干，3个孩子的胃口值分别是：1,2,3。
    虽然你有两块小饼干，由于他们的尺寸都是1，你只能让胃口值是1的孩子满足。
    所以你应该输出1。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/assign-cookies
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = j = count = 0
        while j < len(s) and i < len(g):
            if g[i] <= s[j]:
                i+=1
                count +=1
            j+=1
        return count


"""
给出n个物品，第i个物品重量为Wi
尽可能多的装物品，使得总重量不超过G

解法，把物品按照从小到大排序，依次装入，直到装不下为止
"""
