from typing import List


class Solution:
    """
    给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

    示例 1：

    输入：nums = [10,9,2,5,3,7,101,18]
    输出：4
    解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
    示例 2：

    输入：nums = [0,1,0,3,2,3]
    输出：4
    示例 3：

    输入：nums = [7,7,7,7,7,7,7]
    输出：1

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def longestConsecutive(self, nums: List[int]) -> int:
        """
        dp 方法
        :param nums:
        :return:
        """
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):  # 内循环从头到i进行遍历
                if nums[j] < nums[i]:  # 如果递增
                    dp[i] = max(dp[i], dp[j] + 1)  # 初始值为1，dp[j]+1 : 累加
        return max(dp)

    """
    还有二分法+贪心的方法
    """