class Solution:
    """
    反转一个单链表。
    e.g.
    输入： 1 2 3 4 5-> null
    输出： 5 4 3 2 1 -> null
    """

    def reverseList(self, head: ListNode) -> ListNode:
        """
        时间空间复杂度都是O(n)
        """
        if not head or not head.next:
            return head
        newhead = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return newhead

    def reverseList2(self, head: ListNode) -> ListNode:
        """
        方法二：双指针迭代
        时间复杂度O(n)
        空间为O(1)
        """
        prev = None
        curr = head
        """
        我们可以申请两个指针，第一个指针叫 pre，最初是指向 null 的。
        第二个指针 cur 指向 head，然后不断遍历 cur。
        每次迭代到 cur，都将 cur 的 next 指向 pre，然后 pre 和 cur 前进一位。
        都迭代完了(cur 变成 null 了)，pre 就是最后一个节点了。
        
        作者：wang_ni_ma
        链接：https://leetcode-cn.com/problems/reverse-linked-list/solution/dong-hua-yan-shi-206-fan-zhuan-lian-biao-by-user74/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        """
        while curr:
            # 记录当前节点的下一个节点
            temp = curr.next
            # 然后将当前节点指向pre
            curr.next = prev
            # pre和cur节点都前进一位
            prev = curr
            curr = temp
        return  prev