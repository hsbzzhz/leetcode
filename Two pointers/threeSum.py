"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例：
给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break  # 特殊情况，最小的数字都大于0
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # 保证第第一个数 index i 不会重复
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                    # 判断左界和右界是否和下一位置重复，去除重复解。并同时将 L,RL,R 移到下一位置，寻找新的解
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                    while r > l and nums[l] == nums[l - 1]:
                        l += 1

                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
        return res
