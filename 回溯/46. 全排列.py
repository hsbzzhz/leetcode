class Solution:
    """
    给定一个 没有重复 数字的序列，返回其所有可能的全排列。

    示例:

    输入: [1,2,3]
    输出:
    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]


    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/permutations
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    def permute(self, nums):
        """
        回溯
        时间复杂度：O(n×n!)，其中 n 为序列的长度
        :param nums:
        :return:
        """

        def backtrack(nums: [], p: int, q: int):
            """

            :param nums:
            :param p: 当前要拿 从第一位开始
            :param q: 为链表尾部
            :return:
            """
            if p == q:
                # 递归结束条件，走到最后一个数了
                # 这里要进行深拷贝
                res.append(nums[:])
            else:
                for i in range(p, q):
                    # 先把i位置的数调换到第一位上来，然后对后面数进行递归操作
                    # 就是把每个位置的元素都换到第一位来，然后递归，使得后续每个元素
                    nums[p], nums[i] = nums[i], nums[p]
                    backtrack(nums, p + 1, q)
                    # 为了下一步能够顺利进行，还要把第一个数换回去
                    nums[p], nums[i] = nums[i], nums[p]

        res = []
        backtrack(nums, 0, len(nums))
        return res


demo = Solution()
nums = [1, 2, 3]
print(demo.permute(nums))
