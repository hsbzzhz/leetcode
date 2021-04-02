from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        max_res = [nums[0]]*(len(nums))
        min_res = [nums[0]]*(len(nums))
        ans = nums[0]
        # min_res = []
        for i in range(1, len(nums)):
            max_res[i] = max(max_res[i-1]*nums[i], min_res[i-1]*nums[i], nums[i])
            min_res[i] = min(max_res[i-1]*nums[i], min_res[i-1]*nums[i], nums[i])
            ans = max(ans, max_res[i])
        return ans


nums = [2, 3, -2, 4]
demo = Solution()
print(demo.maxProduct(nums))