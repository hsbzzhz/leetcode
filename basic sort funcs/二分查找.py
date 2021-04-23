class sort(object):
    def binary_search(self, lst: [], target):
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
                high = mid - 1
            else:
                low = mid + 1


    def binary_recursion(self, lst: [], target, left, right):
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
        return self.binary_recursion(lst, target, left, right)


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def find_target_by_index(index):
            count, res = 0, 0
            p1, p2 = 0, 0
            while p1+p2 <= index:
                if p1 >= len(nums1):
                    res = nums2[p2]
                    p2 += 1
                elif p2 >= len(nums2):
                    res = nums1[p1]
                    p1 += 1
                elif nums1[p1] < nums2[p2]:
                    res = nums1[p1]
                    p1 += 1
                else:
                    res = nums2[p2]
                    p2 += 1
            return res

        long = len(nums1) + len(nums2)
        index = long // 2
        if long %2 == 0:
            res = (find_target_by_index(index)+find_target_by_index(index+1))/2
        else:
            res = find_target_by_index(index)

        return res




demo = Solution()
num1 = [1, 2]
num2 = [3, 4]
mid = demo.findMedianSortedArrays(num1, num2)
print(mid)