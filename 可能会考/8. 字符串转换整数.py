class Solution:
    """
    time O(n), space O(1)
    """
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if len(str) < 1:
            return 0
        # 开头有符号，字母，数字的情况
        if str[0] == '-':
            flag = -1
            str = str[1:]
        elif str[0] == '+':
            flag = 1
            str = str[1:]
        elif str[0].isdigit():
            flag = 1
        else:
            return 0
        res = []
        for i in range(len(str)):
            if str[i].isdigit():
                res.append(str[i])
            else:
                break
        if len(res) > 0:
            # 防止只有一个数字的情况
            x = int(''.join(res))
        else:
            return 0
        x = x * flag
        if x < -2 ** 31:
            return -2 ** 31
        elif x > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return x


"""
正则表达式：
^[\\+\\-]?\\d+

^ 表示匹配字符串开头，我们匹配的就是 '+'  '-'  号

[] 表示匹配包含的任一字符，比如[0-9]就是匹配数字字符 0 - 9 中的一个

? 表示前面一个字符出现零次或者一次，这里用 ? 是因为 '+' 号可以省略

 \\d 表示一个数字 0 - 9 范围

+ 表示前面一个字符出现一次或者多次，\\d+ 合一起就能匹配一连串数字了
"""


class Solution2:
    def myAtoi(self, str: str) -> int:
        import re
        str = str.strip()
        matches = re.match('*([+-]?\d+)', str)  # 最重要的就是这一句了吧，正则重在搞定匹配的pattern
        if matches:
            res = int(matches.group(1))
            if res > (MAX := 2 ** 31 - 1):
                """
                海象表达式： 在变量使用的时候赋值
                """
                return MAX
            elif res < (MIN := -2 ** 31):
                return MIN
            else:
                return res
        else:
            return 0

"""作者：LotusPanda
链接：https://leetcode-cn.com/problems/string-to-integer-atoi/solution/xiong-mao-shua-ti-python3-yi-qi-xue-xi-zheng-ze-bi/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。"""