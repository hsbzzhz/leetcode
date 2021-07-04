class Solution(object):
    """
    编写一个函数来查找字符串数组中的最长公共前缀。

    如果不存在公共前缀，返回空字符串 ""。

     

    示例 1：

    输入：strs = ["flower","flow","flight"]
    输出："fl"
    示例 2：

    输入：strs = ["dog","racecar","car"]
    输出：""
    解释：输入不存在公共前缀。


    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/longest-common-prefix
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    def longestCommonPrefix(self, strs):
        """
        时间复杂度O(mn)
        空间为O(1)
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        ans = strs[0]
        for i in range(1, len(strs)):
            ans = self.lcp(ans, strs[i])
            if not ans:
                break
        return ans

    def lcp(self, str1, str2):
        """
        找到两个字符串的公共前缀
        :param str1:
        :param str2:
        :return:
        """
        leng, index = min(len(str1), len(str2)), 0
        while index < leng and str1[index] == str2[index]:
            index += 1

        return str1[:index]


    """
    方法二：二分查找
    O(mnlogm)
    """
    class Solution2:
        def longestCommonPrefix(self, strs: List[str]) -> str:
            def isCommonPrefix(length):
                str0, count = strs[0][:length], len(strs)
                return all(strs[i][:length] == str0 for i in range(1, count))

            if not strs:
                return ""

            minLength = min(len(s) for s in strs)
            low, high = 0, minLength
            while low < high:
                mid = (high - low + 1) // 2 + low
                if isCommonPrefix(mid):
                    low = mid
                else:
                    high = mid - 1

            return strs[0][:low]


class Solution3:
    """
    取第一个值为sample， 然后采样
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str1 = strs[0]
        for each in strs:
            while not each.startswith(str1):
                str1 = str1[:-1]

                if len(str1) == 0:
                    return ''
        return str1