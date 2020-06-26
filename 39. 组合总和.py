"""
39. 组合总和
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
示例 2:

输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
      out = []
      count = len(candidates)
      candidates = sorted(candidates)
      if count == 0 or target == 0: #初始的判定条件
        return []
      #定义回溯函数， nums 临时解列表， res剩余的值， index 循环的游标
      def backtrack(nums: List[int], res, index) -> List[int]:
        if res == 0:#解刚好满足，则进行一个拷贝加入out输出
          out.append(nums.copy())
        for i in range(index, count):
          if res < candidates[i]:#将要加入的值不满足，退出
            return 
          if i > index and candidates[i] == candidates[i-1]: continue#这一步就是判断重复列表解
          nums.append(candidates[i])
          backtrack(nums, res - candidates[i], i)#回溯，其中 i是列表值可以重复使用， i+1则是不能重复使用
          nums.pop()

      backtrack([], target, 0)
      return out

 
if __name__ == "__main__":
  s = Solution()
  print(s.combinationSum([2,1,2,1,2], 9))