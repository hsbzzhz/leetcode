"""
哈希表 + 双向链表

因为如果达到了链表的容量，那么就需要删除最后一个node，单向链表删除最后一个node时间复杂度是O(N)，所以使用双向链表
单向链表的话 需要单独记录操作结点的前驱结点，来实现指针的迁移，双向链表就容易很多，不需要额外记录前驱结点





1。 为什么要是双向链表，单链表行不行
因为我们需要删除操作。删除一个节点不光要得到该节点本身的指针，也需要操作其前驱节点的指针，而双向链表才能支持直接查找前驱，保证操作的时间复杂度 O(1)
2。 既然哈希表中已经存了 key，为什么链表中还要存键值对呢，只存值不就行了
当缓存容量已满，我们不仅仅要删除最后一个 Node 节点，还要把 map 中映射到该节点的 key 同时删除，而这个 key 只能由 Node 得到。
如果 Node 结构中只存储 val，那么我们就无法得知 key 是什么，就无法删除 map 中的键，造成错误


作者：labuladong
链接：https://leetcode-cn.com/problems/lru-cache/solution/lru-ce-lue-xiang-jie-he-shi-xian-by-labuladong/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class DlinkedNode:
    """
    时间复杂度：对于 put 和 get 都是 O(1)。

    空间复杂度：O(capacity)，因为哈希表和双向链表最多存储 capacity+1 个元素。


    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/lru-cache/solution/lruhuan-cun-ji-zhi-by-leetcode-solution/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.hashmap = dict()
        # 新建头尾结点
        self.head = DlinkedNode()
        self.tail = DlinkedNode()
        # 先初始化两个头尾结点, 使得头尾互相指
        self.head.next = self.tail
        self.tail.prev = self.head
        # capacity是指最大容量，size是说已有大小
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        # 如果key存在，通过hash表定位，然后再移到头部
        node = self.hashmap[key]
        self.move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.hashmap:
            # 如果 key 不存在，创建一个新的结点
            node = DlinkedNode(key, value)
            # 添加进 hash 表
            self.hashmap[key] = node
            # 添加进双向链表头部
            self.add_node_to_head(node)
            self.size += 1
            if self.size > self.capacity:
                # 如果超出容量，删除尾部结点
                removed = self.remove_tail()
                # 删除哈希表中对应的项
                self.hashmap.pop(removed.key)
                self.size -= 1
        else:
            # 如果key存在， 修改value，再把该结点移动到头部
            node = self.hashmap[key]
            node.value = value
            self.move_to_head(node)

    # 1
    def add_node_to_head(self, node: DlinkedNode):
        """
        只考虑头节点的关系
        在head节点后插入node

        :param node:
        :return:
        """
        # 建立 node 的前后关系
        node.prev = self.head
        node.next = self.head.next
        # 更新 node 前后节点的关系 （head.next的前节点 和 head的后节点）
        self.head.next.prev = node
        self.head.next = node

    # 2
    def remove_node(self, node):
        # 更新node的前后节点
        node.prev.next = node.next
        node.next.prev = node.prev

    # 3
    def move_to_head(self, node):
        self.remove_node(node)
        self.add_node_to_head(node)

    def remove_tail(self):
        # 删除尾部结点，也就是删除tail的前一个结点
        node = self.tail.prev
        self.remove_node(node)
        return node
