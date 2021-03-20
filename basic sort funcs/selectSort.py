class SortDemo(object):
    """
    O(n^2)
    """

    def selectSort(self, nums: list):
        for i in range(len(nums) - 1):
            # 将起始元素设为最小元素
            min_index = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_index]:
                    min_index = j
            # 最小元素塞到起始位置
            nums[min_index], nums[i] = nums[i], nums[min_index]
        return nums


raw = [10, 6, 1, 0, 5]

demo = SortDemo()
print(demo.selectSort(raw))
