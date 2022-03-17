from typing import List


class Solution:
    """
    dfs
    数字 n代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且有效的 括号组合

    示例 1：

    输入：n = 3
    输出：["((()))","(()())","(())()","()(())","()()()"]

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/generate-parentheses
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(track, left, right):
            """

            :param track: 当前路径
            :param left: 左括号已匹配的个数
            :param right: 右括号已匹配的个数
            :return:
            """
            if left == n and right == n:  # 在左右括号个数都==n的情况上，代表当前路径是一个答案
                ans.append("".join(track))
                return
            # 先放左边的括号，再补右边的括号
            # 这里不用while
            if left < n:  # 先补充左边括号
                track.append("(")
                backtrack(track, left + 1, right)  # 下一个计算
                track.pop()
            if right < left:  # 补充右边括号
                track.append(")")
                backtrack(track, left, right + 1)
                track.pop()

        backtrack([], 0, 0)
        return ans
