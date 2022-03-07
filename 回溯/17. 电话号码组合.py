from typing import List

"""
回溯
# 17.

O(3^M × 4^N)
M 是对应三个字母的数字个数，N 是对应四个字母的数字个数

给定一个仅包含数字2-9的字符串，返回所有它能表示的字母组合。答案可以按任意顺序返回。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

9宫格键盘-给出输入数字，得出输出的可能结果

示例 1：

输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def dfs(track: str, index):
            if len(track) == len(digits):
                res.append(track)  # "ad"
                return  # 必须加这一步，否则指针溢出
            for word in phone[digits[index]]:  # ["a", "b", "c"]
                track += word  # "ad"
                dfs(track, index + 1)  # ["d", "e", "f"]
                track = track[:-1]  # 移除尾部字符，还原

        res = []
        dfs("", 0)
        return res
