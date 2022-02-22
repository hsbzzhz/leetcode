"""
给定一个二叉树的根节点 root ，树中每个节点都存放有一个 0 到 9 之间的数字。

每条从根节点到叶节点的路径都代表一个数字：

例如，从根节点到叶节点的路径 1 -> 2 -> 3 表示数字 123 。
计算从根节点到叶节点生成的 所有数字之和 。

叶节点 是指没有子节点的节点。

输入：root = [4,9,0,5,1]
输出：1026
解释：
从根到叶子节点路径 4->9->5 代表数字 495
从根到叶子节点路径 4->9->1 代表数字 491
从根到叶子节点路径 4->0 代表数字 40
因此，数字总和 = 495 + 491 + 40 = 1026

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3Etpl5
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, prevTotal: int) -> int:
            if not root:
                return 0
            curTotal = prevTotal * 10 + root.val  # 先处理当前节点
            if not root.left and not root.right:
                return curTotal
            else:
                return dfs(root.left, curTotal) + dfs(root.right, curTotal)   # 再处理左右节点

        return dfs(root, 0)

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/3Etpl5/solution/jian-zhi-offer-2-mian-shi-ti-49-shu-zhon-c2tw/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。