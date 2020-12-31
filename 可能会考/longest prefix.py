class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        ans = strs[0]
        for i in range(1, len(strs)):
            ans = self.lcp(ans, strs[i])
            # if not ans:
            #     break
        return ans

    def lcp(self, str1, str2):
        leng, index = min(len(str1), len(str2)), 0
        while index < leng and str1[index] == str2[index]:
            index += 1

        return str1[:index]