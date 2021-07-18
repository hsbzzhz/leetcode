from typing import List


# test = [1,2,3,4,5]


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    nums1 = nums1[:m]
    nums2 = nums2[:n]
    p = q = 0
    while p < m and q < n:
        if nums1[p] < nums2[q]:
            nums1.append(nums1[p])
            p += 1
        else:
            nums1.append(nums2[q])
            q += 1
    if p == m:
        nums1.extend(nums2[q:])
    if q == n:
        nums1.extend(nums1[p:])
    nums1 = nums1[m:]
    print(nums1)

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
merge(nums1, m, nums2, n)