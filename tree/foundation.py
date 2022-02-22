from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    """
    dfs 和 bfs
    ref. https://blog.csdn.net/mengmengdajuanjuan/article/details/84313361
    """
    # dfs
    def preorder(self, TreeNode):
        # 前序遍历: 根 - 左 - 右
        if TreeNode is None:
            return
        print(TreeNode.val)
        self.preorder(TreeNode.left)
        self.preorder(TreeNode.right)

    def inorder(self, TreeNode):
        # 中序遍历：左 - 根 - 右
        if TreeNode is None:
            return
        self.inorder(TreeNode.left)
        print(TreeNode.val)
        self.inorder(TreeNode.right)

    def postorder(self, TreeNode):
        # 后序遍历： 左 - 右 - 根
        if TreeNode is None:
            return " "
        if TreeNode.left:
            self.postorder(TreeNode.left)
        if TreeNode.right:
            self.postorder(TreeNode.right)

        print(TreeNode.val)

    def bfs_order(self, TreeNode):
        """
        时间空间复杂度为 O(n)
        BFS

        尾部入队，头部出队
        :param root:
        :return:
        """
        queue = [TreeNode]
        while queue:
            # 推出第一个元素，队首出队
            node: TreeNode = queue.pop(0)
            # 层次遍历，从左至右
            print(node.val)   # 实际上，只有这里在遍历，下面是在维护队列
            # 左右节点依次队尾入队，
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


class FindDepth:
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
        if not root:
            return 0  # 必须要是0， 应该要参与max运算
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
        if p is None and q is None:  # 都为空的话，显然相同
            return True
        elif p is None or q is None:  # 一个为空，一个非空，显然不同
            return False
        elif p.val != q.val:  # 两个都非空，但 val 不一样也不行
            return False
        else:
            # 分别比较p q两个的左右结点
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


class BST(object):
    """
    98. 验证搜索二叉树
    https://leetcode-cn.com/problems/validate-binary-search-tree/
    定义： left.val < root.val < right.val
    """

    def isValidBST(self, root):
        def is_valid_bst(root, min, max):
            # O(n)
            # https://mp.weixin.qq.com/s/SuGAvV9zOi4viaeyjWhzDw
            if not root:  # base case
                return True
            # min 和 max 的限制
            if min and root.val <= min.val:
                return False
            if max and root.val >= max.val:
                return False
            # 限定左子树的最大值是 root.val，右子树的最小值是 root.val
            return is_valid_bst(root.left, min, root) and is_valid_bst(
                root.right, root, max
            )

        return is_valid_bst(root, None, None)

    pre = float("-inf")

    def inorder(self, root):
        """
        闭包实现，
        中序遍历递归版
        :param root:
        :return:
        """
        nonlocal pre
        if not root:
            return True
        left = self.inorder(root.left)
        if root.val <= pre:
            return False
        pre = root.val
        right = self.inorder(root.right)
        return left and right


class FindDif:
    """
    101. 对称二叉树
    O(n)
    """

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
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
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
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

    bst: 左 < 中 < 右
    """

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """
        因题目要求构造一棵「高度平衡」的树，所以我们在选取节点时选择数组的中点作为根节点，以此来保证平衡性。
        中序遍历
        时间复杂度：O(n)
        空间复杂度：O(log(n))
        :param nums:
        :return:
        """
        if not nums:
            return None
        # 找到中点作为根节点
        mid_idx = len(nums) // 2
        node = TreeNode(nums[mid_idx])

        # 递归构建左右子树
        node.left = self.sortedArrayToBST(nums[:mid_idx])
        node.right = self.sortedArrayToBST(nums[mid_idx + 1 :])

        return node


class Reserve(object):
    """
    226. 翻转二叉树
    示例：

    输入：

         4
       /   \
      2     7
     / \   / \
    1   3 6   9
    输出：

         4
       /   \
      7     2
     / \   / \
    9   6 3   1

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/invert-binary-tree
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def invertTree(self, root):
        """
        使用前序遍历
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        if (root.left is None) and (root.right is None):
            return root

        temp = root.left
        root.left = root.right
        root.right = temp

        # root.left, root.right = root.right, root.left

        # 递归翻转左右子树
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
