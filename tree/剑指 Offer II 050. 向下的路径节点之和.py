"""
给定一个二叉树的根节点 root，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。


示例 1：


输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
输出：3
解释：和等于 8 的路径有 3 条，如图所示。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/6eUYwP
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    """
    brute force

    递归每个节点，并递归每个节点的左右节点，进行check
    """
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def dfs(root: TreeNode, target):
            if not root:
                return 0
            res = 0
            if target - root.val == 0:  # 向下递归，如果等于targetSum，就加一
                res += 1
            res += dfs(root.left, target - root.val)  # 减去该节点的值，向左子树跑去
            res += dfs(root.right, target - root.val)  # 减去该节点的值，向右子树跑去

            return res

        if not root:
            return 0
        res = dfs(root, targetSum)   # 查看根节点是否满足条件
        res += self.pathSum(root.left, targetSum) # 递归查找左右节点是否满足条件
        res += self.pathSum(root.right, targetSum)
        return res