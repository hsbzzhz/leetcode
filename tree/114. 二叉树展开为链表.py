class Solution:
    """
    https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/
    """
    def flatten(self, root: TreeNode) -> None:
        """
        官方题解
        Do not return anything, modify root in-place instead.
        """
        preorderList = list()
        def preorderTraversal(root: TreeNode):
            if not root:
                return
            preorderList.append(root)
            preorderTraversal(root.left)
            preorderTraversal(root.right)
        preorderTraversal(root)
        size = len(preorderList)
        for i in range(1, size):
            prev, curr = preorderList[i - 1], preorderList[i]  # 记录连续两个结点
            prev.left = None  # 把左结点置空
            prev.right = curr  # 把 curr 给右节点