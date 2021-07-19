class Solution:
    """
    hard 难度
    滑动窗口：先通过移动右边指针确定窗口能覆盖所有target
    然后挪动左指针缩小覆盖范围，
    记录每次达到条件的最小窗口范围
    https://leetcode-cn.com/problems/minimum-window-substring/
    """

    def check(self, hashmap: dict) -> bool:
        """
        如果遍历到了字符就把该val -1， 如果字典中所有val都小于1，那么说明窗口中已包含所有target中的元素
        :param hashmap:
        :return:
        """
        for v in hashmap.values():
            if v > 0:
                return False
        return True

    def minWindow0(self, s: str, t: str) -> str:
        # 方法2，自写, 避免使用记录字符的窗口
        target = {}  # 初始化target字典
        for each in t:
            if each in target:
                target[each] += 1
            else:
                target[each] = 1
        # 设置窗口左右边界
        left, right = 0, 0
        res, is_run = s, 0
        while right < len(s):
            # 开始遍历整个 原始字符串
            char_r = s[right]
            if char_r in target:  # 维护整个target
                target[char_r] -= 1
            right += 1

            while self.check(target):  # 如果是正确答案的情况下，就可以开始优化
                length = right - left
                if length < len(res):
                    res = "".join(s[left:right])  # 如果当前结果比res好，即更新当前答案
                # 优化开始
                char_l = s[left]
                if char_l in target:
                    target[char_l] += 1
                left += 1
                is_run = 1

        if is_run:
            return res
        return ""

    def minWindow(self, s: str, t: str) -> str:
        # 把 t 种的字符全部放入hashmap中，出现1次就+1
        target = {}
        for each in t:
            # 为了避免同一个字符出现多次，例如 'aa' ，则需-1值, 而不是直接赋值0
            if each in target:
                target[each] += 1
            else:
                target[each] = 1
        # 设置窗口左右边界
        left, right = 0, 0
        # 记录字符开始位置和长度
        str_start, win_len = 0, len(s) + 1
        while right < len(s):
            # 如果没有把t中所有字符包括在窗口中，那么就移动右指针
            char_r = s[right]
            if char_r in target:
                target[char_r] -= 1
            right += 1

            while self.check(target):
                # 找到答案，进行优化
                # 缩小窗口， 左指针向右移动
                if right - left < win_len:
                    win_len, str_start = right - left, left
                char_l = s[left]
                if char_l in target:
                    target[char_l] += 1
                left += 1

        if win_len != len(s) + 1:
            return "".join(s[str_start : str_start + win_len])
        return ""


demo = Solution()
s = "ADOBECODEBANC"
t = "ABC"
res = demo.minWindow(s, t)
print(res)
