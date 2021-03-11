class SortDemo(object):
    """
    O(nlogn)
    """
    def mergeSort(self, nums: [int], l, r):
        def _merge(nums: [int], l, r):
            #  
            pass

        if l >=r:
            return
        mid = l +r //2
        # 分开
        self.mergeSort(nums, l, mid)
        self.mergeSort(nums, mid, r)
        # 合并
        _merge()




res = [2, 9, 3, 6, 4, 1]

print(res)
