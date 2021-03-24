"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数

解体：
1. 建立数组
2. 确定状态转移方程 f(n) = f(n-1)+f(n-2)
3. 确定边界
========================================
其实是一个斐波那契数列
n  :   0 1 2 3 4 5 ... 多少级楼梯
res:   1 1 2 3 5 8 ... 有多少种走法

https://leetcode-cn.com/problems/climbing-stairs/

时间复杂度：O(n)
空间复杂度：O(n)
"""


def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    dp = [1, 1]
    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[n]


# 递归方法二
class Solution(object):
    def climbStairs2(self, n):
        if n == 0 or n == 1:
            return 1
        return self.climbStairs2(n - 1) + self.climbStairs2(n - 2)


"""
fib 参考
"""


def fib(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


print(climbStairs(10))
sol = Solution()
print(sol.climbStairs2(10))

print(fib(10))
