"""
给定一个字符串，请你找出其中不含有重复字符的最长子串的长度。


示例:

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
解释: 因为无重复字符的最长子串是"wke"，所以其长度为 3。
  请注意，你的答案必须是 子串 的长度，"pwke"是一个子序列，不是子串。
示例 4:

输入: s = ""
输出: 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# 滑动窗口模板
def _sliding_window_template(self, s, t):  # s for string, t for target
    left, right = 0, 0
    while right < len(s):
        "window".add(s[right])
        right += 1
        while t in "window":
            # 如果窗口包含了所有目标元素，可以缩小范围了
            "window".pop(s[left])
            left += 1


class Solution:
    """
    滑动窗口
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        ~看这个
        思路：
        1， 所有元素必须遍历一次
        2. 什么时候重新计算count，也就是重新计算i的位置
        时间复杂度：O(n)
        空间复杂度： O(n)有个dict
        :param s:
        :return:
        """
        left, right = 0, 0
        visited = {}  # {'b':3}
        count = 0
        while right < len(s):
            char_r = s[right]
            if char_r not in visited:
                visited[char_r] = 1
            else:
                visited[char_r] += 1
            right += 1
            # 开始滑动窗口
            while visited[char_r] > 1:
                char_l = s[left]
                visited[char_l] -= 1
                left += 1
            count = max(count, right - left)

        return count

    def lengthOfLongestSubstring2(self, s):
        """
        不记录字符串位置，记录count
        :type s: str
        :rtype: int
        """
        visited = ""
        count = 0
        for char in s:
            if char not in visited:
                visited += char
                count = max(count, len(visited))
            else:
                visited = visited[visited.index(char) + 1 :] + char
        return count

    def lengthOfLongestSubstring3(self, s: str) -> int:
        """
        想不清楚，不应该在else里进行统计，
        :param s:
        :return:
        """
        if len(s) < 1:
            return 0
        i = j = 0
        count = 0
        visited = set()
        while j < len(s):
            if s[j] not in visited:
                visited.add(s[j])
                # count = max(count, j - i)
            else:
                count = max(count, j - i)
                i += 1
                # visited.remove(s[j])
            j += 1

        return count


target = "pwwkew"
s = Solution()
res = s.lengthOfLongestSubstring(target)
print(res)
