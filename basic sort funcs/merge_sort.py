def mergeSort(arr):
    if len(arr) < 2:
        return arr
    middle = len(arr) // 2
    left, right = arr[:middle], arr[middle:]
    return merge(mergeSort(left), mergeSort(right))


# merge 是治， mergeSort是分
def merge(left, right):
    """
    :param left:
    :param right:
    :return: 把左右两个有序list合并成一个, 直至左右list中仅存在一个元素
    """
    result = []
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
res = mergeSort(srr)
print(res)
