 """
55. 跳跃游戏
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例 1:

输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
示例 2:

输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。

"""
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        final = len(nums)
        max_pos, end = 0, 0
        if final == 1: return True
        if nums[0] == 0: return False
        for i in range(final-1):
            max_pos = max(max_pos, nums[i] + i)
            if i == end:
                end = max_pos
            if end >= final-1:
                return True
        return False


#动态规法的方法，从后向前
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp=[False]*len(nums)
        dp[-1]=True
        index=len(nums)-1#记录可达到的最左边的数的索引
        for i in range(len(nums)-2,-1,-1):#从倒数第二个数开始找，因为最后一个数默认可以达到
            if index-i<=nums[i]:#如果左边的数 nums[i]+i大于等于左边的数，即可以到达
                index=i#那么更新左边的边界线
                dp[index]=True#dp数组中这个位置的值设置为True，即从这里可以到达初始设定的 index,最后一个数
        
        return dp[0]


if __name__ == "__main__":
  s = Solution()
  print(s.canJump([1,0,1,0,2]))

