class PriorityQueue:
    """
    大顶堆
    https://github.com/labuladong/fucking-algorithm/blob/master/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E7%B3%BB%E5%88%97/%E4%BA%8C%E5%8F%89%E5%A0%86%E8%AF%A6%E8%A7%A3%E5%AE%9E%E7%8E%B0%E4%BC%98%E5%85%88%E7%BA%A7%E9%98%9F%E5%88%97.md
    """
    __queue = []
    # __size = 0
    __N = 0

    def __init__(self, size):
        self.__size = size + 1

    def peek(self):
        return self.__queue[1]

    def insert(self, key):
        self.__N +=1
        self.__queue.append(key)
        self.swim(self.__N)

    def delete_max_item(self):
        max = self.__queue[1]
        self.exchange_items(1, self.__N)
        self.__queue.pop()
        self.__N-=1
        self.sink(1)
        return max

    def swim(self, index):
        # 将元素浮至堆顶
        parent = index//2
        while index > 1 and self.__queue[parent] > self.__queue[index]:
            self.exchange_items(parent, index)
            index, parent  = parent, index

    def sink(self, index):
        # 如果沉底，就沉不下去了。如果右边节点存在，比一下大小
        while index*2 <= self.__N:
            # 假设左边比右边大，
            left = index*2
            if left < self.__N and self.__queue[left] < self.__queue[left+1]:
                left = left+1
            if self.__queue[left] < self.__queue[index]:
                break
            self.exchange_items(index, left)
            index = left

    def exchange_items(self, i, j):
        self.__queue[i], self.__queue[j] = self.__queue[j], self.__queue[i]
