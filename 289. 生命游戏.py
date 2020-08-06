"""
[289. 生命游戏](https://leetcode-cn.com/problems/game-of-life/)
根据 289. 生命游戏百度百科 ，生命游戏，简称为生命，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。

给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态：1 即为活细胞（live），或 0 即为死细胞（dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：
ｌｅｅｔｃｏｄｅ
如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
根据当前状态，写一个函数来计算面板上所有细胞的下一个（一次更新后的）状态。下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。

 

示例：

输入： 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
输出：
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
 

进阶：

你可以使用原地算法解决本题吗？请注意，面板上所有格子需要同时被更新：你不能先更新某些格子，然后使用它们的更新后的值再更新其他格子。
本题中，我们使用二维数组来表示面板。原则上，面板是无限的，但当活细胞侵占了面板边界时会造成问题。你将如何解决这些问题？
***
笨方法：创建一个临时数组，然后根据面板的值进行赋值，更新完一次之后，把临时矩阵中的值赋值回来给面板矩阵。
"""
```python
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        1：death
        2,3: live
        4,5,6,7,8 death
        3: revive
        """
        m, n = len(board), len(board[0])
        temp = [[0]*n for _ in range(m)]#建立临时矩阵
        DEAD = 0
        LIVE = 1
        def search(i, j):#创建搜索函数，确定当前值的下一个状态
            cnt = 0
            for x, y in ([i-1,j-1],[i-1,j],[i-1,j+1],[i,j-1],[i,j+1],[i+1,j-1],[i+1,j],[i+1,j+1]):
                if 0<= x < m and 0 <= y < n:
                    if board[x][y] == LIVE:
                        cnt += 1

            if cnt in [0,1,4,5,6,7,8]:
                temp[i][j] = DEAD
            elif board[i][j] == DEAD and cnt == 2:
                pass
            else:
                temp[i][j] = LIVE


        for i in range(m):#更新一次模板矩阵
            for j in range(n):
                search(i,j)
        for i in range(m):#赋值
            for j in range(n):
                board[i][j] = temp[i][j]

```
题解中还有解法就是矩阵的卷积，真滴可以嗷。

```python
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        import numpy as np
        r, c = len(board), len(board[0])
        # 下面两行做 zero padding
        board_exp = np.array([[0 for _ in range(c + 2)] for _ in range(r + 2)])
        board_exp[1:1 + r, 1:1 + c] = np.array(board)
        # 设置卷积核
        kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        # 开始卷积
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                # 统计细胞周围 8 个位置的状态
                temp_sum = np.sum(kernel * board_exp[i - 1:i + 2, j - 1:j + 2])
                # 按照题目规则进行判断
                if board_exp[i, j] == 1:
                    if temp_sum < 2 or temp_sum > 3:
                        board[i - 1][j - 1] = 0
                else:
                    if temp_sum == 3:
                        board[i - 1][j - 1] = 1  

作者：LotusPanda
链接：https://leetcode-cn.com/problems/game-of-life/solution/xiong-mao-shua-ti-python3-bao-xue-bao-hui-cvzhong-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
