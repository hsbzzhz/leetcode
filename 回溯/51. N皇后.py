from typing import List


class Solution:
    """
    n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

    给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。

    每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

    示例 1：
    输入：n = 4
    输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
    解释：如上图所示，4 皇后问题存在两个不同的解法。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/n-queens
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

    """
    def is_valid(self, board, row, col) -> bool:   # 减枝
        # 检查列中是否有皇后冲突
        for i in range(row):  # r:0->row-1
            if board[i][col] == "Q":
                return False
        # 判断(左上角)主对角线：判断[0:row-1,0:col-1]是否有'Q'
        i, j = row, col
        while i > 0 and j > 0:  # mrow:0->row-1,  mcol:0->row-1
            i -= 1
            j -= 1
            if board[i][j] == "Q":
                return False
        # 判断(右上角)副对角线：判断 [0:row-1,col+1:n]
        i, j = row, col
        while i > 0 and j < len(board) - 1:  # vrow:0->row-1,vcol:col+1->n
            i -= 1
            j += 1
            if board[i][j] == "Q":
                return False
        return True

    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        * 路径：board 中小于 row 的那些行都已经成功放置了皇后
        * 选择列表：第 row 行的所有列都是放置皇后的选择
        * 结束条件：row 超过 board 的最后一行
        :param n:
        :return:
        """
        def backtrack(board: [], row):
            if row == n:
                temp = []
                for line in board:
                    t = "".join(line)
                    temp.append(t)
                self.res.append(temp)
                return

            for col in range(len(board)):
                if not self.is_valid(board, row, col):
                    continue
                # 选择，将棋盘位置改为 Q
                board[row][col] = "Q"
                # 进入下一行决策
                backtrack(board, row + 1)
                # 还原，撤销选择
                board[row][col] = "."

        # 初始化棋盘
        checkboard = [["." for _ in range(n)] for _ in range(n)]
        self.res = []
        backtrack(checkboard, 0)  # 从 0 开始，直至到整个长度
        return self.res


demo = Solution()
res = demo.solveNQueens(4)
print(res)
