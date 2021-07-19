from typing import List

"""
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

 

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        max_res = [nums[0]] * (len(nums))
        min_res = [nums[0]] * (len(nums))

        for i in range(1, len(nums)):
            max_res[i] = max(
                max_res[i - 1] * nums[i], min_res[i - 1] * nums[i], nums[i]
            )
            min_res[i] = min(
                max_res[i - 1] * nums[i], min_res[i - 1] * nums[i], nums[i]
            )

        ans = nums[0]
        for i in range(1, len(nums)):
            ans = max(ans, max_res[i])

        return ans

    def maxProduct_improve(self, nums: List[int]) -> int:
        """
        不甚理解啊
        :param nums:
        :return:
        """
        max_f = min_f = ans = nums[0]
        for i in range(1, len(nums)):
            mx, mn = max_f, min_f
            max_f = max(mx * nums[i], nums[i], mn * nums[i])
            min_f = min(mn * nums[i], nums[i], mx * nums[i])
            ans = max(max_f, ans)
        return ans


nums = [2, 3, -2, 4]
demo = Solution()
print(demo.maxProduct_improve(nums))
