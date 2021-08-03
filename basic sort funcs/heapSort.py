"""
完全二叉树：
 1. 生成结点顺序，从上往下，从左往右 （对树的深度有要求）
堆（大根堆）：
 1. 完全二叉树 (生成结点的顺序是从上往下，从左往右)
 2. 父节点大于子节点


 堆排序：
 1. 构建一个二叉树，然后转换为大根堆
 2. 把堆顶元素依次取出，就是依次取最大的元素

 ref. https://www.bilibili.com/video/BV1Eb41147dK
 """
from typing import List


class heapSort:
    def heapify(self, tree: [], n: int, i: int):
        """
        从一个结点出发，做交换（使得父节点的值大于子节点），对该结点 下沉 堆化处理

        时间复杂度 O(h), h为堆的高度
        :param tree: 待排数组
        :param n: 树中结点个数
        :param i: last_parent: 对哪个结点开始至树的结尾做操作，倒数第二层
        :return:
        """
        # 跳出递归条件
        # if i >= n:
        #     return
        c1 = 2 * i + 1
        c2 = 2 * i + 2
        # 确保子结点不出界, 和子节点对比，将大的结点序号放在父节点
        # 需要一个中间值来传递节点序号
        max_index = i
        if c1 < n and tree[c1] > tree[max_index]:  # 如果改成 < 号，那就生成一个最小堆，从大到小排序了 (1.)
            max_index = c1
        if c2 < n and tree[c2] > tree[max_index]:  # 如果改成 > 号，那就生成一个最小堆，从大到小排序了 (2.)
            max_index = c2
        if max_index != i:
            tree[i], tree[max_index] = tree[max_index], tree[i]
            # 对该结点子树进行堆化操作, 为了寻找子节点中可能存在最大的数
            self.heapify(tree, n, max_index)

    def build_heap(self, tree: [], heap_size: int):
        """
        构造一个堆，将堆中所有数据重新排序

        时间复杂度 O(nlgn)
        从最后一个结点的父结点依次向上调用堆化，即可完成
        :param tree:
        :param heap_size: 总共结点个数
        :return:
        """
        last_parent = (heap_size - 1) // 2
        while last_parent >= 0:
            # 对遍历过程的每一个非叶子结点，将以其为根的子树维护成大顶堆
            # 最终整个树都满足大顶堆的性质
            self.heapify(tree, heap_size, last_parent)
            last_parent -= 1

    def heap_sort(self, tree: [], heap_size: int):
        # O(nlgn)
        # 构造大根堆
        # 将根结点取出与最后一位做对调，对前面 len-1 个结点进行调整
        self.build_heap(tree, heap_size)
        i = heap_size - 1
        while i >= 0:
            # 将遍历到的元素与最后一个堆的元素交换,
            tree[i], tree[0] = tree[0], tree[i]
            # 还剩i个枝
            self.heapify(tree, i, 0)
            i -= 1


tree = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
heapsort = heapSort()
heapsort.heapify(tree, len(tree), 0)
print(tree)
heapsort.build_heap(tree, len(tree))
print(tree)
heapsort.heap_sort(tree, len(tree))
print(tree)


"""
ref. 
https://zhuanlan.zhihu.com/p/80371429
"""


def findKthLargest(self, nums: List[int], k: int) -> int:
    """
    215. 数组中的第K个最大元素
    :param self:
    :param nums:
    :param k:
    :return:
    """
    n = len(nums)
    self.build_heap(nums, n)
    for i in range(k - 1):
        # 堆顶元素 nums[0] 是最大的元素，将它扔到 nums 尾部去
        nums[n - 1], nums[0] = nums[0], nums[n - 1]
        # 然后默认计算范围缩小 1
        n -= 1
        # 这样一顿操作，那就把最大值放在了 nums[0] 堆顶了
        self.heapify(nums, n, 0)
    return nums[0]
