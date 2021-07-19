from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(track: [], start):
            res.append(track[:])
            for i in range(start, len(nums)):
                track.append(nums[i])
                backtrack(track, i + 1)
                track.pop()

        res = []
        backtrack([], 0)
        return res
