class Solution:
    """
    反转一个单链表。
    e.g.
    输入： 1 2 3 4 5-> null
    输出： 5 4 3 2 1 -> null
    """
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        newhead = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return newhead