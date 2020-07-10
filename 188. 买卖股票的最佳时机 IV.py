"""
188. 买卖股票的最佳时机 IV
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [2,4,1], k = 2
输出: 2
解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
示例 2:

输入: [3,2,6,5,0,3], k = 2
输出: 7
解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。

"""
from typing import List
#动态规划的方法 dp[i][j][k]
# i:天数  j:持有/未持有   k:交易次数(买入)

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices: return 0
        count = len(prices)
        
        #k比列表的一半都长，相当于无限次交易
        if k > count//2:
            res = 0
            for i in range(1, count):
                if prices[i] > prices[i-1]:
                    res += (prices[i]-prices[i-1])
            return res
        elif k == 1:#k ==1的时候，相当于只买卖一次，是之前的一个题目
            # dp_single = [0] * count
            pre, cur = float('INF'), 0
            for i in range(count):
                pre = min(pre, prices[i])
                cur = max(cur, prices[i]-pre)
            return cur  
        
        #计算购买次数为k时候的情形
        dp = [[[0]*(k+1)  for _ in range(2)] for _ in range(count)]
        #给每一层赋初值，首先对每一层，[0][0]没买入，没股票，为0；  [0][1]买入，没股票，不存在
        #对每一次选择买入： 可以选择不买，重复k次，即可以购买1-k次
        for i in range(count):
            dp[i][0][0] = 0
            dp[i][1][0] = -float('INF')
        for j in range(1, k+1):
            dp[0][0][j] = 0
            dp[0][1][j] = -prices[0]
        #三维的dp,dp[i][j][w]，分别代表第几次；是否持有股票；已经购买次数
        for i in range(1, count):
            for w in range(1, k+1):
                dp[i][0][w] = max(dp[i-1][0][w], dp[i-1][1][w] + prices[i])#不持有股票
                dp[i][1][w] = max(dp[i-1][1][w], dp[i-1][0][w-1] - prices[i])#持有股票

        return dp[-1][0][-1]


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit(k = 4 ,prices = [5,7,2,7,3,3,5,3,0]))