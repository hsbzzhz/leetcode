"""
给定一个正整数数组nums和整数 k，请找出该数组内乘积小于k的连续的子数组的个数。


示例 1:

输入: nums = [10,5,2,6], k = 100
输出: 8
解释: 8 个乘积小于 100 的子数组分别为: [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]。
需要注意的是 [10,5,2] 并不是乘积小于100的子数组。
示例 2:

输入: nums = [1,2,3], k = 0
输出: 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ZVAVXX
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

滑动窗口方法

"""


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        res = 0  #最后结果
        prod = 1 # 子集乘积
        l = 0 # 左指针
        for r in range(len(nums)): # 右指针
            prod *= nums[r]
            while prod >= k and l <= r: # 如果乘积大于target，并且要保证左指针不能越过右指针
                prod /= nums[l]  # 就去掉最左边的元素，直到整个乘积再次小于target
                l += 1 # 相应的左指针也要移动
            if r - l + 1 > 0: # 最后，算上有效子集中所有的子集个数
                res += r - l + 1
        return res
