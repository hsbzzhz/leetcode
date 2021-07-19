from typing import List


class Solution:
    def longestConsecutive_0(self, nums: List[int]) -> int:
        # 这个算法有问题，
        # 对 case [0,1,0,3,2,3] 而言，[013] 而不能计算到 [0123]
        res = 1
        for i in range(len(nums)):
            length = 1
            temp = nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] > temp:
                    temp = nums[j]
                    length += 1
            res = max(res, length)
        return res

    def longestConsecutive(self, nums: List[int]) -> int:
        # 用动规来做
        if not nums:
            return 0
        dp = [1] * len(nums)  # dp 存每个位置的最长连续序列
        for i in range(len(nums)):
            for j in range(i):  # 对 每个 i 都从头进行计算，
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)  # 在0，i范围中求得最大数， 复杂！
        return max(dp)
