from typing import List

A = [3, 2, 6, -1, 4, 5, -1, 2]


# should be 17
# https://blog.csdn.net/aejt95023/article/details/101512852


def solution(A):
    fore_max = [0] * len(A)
    post_max = [0] * len(A)
    for i in range(1, len(A)):
        # 上一个数字加现在这个数字
        fore_max[i] = max(fore_max[i - 1] + A[i], 0)
    for j in range(len(A) - 2, -1, -1):
        # 从后往前赋值, 上一个数字加现在这个数字
        post_max[j] = max(fore_max[j + 1] + A[j], 0)

    print(fore_max)
    print(post_max)
    max_value = 0
    for i in range(1, len(A) - 1):
        max_value = max(max_value, fore_max[i - 1] + post_max[i + 1])
    return max_value
