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
            if nums[mid] >= nums[l]:    # 比二分查找多的部分
                # 如果落在大的数组区间
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                # 如果落在小的数组区间
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

    """
    https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/
    https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/
    衍生题：剑指 Offer 11. 旋转数组的最小数字
    153, 寻找旋转排序数组中的最小值
    求最小的数
    """

    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        l, r = 0, len(numbers) - 1
        while l < r:
            mid = (l + r) // 2
            if numbers[mid] > numbers[r]:
                l = mid + 1
            elif numbers[mid] < numbers[r]:
                r = mid
            else:
                r -= 1
        return numbers[l]


test_case = [4, 5, 6, 7, 0, 1, 2]
obj = Solution()
res = obj.search(test_case, target=1)
print(res)
