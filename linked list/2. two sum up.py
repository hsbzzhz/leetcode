"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
"""


def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

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
