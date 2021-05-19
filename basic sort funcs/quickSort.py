class SortDemo(object):
    """
    先治再分
    归并排序，简单来说就是先将数组不断细分成最小的单位，然后每个单位分别排序，排序完毕后合并，重复以上过程最后就可以得到排序结果。

    快速排序，简单来说就是先选定一个基准元素，然后以该基准元素划分数组，再在被划分的部分重复以上过程，最后可以得到排序结果。
    O(nlogn)
    最坏情况O(n^2): 基线没找好，把除基线外的元素都归到了另一个列中
    """

    def quickSort(self, nums: []):
        if len(nums) < 2:
            return nums  # 基线条件
        else:
            pivot = nums[0]  # 递归条件
            less = [i for i in nums[1:] if i < pivot]  # 将所有小于基准值的元素组成一个数组
            greater = [i for i in nums[1:] if i > pivot]  # 将所有大于基准值的元素组成一个数组

            return self.quickSort(less) + [pivot] + self.quickSort(greater)


raw = [10, 6, 1, 0, 5]

demo = SortDemo()
print(demo.quickSort(raw))
