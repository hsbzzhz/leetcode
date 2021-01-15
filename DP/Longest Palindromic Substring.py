class Solution(object):
    # 中心扩散法  O(n^2)
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
            odd, odd_len = self.__center_spread(s, i, i)
            even, even_len = self.__center_spread(s, i, i + 1)

            temp_max_sub = odd if odd_len > even_len else even
            max_sub = temp_max_sub if len(temp_max_sub) > len(max_sub) else max_sub
        return max_sub

    def __center_spread(self, s, left, right):
        """
        :param s:
        :param left:
        :param right:
        :return:
        """
        # i = left
        # j = right
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right], right - left - 1


o = Solution()
ans = o.longestPalindrome("babad")
print(ans)

# res[i] += c： 把每个字符 c 填入对应行 s_is
# i += flag： 更新当前字符 c 对应的行索引；
# flag = - flag： 在达到 ZZ 字形转折点时，执行反向。
