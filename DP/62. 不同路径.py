class Solution:
    """
    一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

    机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

    问总共有多少条不同的路径？


    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/unique-paths
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def uniquePaths(self, m: int, n: int) -> int:
        """
        dp: O(mn)
        :param m:
        :param n:
        :return:
        """
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

    """
    方法二：组合数学
    C   m−1
        m+n−2
    """
