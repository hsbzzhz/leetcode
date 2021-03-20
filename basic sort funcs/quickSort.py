class SortDemo(object):
    """
    O(nlogn)
    最坏情况O(n^2)
    """

    def quickSort(self, nums: []):
        if len(nums) < 2:
            return nums  # 基线条件
        else:
            pivot = nums[0]  # 递归条件
            less = [i for i in nums[1:] if i < pivot]  # 将所有小于基准值的元素组成一个数组
            greater = [i for i in nums[1:] if i > pivot]  # 将所有大于基准值的元素组成一个数组

            return self.quickSort(less) + [pivot] + self.quickSort(greater)


raw = [10, 6, 1, 0, 5]

demo = SortDemo()
print(demo.quickSort(raw))
