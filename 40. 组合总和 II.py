"""

40. 组合总和 II
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]

"""
"""
##普通的回溯方法，这样会产生一些是重复的答案
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
      res = []
      count = len(candidates)
      candidates = sorted(candidates)
      def backtrack(self, index, nums:List[int],tar) -> List[int]:
        if tar ==  target:
          res.append(nums.copy())
          return 0
        
        for i in range(index,count):
          if candidates[i] + tar > target :
            continue
          nums.append(candidates[i])
          tar += candidates[i]
          backtrack(self, i+1, nums, tar)
          nums.pop(-1)
          tar -= candidates[i]

      backtrack(self, 0, [], 0)
      return res
if __name__ == "__main__":
  s = Solution()
  print(s.combinationSum2([10,1,2,7,6,1,5], 8))
"""
###################
#如果将列表首先进行一次排序之后再回溯，
# 可以解决重复解的问题
#
##################
"""
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
      out = []
      count = len(candidates)
      candidates = sorted(candidates)
      if target == 0 or len(candidates) == 0:return []

      def backtrack(self, index, nums:List[int], res) -> List[int]:
        if res ==  0 and (nums not in out):
          out.append(nums.copy())
          return 0
        
        for i in range(index,count):
          if res - candidates[i] <  0:
            continue
          nums.append(candidates[i])
          # res -= candidates[i]
          backtrack(self, i+1, nums, res - candidates[i])
          nums.pop()
          # res += candidates[i]

      backtrack(self, 0, [], target)
      return 
"""
##############################################
##剪枝处理，由于排序是有序数组，所以如果有相同的值，则前面的情况肯定包含后面的情况
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
      out = []
      count = len(candidates)
      candidates = sorted(candidates)#对列表进行排序
      if target == 0 or len(candidates) == 0:return []#如果泪飙为空或者目标值为0，则返回空
      #定义回溯函数，index是每次的坐标位置， nums是临时的结果列表， res就是剩下的余值
      def backtrack(self, index, nums:List[int], res) -> List[int]:
        if res ==  0 : #判断剩余为0 则加入到输出列表
          out.append(nums.copy())
          return 0
        
        for i in range(index,count): #对每一个值进行判断
          if res - candidates[i] <  0: #待加入的目标值不符合，直接退出，因为列表是排序过的，之后肯定不符合
            break
          if i > index and candidates[i] == candidates[i-1]:#如果此时的首字符不是第一个，但是和之前一个一样，则此种情况跳过
            continue
          nums.append(candidates[i]) # 将待定的值加入临时解列表
          backtrack(self, i+1, nums, res - candidates[i])#回溯，回溯的时候下标加一，余值减少
          nums.pop()#回溯到之前的状态，因为条件不满足

      backtrack(self, 0, [], target) #实例回溯
      return out

if __name__ == "__main__":
  s = Solution()
  print(s.combinationSum2([2,5,2,1,2], 5))