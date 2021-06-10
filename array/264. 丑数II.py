class Solution(object):
    """
    给你一个整数 n ，请你找出并返回第 n 个 丑数 。

    丑数 就是只包含质因数 2、3 和/或 5 的正整数。

     

    示例 1：

    输入：n = 10
    输出：12
    解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/ugly-number-ii
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    def nthUglyNumber(self, n):
        """
        因此，如果我们所有丑数的有序序列为 a1,a2,a3,...,an 的话，序列中的每一个数都必然能够被以下三个序列（中的至少一个）覆盖：
        由丑数 * 22 所得的有序序列：1 * 2、2 * 2、3 * 2、4 * 2、5 * 2、6 * 2、8 * 2 ...
        由丑数 * 33 所得的有序序列：1 * 3、2 * 3、3 * 3、4 * 3、5 * 3、6 * 3、8 * 3 ...
        由丑数 * 55 所得的有序序列：1 * 5、2 * 5、3 * 5、4 * 5、5 * 5、6 * 5、8 * 5 ...

        :param n:
        :return:
        """
        dp = [0, 1]  #
        i2, i3, i5 = 1, 1, 1
        index = 2
        while index <= n:
            a, b, c = dp[i2]*2, dp[i3]*3, dp[i5]*5
            temp = min(a, b, c)
            if temp == a: i2 += 1
            if temp == b: i3 += 1
            if temp == c: i5 += 1
            dp.append(temp)
            index += 1
        return dp[-1]

res = Solution().nthUglyNumber(10)
print(res)

