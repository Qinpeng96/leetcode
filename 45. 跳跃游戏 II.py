"""
45. 跳跃游戏 II
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
说明:

假设你总是可以到达数组的最后一个位置。
"""

from typing import List
#递归的方法，超时。
# class Solution:
#     def jump(self, nums: List[int]) -> int:
#       final = len(nums) 
#       out = []
#       if final == 1: return 0

#       def greed(start, count):
#         if nums[start] + start >= final - 1:
#           out.append(count+1)
#           return 
#         mid = nums[start] + start
#         for i in range(mid, start, -1):
#           greed(i, count+1)
#       greed(0, 0)
#       return min(out)
        
class Solution:
    def jump(self, nums: List[int]) -> int:
      final = len(nums) 
      max_pos, end, step = 0, 0, 0
      for pre in range(final-1):
        max_pos = max(max_pos, nums[pre]+pre)
        if pre == end:
          step += 1
          end = max_pos
      return step


if __name__ == "__main__":
  s = Solution()
  # nums = [2,3,1,1,2,3,1,2,3,2,3,1,1,2,1,1,1,4,2,1,1,1,4,3,4]
  # nums = [2,3,2,1,1,1,4,3,4]
  nums = [2,3,1,1,4]
  # nums = [5,9,3,2,1,0,2,3,3,1,0,0]
  # nums = [5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5]
  print(s.jump(nums))


