class Solution(object):
    """


    """

    def search(self, nums, target):
        """
        二分查找法   O(logn)
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


test_case = [4, 5, 6, 7, 0, 1, 2]
obj = Solution()
res = obj.search(test_case, target=1)
print(res)
