"""
给定一个单链表 L 的头节点 head ，单链表 L 表示为：

L0→ L1→ … → Ln-1→ Ln
请将其重新排列后变为：

L0→Ln→L1→Ln-1→L2→Ln-2→ …

不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/LGjMqU
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


"""
解题 思路：
1. 找到链表中心节点
2，翻转中心节点的后半部分
3。合并前半部分，和翻转后的部分
"""

class Solution:
    class Solution:
        def reorderList(self, head: ListNode) -> None:
            if not head:
                return

            mid = self.middleNode(head)
            l1 = head
            l2 = mid.next
            mid.next = None
            l2 = self.reverseList(l2)
            self.mergeList(l1, l2)

        def middleNode(self, head: ListNode) -> ListNode:
            """
            用快慢指针，求得链表的中心节点
            1。 快指针走两步，
            2。 慢指针走一步
            :param head:
            :return:
            """
            slow = fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def reverseList(self, head: ListNode) -> ListNode:
            """
            双指针，迭代翻转链表
            :param head:
            :return:
            """
            prev = None
            curr = head
            while curr:
                nextTemp = curr.next
                curr.next = prev
                prev = curr
                curr = nextTemp
            return prev

        def mergeList(self, l1: ListNode, l2: ListNode):
            """
            合并链表
            :param l1:
            :param l2:
            :return:
            """
            while l1 and l2:
                """
                这个合并过程 和 用循环实现链表翻转的步骤很像
                """
                # 同时遍历 l1 和 l2
                l1_tmp = l1.next   #保留l1的next
                l2_tmp = l2.next

                l1.next = l2  # l1 的 next 就是 l2
                l1 = l1_tmp  # 然后链表向前进，等于l1 = l1.next， 但是因为l1.next已经是l2了，所以要之前的l1_tmp

                l2.next = l1
                l2 = l2_tmp
