"""
102. 二叉树的层序遍历
https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
"""


class Solution(object):
    def levelOrder(self, root):
        """
        O(n)
        :param root:
        :return:
        """
        if not root:
            return []
        queue = [root]
        res = []
        while len(queue) > 0:
            each_level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                each_level.append(node.val)  # 在队尾添加元素
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(each_level)
        return res

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        """
		给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

		例如：
		给定二叉树 [3,9,20,null,null,15,7],

				3
			   / \
			  9  20
				/  \
			   15   7
		返回锯齿形层序遍历如下：

		[
		  [3],
		  [20,9],
		  [15,7]
		]

		来源：力扣（LeetCode）
		链接：https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal
		著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
		:param root:
		:return:
		"""
        if not root:
            return []
        queue = [root]
        res = []
        is_order = True
        while len(queue) > 0:
            level_queue = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                if is_order:
                    level_queue.append(node.val)  # 在头部加元素
                else:
                    level_queue.insert(0, node.val)
                if node.left:
                    queue.append(node.left)  # 在尾部加元素
                if node.right:
                    queue.append(node.right)
            res.append(level_queue)
            is_order = not is_order
        return res
