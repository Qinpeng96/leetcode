"""
518. 零钱兑换 II
给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。 

 

示例 1:

输入: amount = 5, coins = [1, 2, 5]
输出: 4
解释: 有四种方式可以凑成总金额:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
示例 2:

输入: amount = 3, coins = [2]
输出: 0
解释: 只用面额2的硬币不能凑成总金额3。
示例 3:

输入: amount = 10, coins = [10] 
输出: 1
 

注意:

你可以假设：

0 <= amount (总金额) <= 5000
1 <= coin (硬币面额) <= 5000
硬币种类不超过 500 种
结果符合 32 位符号整数

"""
#以看这么多的金额，面额就知道递归不行，要用动态规划
#dp[i][j] 表示若只使用 coins 中的前 i 个硬币的面值，若想凑出金额 j，有 dp[i][j] 种凑法。
#当需要凑出的钱小于本次面值的时候，我们使用上一个小的面值加入，如果
from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 1

        for i in range(1, n+1):
            for j in range(1, amount+1):
                if j >= coins[i-1]:#可以使用本次货币的面值[使用本次货币+不适用本次货币]
                    dp[i][j] = dp[i][j-coins[i-1]] + dp[i-1][j]
                else:#这种情况只能使用上一次的货币面值
                    dp[i][j] = dp[i-1][j]#不使用第 i 中货币，使用之前的货币的方法
        return dp[-1][-1]


if __name__ == "__main__":
  s = Solution()
  print(s.change(5, [1,2,5]))


