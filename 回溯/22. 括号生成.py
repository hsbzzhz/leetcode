from typing import List

class Solution:
    """
    并不是回溯
    dfs
    数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合

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
            if left == n and right == n:  # 所有括号都上齐的情况
                ans.append(''.join(track))
                return
            # 先放左边的括号，再补右边的括号
            if left < n:  # 左括号没有，就append
                track.append('(')
                # left += 1  这样写就错了
                backtrack(track, left + 1, right)
                track.pop()
            if right < left:  # 左括号有了，append右括号
                track.append(')')
                # right += 1  这样写就错了
                backtrack(track, left, right + 1)
                track.pop()

        backtrack([], 0, 0)
        return ans