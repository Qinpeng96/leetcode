"""
面试题 08.08. 有重复字符串的排列组合
有重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合。

示例1:

 输入：S = "qqe"
 输出：["eqq","qeq","qqe"]
示例2:

 输入：S = "ab"
 输出：["ab", "ba"]
提示:

字符都是英文字母。
字符串长度在[1, 9]之间。
"""
"""
#本方法使用了一个额外的列表来记录每次回溯的时候，这个字符是否被使用过
from typing import List
class Solution:
    def permutation(self, S: str) -> List[str]:
      out = []
      count = len(S)
      def backtrack(combination,used):
        if len(used) == count:
          temp = ''.join(combination)
          if temp not in out:
            out.append(temp)
          return 

        
        for i in range(count):
          if i in used:
            continue
          else:
            used.append(i)
          combination.append(S[i])
          backtrack(combination,used)
          combination.pop()
          used.pop()
      backtrack([], [])
      return out
"""

"""
#回溯的过程中字符是在减少的，所以就不需要方法一的建立记录表
#剩余的列表中每个都是未被使用的
from typing import List
class Solution:
    def permutation(self, S: str) -> List[str]:
      out = []
      count = len(S)
      def backtrack(combination,res):
        if len(combination) == count:
          temp = ''.join(combination)
          if temp not in out:
            out.append(temp)
          return 
        
        for i in range(len(res)):#没有对齐进行剪枝的操作
          combination.append(res[i])
          backtrack(combination,res[:i]+res[i+1:])
          combination.pop()

      backtrack([], S)
      return out
"""
#排序之后进行剪枝，如果两个字符相同，那么这两个字符后面组成的字串也是相同的，所以
#可以提前进行剪枝
from typing import List
class Solution:
    def permutation(self, S: str) -> List[str]:
      out = []
      count = len(S)
      S = sorted(S)
      def backtrack(combination,res):
        if len(combination) == count:
          temp = ''.join(combination)#将单个字符合成字符串
          if temp not in out:
            out.append(temp)
          return 
        
        for i in range(len(res)):
          if i > 0 and res[i-1] == res[i]:#相邻字符相同，剪枝操作
            continue
          combination.append(res[i])#回溯操作
          backtrack(combination,res[:i]+res[i+1:])
          combination.pop()

      backtrack([], S)
      return out

if __name__ == "__main__":
  s = Solution()
  print(s.permutation("aba"))


