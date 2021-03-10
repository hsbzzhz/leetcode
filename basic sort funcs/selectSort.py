class SortDemo(object):
    """
    O(n^2)
    """
    def selectSort(self, nums: list):

        def findSmallest(nums: list):
            smallest = nums[0]
            smallest_index = 0
            for i in range(1, len(nums)):
                if nums[i] < smallest:
                    smallest = nums[i]
                    smallest_index = i
            return smallest_index

        res = []
        for i in range(len(nums)):
            smallest = findSmallest(nums)
            res.append(nums.pop(smallest))
        return res


raw = [10, 6, 1, 0, 5]

demo = SortDemo()
print(demo.selectSort(raw))