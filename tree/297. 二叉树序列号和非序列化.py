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
    O(n) 依据前序遍历的复杂度
    输入：root = [1,2,3,null,null,4,5]
    输出：[1,2,3,null,null,4,5]
    """

    def serialize(self, root):
        """
        Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.res = ""

        def preodertravel(root: TreeNode) -> None:
            if root == None:
                self.res += "None,"
            else:
                self.res += str(root.val)
                self.res += ","
                preodertravel(root.left)
                preodertravel(root.right)

        self.preodertravel(root, self.res)
        return self.res

    def preorderbuild(self, data: []):
        temp_str = data.pop(0)
        if temp_str == "None":
            return None
        else:
            root = TreeNode(int(temp_str))
            root.left = self.preorderbuild(data)
            root.right = self.preorderbuild(data)
        return root

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        if len(data) <= 1:
            return None

        return self.preorderbuild(data)
