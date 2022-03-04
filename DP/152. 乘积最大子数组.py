from typing import List

"""
给你一个整数数组 nums，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。


示例 1:

输入: [2,3,-2,4]
输出: 6
解释:子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释:结果不能为 2, 因为 [-2,-1] 不是子数组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        求数组中子区间的最大乘积，
        因为负数乘以负数，会变成正数，所以解这题的时候我们需要维护两个变量，当前的最大值，以及最小值，
        最小值可能为负数，但没准下一步乘以一个负数，当前的最大值就变成最小值，而最小值则变成最大值了

        对于同样的动归方程，需要求其最大值和最小值
        :param nums:
        :return:
        """
        max_res = [nums[0]] * (len(nums))
        min_res = [nums[0]] * (len(nums))

        for i in range(1, len(nums)):
            max_res[i] = max(
                max_res[i - 1] * nums[i], min_res[i - 1] * nums[i], nums[i]
            )
            min_res[i] = min(
                max_res[i - 1] * nums[i], min_res[i - 1] * nums[i], nums[i]
            )

        return max(max_res)
    """
    思考：
    1. 是否可以使用双指针来做：可能因为负数的原因，双指针无法记录负数
    """

nums = [2, 3, -2, 4]
demo = Solution()
print(demo.maxProduct(nums))
