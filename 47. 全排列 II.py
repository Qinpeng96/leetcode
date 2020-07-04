"""
47. 全排列 II
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
 
"""
from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
      length = len(nums)
      output = []
      nums = sorted(nums)
      # nums.append('.')

      def backtrack(count, out, stack):#构建回溯函数
        if count == length :#确定退出条件，即得到有效解的条件
          output.append(out.copy())
          return 

        for i in range(length):#因为序列长度有多少次就会循环多少次
          if i in stack:
            continue
          if i > 0 and nums[i] == nums[i-1] and i-1 not in stack:#剪枝
            continue
          out.append(nums[i])#将这个字符添加进输出
          stack.append(i)
          backtrack(count+1, out, stack)#回溯
          out.pop()#弹出上一次加入到输出的字符
          stack.pop()

      backtrack(0, [], [])
      return output

       

if __name__ == "__main__":
    s = Solution()
    print(s.permuteUnique([2,2,3]))




    
