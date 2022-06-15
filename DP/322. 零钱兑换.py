class Solution(object):
    # 给定不同面额的硬币 coins 和一个总金额 amount。
    # 编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回-1。
    #
    #
    # 来源：力扣（LeetCode）
    # 链接：https: // leetcode - cn.com / problems / coin - change
    # 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    # ref.
    # https://github.com/labuladong/fucking-algorithm/blob/master/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E7%B3%BB%E5%88%97/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E8%AF%A6%E8%A7%A3%E8%BF%9B%E9%98%B6.md
    # 看方法3
    def coinChange1(self, coins, amount):
        """
        1. 原始的递归，没有解决子问题重复计算的问题
        复杂度是指数级别的 O(n^k)
        :param coins:
        :param amount:
        :return:
        """
        def dp(n):
            if n == 0:
                return 0
            if n < 0:
                return -1
            res = float("INF")
            for each in coins:
                prev = dp(n - each)
                if prev == -1:
                    continue
                res = min(res, 1 + prev)
            return res if res != float("INF") else -1

        return dp(amount)

    def coinChange2(self, coins, amount):
        """
        2. 带备忘录的递归
        k是面值的数目，n是总额
        引入了字典来存储子问题答案
        O(kn)
        :param coins:
        :param amount:
        :return:
        """
        memo = dict()

        def dp(n):
            # 查备忘录，避免重复计算
            if n in memo:
                return memo[n]
            # base case
            if n == 0:
                return 0
            if n < 0:
                return -1
            res = float("INF")  # 初始化一个正无穷
            for coin in coins:
                prev = dp(n - coin)
                if prev == -1:
                    continue  # 跳过无解的case
                res = min(res, 1 + prev)

            # 更新备忘录
            memo[n] = res if res != float("INF") else -1
            return memo[n]

        return dp(amount)

    def coinChange3(self, coins, amount):
        """
        3. dp 数组迭代法
        k是面值的数目，n是总额
        O(kn)

        ** dp[i] 表示凑到数额i需要的最少硬币数 **
        :param coins:
        :param amount:
        :return:
        """
        dp = [float("inf")] * (amount + 1)   # 注意需要 amount + 1个数
        dp[0] = 0

        for i in range(len(dp)):
            for coin in coins:
                if i - coin < 0:   # 子问题无解的情况，跳过
                    continue
                dp[i] = min(dp[i], 1 + dp[i - coin])  # 通过循环，得出凑到数额i的最少硬币个数
        return dp[amount] if dp[amount] != float("inf") else -1


demo = Solution()
print(demo.coinChange3([1, 2, 5], 11))