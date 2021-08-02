from typing import List


# test = [1,2,3,4,5]
class HeapSort:
    def heapify(self, nums, n, parent):
        c1 = parent*2 + 1
        c2 = parent*2 + 1
        max_index = parent
        if c1 < n and nums[c1] > nums[max_index]:
            max_index = c1
        if c2 < n and nums[c2] > nums[max_index]:
            max_index = c2

        if max_index != parent:
            nums[parent], nums[max_index] = nums[max_index], nums[parent]
            self.heapify(nums, n, max_index)

    def build_heap(self, nums, n):
        last_node = n -1
        last_parent = (last_node - 1)//2
        while last_parent >= 0:
            self.heapify(nums, n, last_parent)
            last_parent -= 1

    def heap_sort(self, nums, n):
        pass


nums = [2, 4, 5, 1, 17, 3, 7]
test = HeapSort()
res = test.build_heap(nums, len(nums))
print(nums)

class MergeSort():
    def merge_sort(self, nums):
        if len(nums) < 2:
            return nums
        mid = len(nums) //2
        left = nums[:mid]
        right = nums[mid:]
        return self.merge(self.merge_sort(left), self.merge_sort(right))

    def merge(self, left, right):
        res = []
        while left and right:
            if left[0] < right[0]:
                res.append(left[0])
                left.pop(0)
            else:
                res.append(right[0])
                right.pop(0)
        while right:
            res.append(right.pop(0))
        while left:
            res.append(left.pop(0))
        return res





# merge = MergeSort()
# print(merge.merge_sort(nums))