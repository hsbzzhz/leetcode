"""
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder =[3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    """
    时间复杂度：O(n)
    空间复杂度：O(n)
    """

    def buildTree(self, preorder, inorder):
        if not (preorder and inorder):
            return None
        # 根据第一个元素，就能确定根结点
        root = TreeNode(preorder[0])
        # 寻找根结点 在 中序遍历中的位置，左边就是左子树，右边就是右子树
        root_idx = inorder.index(preorder[0])
        # 递归的处理前序数组的左边部分和中序数组的左边部分
        # 递归处理前序数组右边部分和中序数组右边部分
        root.left = self.buildTree(preorder[1 : root_idx + 1], inorder[:root_idx])
        root.right = self.buildTree(preorder[root_idx + 1 :], inorder[root_idx + 1 :])

        return root


"""
作者：wang_ni_ma
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solution/dong-hua-yan-shi-105-cong-qian-xu-yu-zhong-xu-bian/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
