from typing import List

"""
给你一个整数数组nums, 数组中的元素 互不相同. 返回该数组所有可能的子集（幂集）.

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。


示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def backtrack(track: [], start):
            res.append(track[:])
            for i in range(start, len(nums)):
                track.append(nums[i])
                backtrack(track, i + 1)
                track.pop(-1)

        res = []
        backtrack([], 0)
        return res
