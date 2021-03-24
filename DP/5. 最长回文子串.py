"""
示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"
示例 3：

输入：s = "a"
输出："a"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution(object):
    """
    中心扩散法  O(n^2)

    奇数回文串的“中心”是一个具体的字符，例如：回文串 "aba" 的中心是字符 "b"；
    偶数回文串的“中心”是位于中间的两个字符的“空隙”，例如：回文串串 "abba" 的中心是两个 "b" 中间的那个“空隙”。
    """

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        if size < 2:
            return s
        max_sub = ""
        for i in range(size):
            # 存在奇偶情况，都需要算出来再进行长度比较
            odd, odd_len = self.__center_spread(s, i, i)   # 情况1，单独一个字母作为中心
            even, even_len = self.__center_spread(s, i, i + 1)   # 情况2， 两个字母作为中心

            temp_max_sub = odd if odd_len > even_len else even
            max_sub = temp_max_sub if len(temp_max_sub) > len(max_sub) else max_sub
        return max_sub

    def __center_spread(self, s, left, right):
        """
        每个字符向四周扩散搜索，
        :param s:
        :param left:
        :param right:
        :return:
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right], right - left - 1


o = Solution()
ans = o.longestPalindrome("babad")
print(ans)

"""
方法二：动态规划
"""

def longestPalindrome(self, s: str) -> str:
    """
    时间空间复杂度都是O(n^2)
    :param self:
    :param s:
    :return:
    """
    size = len(s)
    if size < 2:
        return s

    dp = [[False for _ in range(size)] for _ in range(size)]

    max_len = 1
    start = 0

    for i in range(size):
        dp[i][i] = True

    for j in range(1, size):
        for i in range(0, j):
            if s[i] == s[j]:
                if j - i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = False

            if dp[i][j]:
                cur_len = j - i + 1
                if cur_len > max_len:
                    max_len = cur_len
                    start = i
    return s[start:start + max_len]



# res[i] += c： 把每个字符 c 填入对应行 s_is
# i += flag： 更新当前字符 c 对应的行索引；
# flag = - flag： 在达到 ZZ 字形转折点时，执行反向。
