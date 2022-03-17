from typing import List

"""
n 位格雷码序列 是一个由 2n 个整数组成的序列，其中：
    1. 每个整数都在范围 [0, 2n - 1] 内（含 0 和 2n - 1）
    2. 第一个整数是 0
    3. 一个整数在序列中出现 不超过一次
    4. 每对 相邻 整数的二进制表示 恰好一位不同 ，且
    5. 第一个 和 最后一个 整数的二进制表示 恰好一位不同

求： 给你一个整数 n ，返回任一有效的 n 位格雷码序列

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/gray-code
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

例子：
输入：n = 2
输出：[0,1,3,2]
解释：
[0,1,3,2] 的二进制表示是 [00,01,11,10] 。
- 00 和 01 有一位不同
- 01 和 11 有一位不同
- 11 和 10 有一位不同
- 10 和 00 有一位不同
[0,2,3,1] 也是一个有效的格雷码序列，其二进制表示是 [00,10,11,01] 。
- 00 和 10 有一位不同
- 10 和 11 有一位不同
- 11 和 01 有一位不同
- 01 和 00 有一位不同


推导：
往前补0，<<
0： 0
1： 00  01
    0   1
2： 00  01   11  10    
    0   1    3   2     
3： 000  001  011  010  110 111  101  100 
    0    1    3    2    6   7    5    4
    
    
具体实现，to be continue
"""


class solution:
    """
    非 typical 回溯，太tricky 搞死人
    """

    def grayCode(self, n: int) -> List[int]:
        nums = [0, 1]
        output = []

        def dfs(arr, combin, target, idx):
            if len(combin) == target:
                output.append(int("".join([str(g) for g in combin[:]]), 2))
                return
            if idx == 0:
                for i in range(len(arr)):
                    combin.append(arr[i])
                    dfs(arr, combin, target, i)
                    combin.pop()
            if idx == 1:
                for i in range(len(arr)):
                    combin.append(arr[::-1][i])
                    dfs(arr, combin, target, i)
                    combin.pop()

        dfs(nums, [], n, 0)
        return output
