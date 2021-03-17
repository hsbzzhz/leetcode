"""
inOrder:  左 中 右
preOrder(先序遍历)：中 左 右
postOrder：左 右 中

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    """
    输入：root = [1,2,3,null,null,4,5]
    输出：[1,2,3,null,null,4,5]
    """
    def preodertravel(self, root, res: str):
        if root == None:
            res += 'None,'
        else:
            res += str(root.val)
            res += ','
            self.preodertravel(root.left, res)
            self.preodertravel(root.right, res)
        return res

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = ''
        self.preodertravel(root, res)
        return res

    def preorderbuild(self, data):
        temp = data.pop(0)
        if temp == 'Null':
            return None
        else:
            root = TreeNode(int(temp))
            root.left = preorderbuild(data)
            root.right = preorderbuild(data)
        return root

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')

        return self.preorderbuild(data)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

    # def serialize(self, root):
    #     """Encodes a tree to a single string.
    #
    #     :type root: TreeNode
    #     :rtype: str
    #     """
    #     self.res = ""
    #
    #     def dfs_NLR(rt: TreeNode) -> None:
    #         if rt == None:
    #             self.res += 'None,'
    #         else:
    #             self.res += str(rt.val)
    #             self.res += ','
    #             dfs_NLR(rt.left)
    #             dfs_NLR(rt.right)
    #
    #     dfs_NLR(root)
    #     return self.res
    #
    # def deserialize(self, data):
    #     """Decodes your encoded data to tree.
    #
    #     :type data: str
    #     :rtype: TreeNode
    #     """
    #     data = data.split(',')
    #
    #     def dfs() -> None:
    #         p_str = data.pop(0)
    #         if (p_str == 'None'):
    #             return None
    #         else:
    #             root = TreeNode(int(p_str))
    #             root.left = dfs()
    #             root.right = dfs()
    #         return root
    #
    #     return dfs()


