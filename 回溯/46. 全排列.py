class Solution:
    def permute(self, nums):
        """
        回溯
        时间复杂度：O(n×n!)，其中 n 为序列的长度
        :param nums:
        :return:
        """

        def backtrack(nums: [], p: int, q: int):
            if p == q:
                # 递归结束条件，走到最后一个数了
                res.append(nums)
            else:
                for i in range(p, q):
                    # 先把i位置的数调换到第一位上来，然后对后面数进行递归操作
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
