# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    """
    输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    输出：3
    解释：节点 5 和节点 1 的最近公共祖先是节点 3 。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

    O(n) 递归
 (1） 如果当前结点 root 等于 NULL，则直接返回 NULL
（2） 如果 root 等于 p 或者 q ，那这棵树一定返回 p 或者 q
（3） 然后递归左右子树，因为是递归，使用函数后可认为左右子树已经算出结果，用 left 和 right 表示
（4） 此时若left为空，那最终结果只要看 right；若 right 为空，那最终结果只要看 left
（5） 如果 left 和 right 都非空，因为只给了 p 和 q 两个结点，都非空，说明一边一个，因此 root 是他们的最近公共祖先
（6） 如果 left 和 right 都为空，则返回空（其实已经包含在前面的情况中了）

    """

    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        """
        找p和q分别在哪，如果找到就返回上层根节点，一直返回直至同时找到p 和 q
        :param root:
        :param p:
        :param q:
        :return:
        """
        if root is None:
            return None

        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 如果存在一个，则返回存在的一个
        if left == None:
            return right
        if right == None:
            return left
        if left and right:
            # 如果 p 和 q 都存在，则返回它们的公共祖先；
            return root
        # 如果p q都不存在，则返回null
        return None
