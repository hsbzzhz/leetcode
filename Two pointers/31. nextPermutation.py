class Solution(object):
    """
    下一个排列
    1 4 3 2 0
    2 0 1 3 4
    """

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums

        i = len(nums) - 2
        while i >= 0 & nums[i] >= nums[i + 1]:
            i -= 1
        if i < 0:
            nums = nums[::-1]
