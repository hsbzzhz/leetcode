"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers_0(self, l1: ListNode, l2: ListNode) -> ListNode:
    # loop 版， 看这个
    dummyHead = ListNode(None)  # 创建一个结点
    curr = dummyHead  # 创建一个干活结点，不然遍历完了指针就到最后一个结点去了
    appendix = 0  # 来存sum，初始进化位为0
    while l1 or l2 or appendix:
        # 对 l1 l2 appendix 分别处理，就不用考虑链表长度不一的问题
        if l1:
            appendix += l1.val
            l1 = l1.next
        if l2:
            appendix += l2.val
            l2 = l2.next

        curr.next = ListNode(appendix % 10)  # 注意为curr next结点
        curr = curr.next  # 然后移动curr结点好了
        appendix = appendix // 10  # 一轮循环后把appendix更新为进位，第二轮循环就可以直接用
    return dummyHead.next  # 最后直接把大哥next 结点 返回


def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    # 递归版，尾递归
    def dfs(l, r, i):
        """
        :param l: l1
        :param r: l2
        :param i: 用来保存进位
        :return: 合并后的node
        """
        if not l and not r and not i:
            return None
        s = (l.val if l else 0) + (r.val if r else 0) + i
        node = ListNode(s % 10)  # 取余，当前位的值
        node.next = dfs(l.next if l else None, r.next if r else None, s // 10)
        return node

    return dfs(l1, l2, 0)
