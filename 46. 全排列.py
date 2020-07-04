"""
46. 全排列
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
      length = len(nums)
      # out = []
      output = []

      def backtrack(count, out):#构建回溯函数
        if count == length:#确定退出条件，即得到有效解的条件
          output.append(out.copy())
          return 

        for i in range(length):#因为序列长度有多少次就会循环多少次
          if nums[i] not in out:#每次找一个不在输出中的字符
            out.append(nums[i])#将这个字符添加进输出
            backtrack(count+1, out)#回溯
            out.pop()#弹出上一次加入到输出的字符

      backtrack(0, [])
      return output

       

if __name__ == "__main__":
    # res = [1,2,3,4,5]
    # res = res[:4] + res[5:]
    # print(res)
    s = Solution()
    print(s.permute([1,2,3,4,5,6]))

    
