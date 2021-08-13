"""
给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。

子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。

 

示例 1：

输入：s = "bbbab"
输出：4
解释：一个可能的最长回文子序列为 "bbbb" 。
示例 2：

输入：s = "cbbd"
输出：2
解释：一个可能的最长回文子序列为 "bb" 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        for r in range(len(s) - 1, -1, -1):  # 这个遍历顺序很迷
            for l in range(r + 1, len(s)):
                if s[l] == s[r]:
                    dp[r][l] = dp[r + 1][l - 1] + 2    # 如果内层相等，就左右扩大一个
                else:
                    dp[r][l] = max(dp[r+1][l], dp[r][l-1])    # ??? 如果不相等，就左挪一位和右挪一位做比较
        print(dp)  # 可以看一下返回了什么
        return dp[0][len(s) - 1]



longp = Solution()
longp.longestPalindromeSubseq("bbbab")

# ref. https://github.com/labuladong/fucking-algorithm/blob/master/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E7%B3%BB%E5%88%97/%E5%AD%90%E5%BA%8F%E5%88%97%E9%97%AE%E9%A2%98%E6%A8%A1%E6%9D%BF.md