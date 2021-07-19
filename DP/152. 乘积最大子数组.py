from typing import List


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
