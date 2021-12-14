class SortDemo(object):
    """
    O(n^2)
    希尔排序，不稳定
    """

    def shellSort(self, nums: list):
        n = len(nums)
        gap = n // 2
        while gap > 0:
            # 以gap的index进行插入排序
            for i in range(gap, n):  # 第一层循环
                j = i
                while j >= gap and nums[j - gap] > nums[j]:  # 第二层
                    nums[j - gap], nums[j] = nums[j], nums[j - gap]
                    j -= gap
            # 一轮循环后更新步长
            gap = gap // 2
        return nums


raw = [10, 6, 1, 0, 5]

demo = SortDemo()
print(demo.shellSort(raw))
