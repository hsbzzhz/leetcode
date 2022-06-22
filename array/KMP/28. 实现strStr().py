class Solution:
    """
    实现strStr()函数。
    7.20 日 微软电话面试题
    给你两个字符串haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回 -1 。

    说明：

    当needle是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

    对于本题而言，当needle是空字符串时我们应当返回 0 。这与 C 语言的strstr()以及 Java 的indexOf()定义相符。


    示例 1：

    输入：haystack = "hello", needle = "ll"
    输出：2
    示例 2：

    输入：haystack = "aaaaa", needle = "bba"
    输出：-1

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/implement-strstr
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    #  这答案有问题，@todo improve
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
                if j == len(needle) - 1:
                    return i
        return -1
