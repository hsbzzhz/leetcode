
class Solution(object):
    # ref.
    # https://github.com/labuladong/fucking-algorithm/blob/master/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E7%B3%BB%E5%88%97/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E8%AF%A6%E8%A7%A3%E8%BF%9B%E9%98%B6.md
    def coinChange1(self, coins, amount):
        """
        原始的递归，没有解决子问题重复计算的问题
        复杂度是指数级别的 O(n^k)
        :param coins:
        :param amount:
        :return:
        """
        def dp(n):
            if n == 0: return 0
            if n < 0: return -1
            res = float('INF')
            for each in coins:
                prev = dp(n - each)
                if prev == -1: continue
                res = min(res, 1 + prev)
            return res if res != float('INF') else -1

        return dp(amount)

    def coinChange2(self, coins, amount):
        """
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
            if n in memo: return memo[n]
            # base case
            if n == 0: return 0
            if n < 0: return -1
            res = float('INF')  # 初始化一个正无穷
            for coin in coins:
                prev = dp(n - coin)
                if prev == -1: continue  # 跳过无解的case
                res = min(res, 1+prev)

            # 更新备忘录
            memo[n] = res if res != float('INF') else -1
            return memo[n]
        return dp(amount)

    def coinChange3(self, coins, amount):
        """
        k是面值的数目，n是总额
        O(kn)
        dp 中存储的是额度为i 的 最小方法个数
        :param coins:
        :param amount:
        :return:
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

