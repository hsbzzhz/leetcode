"""
完全二叉树：
 1. 生成结点顺序，从上往下，从左往右 （对树的深度有要求）
堆（大根堆）：
 1. 完全二叉树
 2. 父节点大于子节点


 堆排序：
 1. 构建一个二叉树，然后转换为大根堆
 2. 把堆顶元素依次取出，就是依次取最大的元素
 """


def heapify(tree: [], n: int, i: int):
    """
    时间复杂度O(h),h为堆的高度
    :param tree: 待排数组
    :param n: 树中结点个数
    :param i: 对哪个结点开始至树的结尾做操作
    :return:
    """
    # 跳出递归条件
    # if i >= n:
    #     return
    c1 = 2 * i + 1
    c2 = 2 * i + 2
    # 确保子结点不出界
    max_index = i
    if c1 < n and tree[c1] > tree[max_index]:
        max_index = c1
    if c2 < n and tree[c2] > tree[max_index]:
        max_index = c2
    if max_index != i:
        tree[i], tree[max_index] = tree[max_index], tree[i]
        # 对该结点子树进行堆化操作, 为了寻找子节点中可能存在最大的数
        heapify(tree, n, max_index)


def build_heap(tree: [], n: int):
    """
    时间复杂度O(nlgn)
    从最后一个结点的父结点依次向上调用堆化，即可完成
    :param tree:
    :param n: 总共结点个数
    :return:
    """
    last_node = n - 1
    last_parent = (last_node - 1) // 2
    while last_parent >= 0:
        # 对遍历过程的每一个非叶子结点，将以其为根的子树维护成大顶堆
        # 最终整个树都满足大顶堆的性质
        heapify(tree, n, last_parent)
        last_parent -= 1


def heap_sort(tree: [], n):
    # O(nlgn)
    # 构造大根堆
    build_heap(tree, n)
    i = n - 1
    while i >= 0:
        # 将遍历到的元素与最后一个堆的元素交换,
        tree[i], tree[0] = tree[0], tree[i]
        # 还剩i个枝
        heapify(tree, i, 0)
        i -= 1


tree = [4, 17, 5, 1, 2, 3, 7]
heapify(tree, len(tree), 0)
print(tree)
build_heap(tree, len(tree))
print(tree)
heap_sort(tree, len(tree))
print(tree)


"""
ref. 
https://zhuanlan.zhihu.com/p/80371429
"""
