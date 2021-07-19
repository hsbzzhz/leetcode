from typing import List


class Solution:
    """
    给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

    示例 1：

    输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
    输出：6
    解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/maximum-subarray
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

    """

    def maxSubArray(self, nums: List[int]) -> int:
        """
        DP O(n) O(1)
        当前最大连续子序列和为 pre， 总计最大结果 max_res
        f(i)=max{f(i−1)+nums[i],nums[i]}
        :param nums:
        :return:
        """
        max_res = nums[0]
        pre = 0
        for each in nums:
            pre = max(pre + each, each)
            max_res = max(max_res, pre)
        return max_res

    def maxSubArray2(self, nums: List[int]) -> int:
        dp = [nums[0]]
        for i in range(1, len(nums)):
            temp = max(dp[i - 1] + nums[i], nums[i])
            dp.append(temp)
        return max(dp)


case = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
demo = Solution().maxSubArray2(case)
print(demo)
