import List


class SegmentTree:
    """
    线段树
    https://www.bilibili.com/video/BV1cb411t7AM?t=386
    """

    def build_tree(self, arr: list, tree: list, node, start, end):
        """

        :param arr:
        :param tree:
        :param node: 树的根节点
        :param start: arr的start
        :param end: arr的end
        :return:
        """
        if start == end:
            tree[node] = arr[start]  # 递归出口，到了树的底部
        else:
            mid = (start + end) // 2  # 根据范围求得根节点index
            left_node = node * 2 + 1
            right_node = node * 2 + 2
            self.build_tree(arr, tree, left_node, start, mid)
            self.build_tree(arr, tree, right_node, mid + 1, end)
            tree[node] = tree[left_node] + tree[right_node]

    def update_tree(self, arr: list, tree: list, node, start, end, idx, val):
        """
        更改某个节点的值
        :param arr:
        :param tree:
        :param node:
        :param start: 搜索范围
        :param end: 搜索范围
        :param idx:
        :param val:
        :return:
        """
        if start == end:
            arr[idx] = val
            tree[node] = val
        else:
            mid = (start + end) // 2
            left_node = node * 2 + 1
            right_node = node * 2 + 2
            if start <= idx <= mid:
                self.update_tree(arr, tree, left_node, start, mid, idx, val)
            elif idx > mid:
                self.update_tree(arr, tree, right_node, mid + 1, end, idx, val)
            tree[node] = tree[left_node] + tree[right_node]

    def query_tree(self, arr: list, tree: list, node, start, end, range_l, range_r):
        if range_r < start or range_l > end:
            return 0
        elif range_l <= start and end <= range_r:
            return tree[node]
        elif start == end:
            return tree[node]
        else:
            mid = (start + end) // 2
            left_node = 2 * node + 1
            right_node = 2 * node + 2
            sum_left = self.query_tree(
                arr, tree, left_node, start, mid, range_l, range_r
            )
            sum_right = self.query_tree(
                arr, tree, right_node, mid + 1, end, range_l, range_r
            )

            return sum_left + sum_right
