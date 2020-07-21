"""
[79. 单词搜索](https://leetcode-cn.com/problems/word-search/)
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false
 

提示：

board 和 word 中只包含大写和小写英文字母。
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
通过次数71,134提交次数168,953
***
这道题主要使用回溯算法：对每一个点的值进行匹配，如果当前值匹配成功，再从当前值的上下左右开始匹配下一个点。
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board: return not word
        num = len(word)
        row, col = len(board), len(board[0])True
        used = []

        def backtrack(i, j, cnt):#回溯函数False
            if cnt == num:#匹配完成，返回True
                return True
            if i < 0 or i > row-1 or j < 0 or j > col-1: return False#越界
            if board[i][j] == word[cnt] and [i,j]not in used:#对没走过的格子进行上下左右判断
                used.append([i,j])
                if backtrack(i+1, j, cnt+1): return True
                if backtrack(i-1, j, cnt+1): return True
                if backtrack(i, j+1, cnt+1): return True
                if backtrack(i, j-1, cnt+1): return True
                used.pop()
            return False

        for i in range(row):#开始从每个位置开始查找
            for j in range(col):
                if backtrack(i, j, 0):
                    return True
        return False

