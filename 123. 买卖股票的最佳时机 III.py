"""
123. 买卖股票的最佳时机 III
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
示例 2:

输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。   
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。   
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3:

输入: [7,6,4,3,1] 
输出: 0 
解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。

"""
from typing import List
#动态规划的方法 dp[i][j][k]
# i:天数  j:持有/未持有   k:交易次数(卖出)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        count = len(prices)
        dp = [[[0]*3  for _ in range(2)] for _ in range(count)]

        dp[0][0][0] = 0                  #第一天，啥都没做
        dp[0][0][1] = -float('INF')      #第一天卖了一次，不存在
        dp[0][0][2] = -float('INF')      #第一天卖了两次，不存在
        dp[0][1][0] = -prices[0]         #第一天买一次了，但是没卖，但是有股票
        dp[0][1][1] = -float('INF')      #第一天卖一了次，还有股票，不存在
        dp[0][1][2] = -float('INF')      #第一天卖了两次，还有股票不存在

        for i in range(1, count): 
            # for k in range(1, 3):
            #     dp[i][0][k] = max(dp[i-1][0][k], dp[i-1][1][k-1] + prices[i])#不持有股票
            #     dp[i][1][k] = max(dp[i-1][1][k], dp[i-1][0][k] - prices[i])#持有股票。买入的时候变化的k
            # 
            #未持股，未卖出过，说明从未进行过买卖
            dp[i][0][0]=0
            #未持股，卖出过1次，可能是今天卖的，可能是之前卖的
            dp[i][0][1]=max(dp[i-1][1][0]+prices[i],dp[i-1][0][1])
            #未持股，卖出过2次，可能是今天卖的，可能是之前卖的
            dp[i][0][2]=max(dp[i-1][1][1]+prices[i],dp[i-1][0][2])
            #持股，未卖出过，可能是今天买的，可能是之前买的
            dp[i][1][0]=max(dp[i-1][0][0]-prices[i],dp[i-1][1][0])
            #持股，卖出过1次，可能是今天买的，可能是之前买的
            dp[i][1][1]=max(dp[i-1][0][1]-prices[i],dp[i-1][1][1])
            #持股，卖出过2次，不可能
            dp[i][1][2]=float('-inf')
        print(dp)

        return max(dp[-1][0])



###################################################
#动态规划的方法 dp[i][j][k]
# i:天数  j:持有/未持有   k:交易次数(买入)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        count = len(prices)
        dp = [[[0]*3  for _ in range(2)] for _ in range(count)]
        # print(dp)
        dp[0][0][0] = 0
        dp[0][0][1] = -float('INF')
        dp[0][0][2] = -float('INF')
        dp[0][1][0] = 0
        dp[0][1][1] = -prices[0]
        dp[0][1][2] = -float('INF')

        for i in range(1, count):
            for k in range(1, 3):
                dp[i][0][k] = max(dp[i-1][0][k], dp[i-1][1][k] + prices[i])#不持有股票
                dp[i][1][k] = max(dp[i-1][1][k], dp[i-1][0][k-1] - prices[i])#持有股票

        return max(dp[-1][0])


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit(prices = [3,3,5,0,0,3,1,4]))