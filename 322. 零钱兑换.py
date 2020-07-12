"""
322. 零钱兑换
给定不同面额的硬币 coins 和一个总金额 amount。
编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
 

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3 
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1
 

说明:
你可以认为每种硬币的数量是无限的。

"""
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[0]*(amount+1) for _ in range(len(coins)+1)]
        for i in range(1,amount+1):
          dp[0][i] = float('inf')

        for i in range(1, len(coins)+1):
          for j in range(1, amount+1):
            if j >= coins[i-1]:
              dp[i][j] = min(dp[i][j-coins[i-1]] + 1, dp[i-1][j])
            else:
              dp[i][j] = dp[i-1][j]
        print(dp)
        if dp[-1][-1] != float('inf'):
          return dp[-1][-1]
        else:
          return -1


if __name__ == "__main__":
  s = Solution()
  print(s.coinChange([3,5],7))

