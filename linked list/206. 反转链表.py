class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return newHead

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
            # 用一个临时变量，保存当前节点的next
            temp = curr.next
            # 翻转：将当前节点指向pre
            curr.next = prev
            # pre和cur节点都前进一位
            prev = curr  # pre 吸收了翻转后到 cur节点
            curr = temp  # 切换到翻转前到 next 节点
        return prev


class Solution2:
    """
    给你单链表的头指针 head 和两个整数left 和 right ，其中left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。

    示例 1：

    输入：head = [1,2,3,4,5], left = 2, right = 4
    输出：[1,4,3,2,5]
    示例 2：

    输入：head = [5], left = 1, right = 1
    输出：[5]

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/reverse-linked-list-ii
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre = dummy_node
        for _ in range(left - 1):
            # 将dummy赋值给pre，然后把pre 移动到反转前的结点
            pre = pre.next
        cur = pre.next  # cur就是开始反转的结点
        for _ in range(right - left):
            temp = cur.next  # 记录当前节点的下一个节点
            cur.next = temp.next  # 将当前结点指向下一个结点
            temp.next = pre.next  # 下一个结点再指向前一个结点
            pre.next = temp  #
        return dummy_node.next
