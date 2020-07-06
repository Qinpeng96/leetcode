"""
78. 子集
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
      length = len(nums)
      output = []

      def backtrack(count, out, index, i):#定义一个回溯函数
        if count == i:
          output.append(out[:])
          return 
        for j in range(index, length):
          backtrack(count+1, out+[nums[j]], j+1, i)

      for i in range(length):#循环改变回溯的输出长度
        backtrack(0,[],0,i)
        
      output.append(nums)
      return output
if __name__ == "__main__":
    s = Solution()
    print(s.subsets([1,2,3]))




    
