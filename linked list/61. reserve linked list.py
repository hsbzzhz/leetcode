"""
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL

"""


def rotateRight(self, head: ListNode, k: int) -> ListNode:
    if not head or k == 0:
        return head
    tail, length = head, 1
    while tail.next:
        tail, length = tail.next, length + 1

    k, temp = k % length, head
    if k == 0:
        return head

    for _ in range(length - k - 1):
        temp = temp.next

    new_head = temp.next
    temp.next = None
    tail.next = head

    return new_head
