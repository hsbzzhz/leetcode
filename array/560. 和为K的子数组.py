"""
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarray-sum-equals-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
class Solution:
    """
    前缀和的思路是这样的，对于一个给定的数组 nums，我们额外开辟一个前缀和数组进行预处理
    https://github.com/labuladong/fucking-algorithm/blob/master/%E7%AE%97%E6%B3%95%E6%80%9D%E7%BB%B4%E7%B3%BB%E5%88%97/%E5%89%8D%E7%BC%80%E5%92%8C%E6%8A%80%E5%B7%A7.md
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_array = [0] * (len(nums) +1)
        # 构造前缀和
        for i in range(len(nums)):
            sum_array[i + 1] = sum_array[i] + nums[i]
        ans = 0
        for i in range(1, len(sum_array)):
            for j in range(0, i):
                # sum of nums[j..i - 1]
                if sum_array[i] - sum_array[j] == k:
                    ans+=1
        return ans

    def subarraySum1(self, nums: List[int], k: int) -> int:
        # 利用字典，优化至O(n)
        pass