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
