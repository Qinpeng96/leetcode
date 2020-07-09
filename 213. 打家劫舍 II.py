"""
213. 打家劫舍 II
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，
这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [2,3,2]
输出: 3
解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
示例 2:

输入: [1,2,3,1]
输出: 4
解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。
"""
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0#判断两个特殊情况
        if len(nums) == 1: return nums[0]

        def rob_circle(nums):#这和上一题的打家劫舍是一样的，只不过不用加判断是否为空
            len_nums = len(nums)
            dp = [0] * (len_nums+1)
            dp[0] = 0
            dp[1] = nums[0]

            for i in range(2, len_nums+1):#这里是动态规划，取当前值，和不取当前值。
                dp[i] = max(dp[i-1] , dp[i-2]+ nums[i-1]) 
            return dp[-1]
        return max(rob_circle(nums[1:]), rob_circle(nums[:-1]))




if __name__ == "__main__":
    s = Solution()
    print(s.rob([2]))
    # print(s.rob([2,7,9,3,1]))

