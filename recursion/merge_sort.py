def mergeSort(arr):
    if (len(arr) < 2):
        return arr
    middle = ((len(arr) + 1) // 2)
    left, right = arr[0:middle], arr[middle:]
    return merge(mergeSort(left), mergeSort(right))


def merge(left: [], right: []):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


# test case
srr = [13, 4, 5, 12, 15, 21, 16, 23, 89]
res = mergeSort(srr)
print(res)
