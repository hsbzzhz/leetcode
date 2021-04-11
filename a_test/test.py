from typing import List


def dfs(graph: [], start):
    stack = list()
    # initial it
    stack.append(start)
    visited = set()
    visited.add(start)
    while stack:
        top_item = stack.pop()
        vertex = graph[top_item]
        for each in vertex:
            if each not in visited:
                stack.append(each)
                visited.add(each)
        print(top_item)


# graph = {
#     "A": ["B", "C"],
#     "B": ["A", "C", "D"],
#     "C": ["A", "B", "D", "E"],
#     "D": ["B", "C", "E", "F"],
#     "E": ["C", "D"],
#     "F": ["D"]
# }

    def singleNumber(nums):
        if len(nums) == 1:  # 如果数组长度为1，则直接返回即可
            return nums[0]
        nums.sort()  # 对数组进行排序，使其相同元素靠在一起
        for i in range(1, len(nums), 2):  # 循环数组，验证前后是否相同，由于原始出现两次，因此可跳跃判断
            if nums[i - 1] != nums[i]:
                return nums[i - 1]
            if (i + 2) == len(nums):  # 判断单一元素在排序后数组的最后面
                return nums[-1]


# 作者：3
# wMnEBDLkw
# 链接：https: // leetcode - cn.com / problems / single - number / solution / python3 - 136
# zhi - chu - xian - yi - ci - de - shu - zi - duo - chong - /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

nums = [4,1,2,1,2]
print(singleNumber(nums))