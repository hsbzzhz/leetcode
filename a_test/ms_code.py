"""
AA00 = 10
AB00 = (AA00 + AA01) *15
AA01 = 20 + AB00

求公式内的循环调用
union find？
"""


def str_match_0(s, target):
    for i in range(len(s) - len(target) + 1):
        for j in range(len(target)):
            if s[i + j] != target[j]:
                break
            if j == len(target) - 1:
                return i
    return -1


s = "a"
target = "a"
index = str_match_0(s, target)
print(index)
