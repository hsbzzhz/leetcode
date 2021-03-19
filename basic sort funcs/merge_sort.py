def SortDemo(arr):
    """
    O(nlogn)
    最坏情况也能保证 O(nlogn)
    mergeSort是分, 把列表分开
    :param arr:
    :return:
    """
    if len(arr) < 2:
        return arr
    middle = len(arr) // 2
    left, right = arr[:middle], arr[middle:]
    # 最后把多个列表合并
    return merge(mergeSort(left), mergeSort(right))


def merge(left, right):
    """
    左右两边排好了序，把左右两边合并
    :param left:
    :param right:
    :return: 把左右两个有序list合并成一个, 直至左右list中仅存在一个元素
    """
    result = []
    # 如果两个子列表都有
    while left and right:
        # 把小的元素弹出
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    # 单个list存在元素的情况
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


# test case
srr = [13, 4, 5, 12, 15, 21, 16, 23, 89]
res = SortDemo(srr)
print(res)

#########################################################################################

class SortDemo2(object):
    """
    O(nlogn)
    最坏情况也能保证 O(nlogn)
    """

    def mergeSort2(self, nums: [int], l, r):
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