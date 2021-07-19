class SortDemo1(object):
    def SortDemo(self, arr):
        """
        O(nlogn)
        先分后治
        最坏情况也能保证 O(nlogn)
        mergeSort是分, 把列表分开
        :param arr:
        :return:
        """
        if len(arr) < 2:
            return arr
        middle = len(arr) // 2
        left, right = arr[:middle], arr[middle:]
        # SortDemo 是分，merge 是治，所以是先分后治
        return self.merge(self.SortDemo(left), self.SortDemo(right))

    def merge(self, left, right):
        """
        左右两边排好了序，把左右两边合并
        :param left:
        :param right:
        :return: 把左右两个有序list合并成一个, 直至左右list中仅存在一个元素
        """
        result = []
        # 如果两个子列表都有
        while left and right:
            # 把小的元素弹出
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        # 单个list存在元素的情况
        while left:
            result.append(left.pop(0))
        while right:
            result.append(right.pop(0))
        return result


if __name__ == "__main__":
    srr = [13, 4, 5, 12, 15, 21, 16, 23, 89]
    demo = SortDemo1()
    res = demo.SortDemo(srr)
    print(res)

#########################################################################################


class Solution:
    """
    148. 排序链表
    给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
    https://leetcode-cn.com/problems/sort-list/
    """

    def sortList(self, head: ListNode) -> ListNode:
        def sortFunc(head: ListNode, tail: ListNode) -> ListNode:
            if not head:
                return head
            if head.next == tail:
                head.next = None
                return head
            slow = fast = head
            while fast != tail and fast.next != tail:
                slow = slow.next
                fast = fast.next.next
            mid = slow
            return merge(sortFunc(head, mid), sortFunc(mid, tail))

        def merge(head1: ListNode, head2: ListNode) -> ListNode:
            dummyHead = ListNode(0)
            temp, temp1, temp2 = dummyHead, head1, head2
            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            if temp1:
                temp.next = temp1
            elif temp2:
                temp.next = temp2
            return dummyHead.next

        return sortFunc(head, None)


# 作者：LeetCode - Solution
# 链接：https: // leetcode - cn.com / problems / sort - list / solution / pai - xu - lian - biao - by - leetcode - solution /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# while (fast != tail) {
#         slow = slow.next;
#         fast = fast.next;
#         if (fast != tail) {
#             fast = fast.next;
#         }
