"""
给定一个数组 prices ，它的第i 个元素prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0

示例 1：

输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
"""
from typing import List


class Stock(object):
    def maxProfit(self, prices):
        """
        121. 买卖股票的最佳时机
        单次买卖，获得的最大利润

        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        minPrice, profit = prices[0], 0
        for index in range(len(prices)):
            minPrice = min(minPrice, prices[index])
            profit = max(profit, prices[index] - minPrice)
        return profit

    def maxProfit2(self, prices: List[int]) -> int:
        """
        O(n) O(1)
        122. 买卖股票的最佳时机 II
        允许多次买卖
        :param self:
        :param prices:
        :return:
        """
        max_profit = 0
        for i in range(1, len(prices)):
            max_profit += max(0, prices[i] - prices[i - 1])

        return max_profit

    def maxProfit3(self, prices: List[int]) -> int:
        """
        O(n) O(n)
        :param self:
        :param prices:
        :return:
        """
        dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[len(prices) - 1][0]

    """
    
    dp[i][k][0]  第i天，最多进行了k次交易，手里没有持股
    dp[i][k][1]  第i天，最多进行了k次交易，手里持股
    
    dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                  max(   选择 rest ,       选择 sell         )

    dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
                  max(   选择 rest ,       选择 buy     )
    
    ref.
    https://labuladong.gitbook.io/algo/bi-du-wen-zhang/tuan-mie-gu-piao-wen-ti
    
    """

    def maxProfit_k_inf(self, prices):
        n = len(prices)
        dp_i_0, dp_i_1 = 0, float("-inf")
        for i in range(n):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, temp - prices[i])
        return dp_i_0

    def maxProfit5(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if k > n // 2:
            # return self.maxProfit_k_inf(prices)
            k = n // 2
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n)]
        # base case
        for i in range(1, k + 1):
            dp[0][i][0] = 0
            dp[0][i][1] = -prices[0]
        for i in range(1, n):
            for j in range(1, k + 1):
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])

        return dp[n - 1][k][0]

    def maxProfit6(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if k > n / 2:
            return self.maxProfit_k_inf(prices)

        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n)]

        # for i in range(k+1):
        #     dp[0][i][0] = 0
        #     dp[0][i][-1] = float('-inf')
        for i in range(n):
            # j = k
            for j in range(1, k + 1):
                # k +1是因为k从1开始，循环要到k
                if i == 0:  # base case
                    dp[i][j][0] = 0
                    dp[i][j][1] = float("-inf")
                    continue
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
                # j -= 1
        print(dp)
        return dp[n - 1][k][0]


demo = Stock()
res = demo.maxProfit5(2, [1, 2, 4, 2, 5, 7, 2, 4, 9, 0])  # 13
# res = demo.maxProfit6(1, [1,2])
print(res)
