"""
37. 解数独
编写一个程序，通过已填充的空格来解决数独问题。

一个数独的解法需遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。

一个数独。
答案被标成红色。

Note:

给定的数独序列只包含数字 1-9 和字符 '.' 。
你可以假设给定的数独只有唯一解。
给定数独永远是 9x9 形式的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sudoku-solver
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        out = []
        def is_valid(row, col, num, board):
            for i in range(9):
                if i != row and  str(num) == board[i][col]:
                    return False
                if i != col and  str(num) == board[row][i]:
                    return False

            i_index = row // 3 * 3
            j_index = col // 3 * 3

            for i in range(3):
                for j in range(3):
                    if i+i_index != row and j+j_index != col and \
                        str(num) == board[i+i_index][j+j_index]:
                        return False
            return True

        def backtrack(board, row, col):
            if row == 9:
                out.append(board.copy())
                return True
            for k in range(1,10):
                while board[row][col] != '.':
                    if col < 8:
                        col += 1
                    elif col == 8:
                        row += 1
                        col = 0
                        if row == 9:
                            out.append(board)
                            return True
                if is_valid(row,col,k,board):
                    board[row][col] = str(k)
                    if backtrack(board, row if (col<8) else row + 1, (col + 1)%9):
                        return True
                    board[row][col] = '.'
            return False
        backtrack(board, 0 , 0)
        return out[0]

if __name__ == "__main__":
    s = Solution()
    # print(s.solveSudoku([
    # ["5","3",".",".","7",".",".",".","."],
    # ["6",".",".","1","9","5",".",".","."],
    # [".","9","8",".",".",".",".","6","."],
    # ["8",".",".",".","6",".",".",".","3"],
    # ["4",".",".","8",".","3",".",".","1"],
    # ["7",".",".",".","2",".",".",".","6"],
    # [".","6",".",".",".",".","2","8","."],
    # [".",".",".","4","1","9",".",".","5"],
    # [".",".",".",".","8",".",".","7","9"]]))
    print(s.solveSudoku([
        [".",".","9","7","4","8",".",".","."],
        ["7",".",".",".",".",".",".",".","."],
        [".","2",".","1",".","9",".",".","."],
        [".",".","7",".",".",".","2","4","."],
        [".","6","4",".","1",".","5","9","."],
        [".","9","8",".",".",".","3",".","."],
        [".",".",".","8",".","3",".","2","."],
        [".",".",".",".",".",".",".",".","6"],
        [".",".",".","2","7","5","9",".","."]]))


    
