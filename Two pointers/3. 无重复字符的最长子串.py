"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

 

示例 1:

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
示例 4:

输入: s = ""
输出: 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution:
    """
    滑动窗口
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        时间复杂度：O(n)
        空间~~~： O(n)有个dict
        :param s:
        :return:
        """
        if len(s) < 1:
            return 0
        i = j = 0
        visited = {}
        count = 0
        while j < len(s):
            if i != j and s[j] in visited:
                # abba 这种情况，确保不能往后退
                i = max(visited[s[j]] + 1, i)

                # visited.update({s[j]: j})
            count = max(j - i + 1, count)
            visited.update({s[j]: j})  # 更新最新元素的位置
            j += 1

        return count


target = "pwwkew"
s = Solution()
res = s.lengthOfLongestSubstring(target)
print(res)

# def lengthOfLongestSubstring2(self, s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     temp = ''
#     length = 0
#     for i in s:
#         if i not in temp:
#             temp += i
#             length = max(length, len(temp))
#         else:
#             temp = temp[temp.index(i) + 1:] + i
#             # temp += i
#             # temp = temp[temp.index(i) + 1:]
#     return length
