"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
 
示例 1：
输入：s = "()"
输出：true
"""


class Solution:
    """
    思路：
    1。把左括号入栈
    2。如果是右括号，pop出栈顶左括号（所以只入栈了一半的字符串）
    3。最后如果为空栈，即匹配成功
    """

    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        pairs = {")": "(", "]": "[", "}": "{"}
        stack = list()
        for each in s:
            if each in pairs:
                if not stack or stack[-1] != pairs[each]:
                    return False
                stack.pop()  # 默认最后一个元素
            else:
                stack.append(each)
        return not stack
