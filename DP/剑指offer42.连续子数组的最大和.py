from typing import List


class Solution:
    """
    输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

    要求时间复杂度为O(n)。

    示例1:

    输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
    输出: 6
    解释: 连续子数组 [4,-1,2,1] 的和最大，为6。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]] * len(nums)
        index = []
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            if dp[i-1] + nums[i] > nums[i]:
                index.append(index[-1] + nums[i])
            else:
                index.append([nums[i]])
        print(index)
        return max(dp)


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
demo = Solution().maxSubArray(nums)
print(demo)