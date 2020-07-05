"""
52. N皇后 II
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。



上图为 8 皇后问题的一种解法。

给定一个整数 n，返回 n 皇后不同的解决方案的数量。

示例:

输入: 4
输出: 2
解释: 4 皇后问题存在如下两个不同的解法。
[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-queens-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
"""
假设皇后的坐标如下，做右对角线和横竖线与坐标之间有一定关系
[[(1,1),(1,2),(1,3)],
[(2,1),(2,2),(2,3)],
[(3,1),(3,2),(3,3)]]
上面就是col纵坐标相同，则为同一列


每对坐标相减得到，可以看到纵坐标减横坐标，可以得到左对角线
差值相同的都是再一条左对角线上面
[[(0),(1),(2)],
[(-1),(0),(1)],
[(-2),(-1),(0)]]

横纵坐标相加，则可以得到右对角线
[[(2),(3),(4)],
[(3),(4),(5)],
[(4),(5),(6)]]
"""
from typing import List
class Solution:
    def totalNQueens(self, n: int) -> int:
      out = []

      def backtrack(left_d, right_d, column):
        row = len(column)
        if row == n:
          out.append(1)
          return
        for col in range(n):
          if row+col in right_d or col-row in left_d or col in column:
            continue
          backtrack(left_d + [col-row],right_d + [row+col],column  + [col])
      backtrack([],[],[])
      return len(out)
       

if __name__ == "__main__":
    s = Solution()
    print(s.totalNQueens(8))

    
