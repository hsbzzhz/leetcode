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
        双指针
        时间复杂度：O(n^2)
        空间复杂度：O(1)
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
            left, right = i + 1, len(nums) - 1  # 左指针只会右移动，右指针只会左移
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    res.append((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                    # 判断左界和右界是否和下一位置重复，去除重复解。并同时将 L,R 移到下一位置，寻找新的解
                    while left < right and nums[right] == nums[right + 1]:   # 跳过重复的, right的上一位是 right + 1
                        right -= 1
                    while left < right and nums[left] == nums[left - 1]:   # 跳过重复的， left 的上一位是 left - 1
                        left += 1

                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
        return res

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        """
        对于重复解，把所有答案算出来以后再进行去重处理
        :param nums:
        :return:
        """
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            l, r = i + 1, len(nums) - 1
            while l < r:
                temp = nums[i] + nums[l] + nums[r]
                if temp == 0:
                    res.append((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif temp < 0:
                    l += 1
                elif temp > 0:
                    r -= 1

        return list(set(res))
