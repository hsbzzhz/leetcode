from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindDepth():
    """
    104. 二叉树最大深度
    """
    def maxDepth(self, root: TreeNode) -> int:
        """
        DFS  O(n)
        当前结点为空即终止
        加上根节点自己即为最大深度
        :param root:
        :return:
        """
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


class CompareTree(object):
    """
    100. 相同的树
    O(n) n为树的结点树
    """

    def isSameTree(self, p, q):
        """
        1. 两个结点都为空
        2. 两个结点其中一个为空
        3. 两个结点不相等
        然后同时对比树1的左vs树2的左 + 树1的右vs树2的右
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


class FindDif:
    """
    101. 对称二叉树
    O(n)
    """

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        return self.dfs(root.left, root.right)

    def dfs(self, left: TreeNode, right: TreeNode):
        """
        1. 两个结点都为空，
        2. 两个结点中有一个为空
        3. 两个结点的值不相等
        因为对称，要比较左和右：左的左vs右的右 + 左的右vs右的左
        :param left:
        :param right:
        :return:
        """
        if left is None and right is None: return True
        if left is None or right is None: return False
        if left.val != right.val: return False
        return self.dfs(left.left, right.right) and self.dfs(left.right, right.left)


class TreeTransfer:
    """
    108. 将有序数组转化为二叉搜索树
    给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树
    输入：nums = [-10,-3,0,5,9]
    输出：[0,-3,9,-10,null,5]
    解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(nums, left, right):
            if left >= right:
                return None
            mid = (left + right) // 2
            this_node = TreeNode(nums[mid])
            this_node.left = helper(nums, left, mid)
            this_node.right = helper(nums, mid + 1, right)
            return this_node

        return helper(nums, 0, len(nums))