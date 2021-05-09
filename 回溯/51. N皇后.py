"""
回溯的核心框架：

result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return

    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
"""


def is_valid(board: [], row, col):
    for i in range(row):
        """
        不能同列，和同对角线
        p.s. 同行的情况已经排除
        """
        if board[i] == col:
            # 同列
            return False
        elif abs(board[i] - col) == abs(i - row):
            return False
        return True


from typing import List


class Solution:
    def is_valid(self, board, row, col) -> bool:
        # 检查列中是否有皇后冲突
        for r in range(row):  # r:0->row-1
            if board[r][col] == "Q":
                return False
        # 判断(左上角)主对角线：判断[0:row-1,0:col-1]是否有'Q'
        mrow, mcol = row, col
        while mrow > 0 and mcol > 0:  # mrow:0->row-1,mcol:0->row-1
            mrow -= 1
            mcol -= 1
            if board[mrow][mcol] == "Q":
                return False
        # 判断(右上角)副对角线：判断[0:row-1,col+1:n]
        vrow, vcol = row, col
        while vrow > 0 and vcol < len(board) - 1:  # vrow:0->row-1,vcol:col+1->n
            vrow -= 1
            vcol += 1
            if board[vrow][vcol] == "Q":
                return False
        return True

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []

        def backtrack(board: [], row):
            if row == n:
                temp = []
                for line in board:
                    t = "".join(line)
                    temp.append(t)
                self.res.append(temp)
                return
            else:
                for col in range(len(board)):
                    if not self.is_valid(board, row, col):
                        continue
                    board[row][col] = "Q"
                    backtrack(board, row + 1)
                    board[row][col] = "."

        checkboard = [["." for _ in range(n)] for _ in range(n)]

        backtrack(checkboard, 0)
        return self.res


demo = Solution()
res = demo.solveNQueens(4)
print(res)
