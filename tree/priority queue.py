class PriorityQueue:
    """
    大顶堆
    """
    __queue = []
    # __size = 0
    __N = 0

    def __init__(self, size):
        self.__size = size + 1

    def peek(self):
        return self.__queue[1]

    def insert(self, key):
        pass

    def delete_max_item(self):
        pass

    def swim(self, index):
        # 将元素浮至堆顶
        parent = index//2
        while index > 1 and self.__queue[parent] > self.__queue[index]:
            self.exchange_items(parent, index)
            index, parent  = parent, index

    def sink(self, index):
        #
        while index*2 

    def exchange_items(self, i, j):
        self.__queue[i], self.__queue[j] = self.__queue[j], self.__queue[i]
