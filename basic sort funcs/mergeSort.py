class SortDemo(object):
    """
    O(nlogn)
    """

    def mergeSort(self, nums: [int], l, r):
        def _merge(nums: [int], l, m, r):
            # 左右两边排好了序，把左右两边合并
            res = []
            p1 = l
            p2 = m + 1
            while (p1 < mid) or (p2 < r):
                if p1 == mid:
                    res.append(nums[p2])
                    p2 += 1
                elif p2 == r:
                    res.append(nums[p1])
                    p1 += 1
                elif nums[p1] < nums[p2]:
                    res.append(nums[p1])
                    p1 += 1
                else:
                    res.append([nums[p2]])
                    p2 += 1
            # 深度拷贝
            for i in range(len(res)):
                nums[l+i] = res[i]

        if l == r:
            return None
        mid = (l + r) // 2
        # 分开
        self.mergeSort(nums, l, mid)
        self.mergeSort(nums, mid+1, r)
        # 合并
        _merge(nums, l, mid, r)


res = [2, 9, 3, 6, 4, 1]
demo = SortDemo()
print(demo.mergeSort(res, 0, len(res)))