"""
714. 买卖股票的最佳时机含手续费
给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。

你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。

返回获得利润的最大值。

注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

示例 1:

输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
输出: 8
解释: 能够达到的最大利润:  
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
注意:

0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.

"""
from typing import List
#动态规划的方法
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        count = len(prices)
        dp = [[0]*2  for _ in range(count)]
        dp[0][1] = -prices[0]
        res = 0
        for i in range(1, count):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)#持有股票
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])#不持有股票

        print(dp)
        return dp[-1][0]

#考虑到上述公式中每次只有两个参数保存计算，所以可以简化一下
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        count = len(prices) 
        empty, bought = 0, -prices[0]
        cur_empty = cur_bought = 0
        for i in range(1, count):
            cur_empty = max(empty, bought + prices[i] - fee)#持有股票
            cur_bought = max(bought, empty - prices[i])#不持有股票
            bought, empty = cur_bought, cur_empty
        return cur_empty


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit(prices = [1, 3, 2, 8, 4, 9], fee = 2))