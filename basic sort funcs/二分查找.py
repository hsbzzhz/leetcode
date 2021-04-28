class Sort(object):
    def binary_search(self, lst: [], target):
        """
        循环实现： O(logn)
        :param lst:
        :param target:
        :return:
        """
        low, high = 0, len(lst) -1   # 注意
        while low <= high:
            mid = low + (high - low)//2
            if lst[mid] == target:
                return mid
            elif lst[mid] > target:
                high = mid - 1
            elif lst[mid] < target:
                low = mid + 1
        return -1  #没找到的情况

    def binary_recursion(self, lst: [], target, left, right):
        """
        递归实现
        :param lst:
        :param target:
        :param left:
        :param right:
        :return:
        """
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

    def binary_left_bound(self, lst: [], target):
        # 搜索区间为[left, right]
        left, right = 0, len(lst) - 1
        while left <= right:
            # 循环返回条件是 left == right, 但是找到target会一直往左边缩进，直至两个指针指向同一个元素
            mid = (left + right)//2
            if lst[mid] == target:
                # 收缩右侧边界，
                right = mid - 1
            elif lst[mid] < target:
                left = mid + 1
            elif lst[mid] > target:
                right = mid - 1

        # 检查left边界以及没有找到的情况
        if left >= len(lst) or lst[left] != target:  # 只判断了有没有出右边界，因为 index是从0开始，难道还能index为负数?
            return -1
        return left

    def binary_right_bound(self, lst:[], target):
        left, right = 0, len(lst) - 1
        while left <= right:
            mid = (left + right)//2
            if lst[mid] == target:
                # 收缩左边界
                left = mid + 1
            elif lst[mid] < target:
                left = mid + 1
            elif lst[mid] > target:
                right = mid - 1
        if right < 0 or lst[right] != target:  # 检查right的越界情况
            return -1
        return right


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
num3 = [1,2,2,2,3,4,8]
# mid = demo.findMedianSortedArrays(num1, num2)

paixu = Sort()
# res = paixu.binary_left_bound(num3, 2)
res = paixu.binary_right_bound(num3, 2)
print(res)
