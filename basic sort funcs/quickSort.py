class SortDemo(object):
    """
    先治再分

    快速排序，简单来说就是先选定一个基准元素，然后以该基准元素划分数组，再在被划分的部分重复以上过程，最后可以得到排序结果。
    O(nlogn)
    最坏情况O(n^2): 基线没找好，把除基线外的元素都归到了另一个列中
    """

    def quickSort(self, nums: []):
        """
        摘自算法图解
        效率太低，最好不要用
        :param nums:
        :return:
        """
        if len(nums) < 2:
            return nums  # 基线条件
        else:
            pivot = nums[0]  # 递归条件
            less = [i for i in nums[1:] if i < pivot]  # 将所有小于基准值的元素组成一个数组
            greater = [i for i in nums[1:] if i > pivot]  # 将所有大于基准值的元素组成一个数组

            return self.quickSort(less) + [pivot] + self.quickSort(greater)


class Solution:
    """
    215. 求 topk 问题
    使用快排来解决
    ref. https://leetcode-cn.com/problems/kth-largest-element-in-an-array/solution/ji-yu-kuai-pai-de-suo-you-topkwen-ti-jia-ylsd/
    """

    def partition(self, nums, left, right):
        pivot = nums[left]  # 初始化一个待比较数据
        while left < right:
            while left < right and nums[right] >= pivot:  # 从后往前查找，直到找到一个比pivot更小的数
                # while left < right and nums[right] <= pivot:  # 如果改成这样，就是从大到小排序（1）
                right -= 1
            # if nums[right] < pivot:
            nums[left] = nums[right]  # 将更小的数放入左边

            while left < right and nums[left] <= pivot:  # 从前往后找，直到找到一个比pivot更大的数
                # while left < right and nums[left] >= pivot:  # 如果改成这样，就是从大到小排序（2）
                left += 1
            # if nums[left] > pivot
            nums[right] = nums[left]  # 将更大的数放入右边
        # 循环结束，left 与 right 重合
        nums[left] = pivot  # 待比较数据放入最终位置
        return left  # 返回待比较数据最终位置

    def quickSort(self, nums, left, right):
        if left < right:
            index = self.partition(nums, left, right)  # 寻找 mid
            self.quickSort(nums, left, index - 1)  # 跳过 mid 进行排序
            self.quickSort(nums, index + 1, right)
        return nums

    def top_split(self, nums, k, left, right):
        """
        原地排序，使得前 k 个数从小到大排序
        理解不能！！！@todo
        """
        if left < right:
            index = self.partition(nums, left, right)
            if index == k:
                return
            elif index < k:  # k 大一点，那边目标元素就在右侧
                self.top_split(nums, k, index + 1, right)
            elif index > k:  # k 小一些，那就是在左侧
                self.top_split(nums, k, left, index - 1)

    def topk_small(self, nums, k):
        self.top_split(nums, k, 0, len(nums) - 1)
        print(nums)
        return nums[k - 1]  # 右边是开区间，需要-1

    def topk_sort_right(self, nums, k):
        self.top_split(nums, len(nums) - k, 0, len(nums) - 1)
        topk = nums[len(nums) - k :]
        self.quickSort(topk, 0, len(topk) - 1)
        # print(topk)
        return nums[: len(nums) - k] + topk  # 只排序后k个数字


raw = [3, 2, 3, 1, 2, 4, 5, 5, 6]


demo = Solution()
# res = demo.partition(raw, 0, len(raw)-1)
res = demo.quickSort(raw, 0, len(raw) - 1)

print(res)
