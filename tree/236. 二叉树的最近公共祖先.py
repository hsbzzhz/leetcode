# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    输出：3
    解释：节点 5 和节点 1 的最近公共祖先是节点 3 。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

    递归   dfs后序遍历
    可展开四种情况讨论
    (1） 当 left 和 right 同时为空 ：说明 root 的左 / 右子树中都不包含 p,q ，返回 null；
    (2)  当 left 和 right 同时不为空 ：说明 p,q 分列在 root 的异侧 （分别在 左 / 右子树），因此 root 为最近公共祖先，返回 root；
    (3)  当 left 为空 ，right 不为空 ：p,q 都不在 root 的左子树中，直接返回 right; (其中有两种情况)
    (4)  当 right 为空 ，left 不为空 ：p,q 都不在 root 的右子树中，直接返回 left; (其中有两种情况)

    """

    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        """
        O(n)
        :param root:
        :param p:
        :param q:
        :return:
        """
        # baseline
        if not root:  # 当越过叶节点，则直接返回 null
            return None
        # 为什么说找到一个就可以
        # 因为:
        # 1 如果 q 是 p 的子孙， 那么肯定先找到的是p，那么p就是 p和q 的公共祖先
        # 2 如果 q 不是 p 的子孙， 那么在到达p之前，肯定会先到达p和q的公共祖先r，然后分别到达p和q，也就可以返回r了
        if root == p or root == q:  # 当 root 等于 p, q，则直接返回 root
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 如果存在一个，则返回存在的一个
        if not left and not right:  # case 1
            return None
        if left and right:  # case 2
            return root
        if not left:  # case 3
            return right
        if not right:  # case 4
            return left
