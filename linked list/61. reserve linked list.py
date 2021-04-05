"""
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL


时间复杂度：O(n)
空间复杂度：O(1)
"""


def rotateRight(self, head: ListNode, k: int) -> ListNode:
    """
    1. 找到链表长度
    2. 从右往左倒数第k个，就是从左到右length-k+1个
    :param self:
    :param head:
    :param k:
    :return:
    """
    if not head or not head.next or k == 0:
        return head
    tail, length = head, 1
    # 1. 找到尾结点，形成环
    while tail.next:
        # 获得链表长度
        tail, length = tail.next, length + 1

    tail.next = head
    # 2.向右移动尾部结点 length - k 步
    k = k % length
    # 然后我们找到新链表的最后一个节点（即原链表的第 (n - 1) - (k mod n) 个节点）
    for _ in range(length - k):
        tail = tail.next

    # 移动后的尾结点的下一个结点就是新链表的头结点，找到断开它
    head = tail.next
    tail.next = None
    return head
