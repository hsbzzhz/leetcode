"""
汽车从起点出发驶向目的地，该目的地位于出发位置东面 target英里处。

沿途有加油站，每个station[i]代表一个加油站，它位于出发位置东面station[i][0]英里处，并且有station[i][1]升汽油。

假设汽车油箱的容量是无限的，其中最初有startFuel升燃料。它每行驶 1 英里就会用掉 1 升汽油。

当汽车到达加油站时，它可能停下来加油，将所有汽油从加油站转移到汽车中。

为了到达目的地，汽车所必要的最低加油次数是多少？如果无法到达目的地，则返回 -1 。

注意：如果汽车到达加油站时剩余燃料为 0，它仍然可以在那里加油。如果汽车到达目的地时剩余燃料为 0，仍然认为它已经到达目的地。



示例 1：

输入：target = 1, startFuel = 1, stations = []
输出：0
解释：我们可以在不加油的情况下到达目的地。
示例 2：

输入：target = 100, startFuel = 1, stations = [[10,100]]
输出：-1
解释：我们无法抵达目的地，甚至无法到达第一个加油站。
示例 3：

输入：target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
输出：2
解释：
我们出发时有 10 升燃料。
我们开车来到距起点 10 英里处的加油站，消耗 10 升燃料。将汽油从 0 升加到 60 升。
然后，我们从 10 英里处的加油站开到 60 英里处的加油站（消耗 50 升燃料），
并将汽油从 10 升加到 50 升。然后我们开车抵达目的地。
我们沿途在1两个加油站停靠，所以返回 2 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-number-of-refueling-stops
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
from typing import List

# TODO 理解
class Solution:
    def minRefuelStops(
        self, target: int, startFuel: int, stations: List[List[int]]
    ) -> int:
        # 没加油都能跑到终点，那就一次油都不用加
        if startFuel >= target:
            return 0
        n = len(stations)
        # dp[][] 经过i 个加油站，加油 j 次 = 能行驶的最大距离
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        # dp 长度是 n + 1 的长度是因为把起点视为第0个加油站：起始状态处理
        # 不管经过了几个站，一次油也不加那最多跑的就是startFuel的距离
        for i in range(n + 1):
            dp[i][0] = startFuel
        """
        第站i， 有station[i][1]升汽油
        第站i， 有station[i][0]英里远
        """
        for i in range(1, n + 1):  # 0 为初始
            for j in range(1, i):
                if dp[i - 1][j] >= stations[i - 1][0]:  # 不懂
                    # 本站不加油，的前提是不加油的情况可以到油站
                    dp[i][j] = dp[i - 1][j]
                if dp[i - 1][j - 1] >= stations[i - 1][0]:
                    # 前 i-1 站加 j-1 次，本站加油
                    dp[i][j] = max(
                        dp[i][j], dp[i - 1][j - 1] + stations[i - 1][1]
                    )  # 不懂
                # or
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + stations[i - 1][1])
        for i in range(n + 1):
            if dp[n][i] >= target:
                return i
        return -1


"""
Ref.
https://leetcode-cn.com/problems/minimum-number-of-refueling-stops/solution/yi-wei-lao-xiao-bai-de-dpjie-jue-tan-suo-zhi-lu-by/
优先队列+贪心：
https://leetcode-cn.com/problems/minimum-number-of-refueling-stops/solution/tan-xin-fa-jie-jia-you-zhan-wen-ti-by-arvin-3e/
"""
