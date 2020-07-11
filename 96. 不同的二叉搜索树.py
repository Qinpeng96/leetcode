"""
96. 不同的二叉搜索树
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

dp[0] = 1

dp[1] = 1

当 n = 2时，dp[2] = 2 = dp[0]dp[1] + dp[1]dp[0]

当 n = 3时，dp[3] = 2 = dp[0]dp[2] + dp[1]dp[1] + dp[2]dp[0]


"""

from typing import List
class Solution:
    def numTrees(self, n: int) -> int:
      dp = [0] * (n+1)
      dp[0] = 1
      res = 0
      for i in range(1, n+1):
        for j in range(0, i):
          dp[i] += dp[j]*dp[i-j-1]
      return dp[-1]


#发现规律，可以在第二个for 中计算dp[n]，数量减半
class Solution:
    def numTrees(self, n: int) -> int:
      dp = [0] * (n+1)
      dp[0] = dp[1] = 1
      for i in range(2, n+1):
        res = 0
        for j in range(0, i//2):
          # if 2*j == i-1:
          #   res += dp[j]*dp[j]
          #   break
          res += dp[j]*dp[i-j-1]*2
        if i % 2 == 1:
          res += dp[(i-1)//2]*dp[(i-1)//2]
        dp[i] = res
      return dp[-1]

if __name__ == "__main__":
  s = Solution()
  print(s.numTrees(6))


