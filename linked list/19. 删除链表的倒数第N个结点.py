class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        fast = slow = dummy
        # 先让快指针走n个位
        for i in range(n + 1):
            fast = fast.next
        # 然后两个一起走，一直到快指针到底
        while fast:
            fast = fast.next
            slow = slow.next
        # 跳过倒数第n个结点
        slow.next = slow.next.next
        # 要返回dummy 而不是快慢指针
        return dummy.next
