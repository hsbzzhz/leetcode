def binary_search(lst: [], target):
    """
    循环实现： O(logn)
    :param lst:
    :param target:
    :return:
    """
    low, high = 0, len(lst) -1
    while low <= high:
        mid = (low+high)//2

        if lst[mid] == target:
            return mid
        elif lst[mid] > target:
            high = mid -1
        else:
            low = mid + 1


def binary_recursion(lst: [], target, left, right):
    if left > right:
        # 递归出口
        return None
    mid = (left+right)//2
    if lst[mid] == target:
        return mid
    elif lst[mid] > target:
        right = mid - 1
    else:
        left = mid + 1
    return binary_recursion(lst, target, left, right)