class Solution(object):
    """
    33. 搜索旋转排序数组
    升序排列的整数数组 nums 在预先未知的某个点上进行了旋转（例如， [0,1,2,4,5,6,7] 经旋转后可能变为 [4,5,6,7,0,1,2] ）。

    请你在数组中搜索 target ，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

 

    示例 1：

    输入：nums = [4,5,6,7,0,1,2], target = 0
    输出：4
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
