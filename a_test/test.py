from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # merge into one array
        res = []
        i = j = 0
        while i < len(nums1) or j < len(nums2):
            if j == len(nums2):
                res.extend(nums1[i:])
                break
            elif i == len(nums1):
                res.extend(nums2[j:])
                break
            elif nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                res.append(nums2[j])
                j += 1
        length = len(nums1) + len(nums2)
        if length % 2 == 0:
            mid = length // 2
            return (res[mid-1] + res[mid])/2
        else:
            mid = length // 2
            return res[mid]

demo = Solution()
res = demo.findMedianSortedArrays([1,2], [3])
print(res)