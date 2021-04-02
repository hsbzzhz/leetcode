"""
哈希表 + 双向链表

因为如果达到了链表的容量，那么就需要删除最后一个node，单向链表删除最后一个node时间复杂度是O(N)，所以使用双向链表
单向链表的话 需要单独记录操作结点的前驱结点，来实现指针的迁移，双向链表就容易很多，不需要额外记录前驱结点
"""
class DlinkedNode:
    def __init__(self):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.head = DlinkedNode()
        self.tail = DlinkedNode()
        # 先初始化两个头尾结点
        self.head.next = self.tail
        self.tail.prev = self.head
        # 如果capacity > size，就resize整个链表
        self.capacity = capacity
        self.size = 0


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 如果key存在，
        node = self.cache.get(key)

