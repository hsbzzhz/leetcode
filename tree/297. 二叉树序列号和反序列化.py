"""
inOrder:  左 中 右
preOrder(先序遍历)：中 左 右
postOrder：左 右 中


序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

 

示例 1：

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
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
        """
        build a tree with given list
        :param data:
        :return:
        """
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
