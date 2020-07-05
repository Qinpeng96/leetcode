"""
77. 组合
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
      output = []

      def backtrack(out,count,index):
        if count == k:
          output.append(out.copy())
          return 
        for i in range(index,n):#这里为了防止重复使用，每次起始坐标后移
          backtrack(out + [i+1],count+1,i+1)

      backtrack([],0,0)
      return output

#下面这种方法有一个巧妙地地方，由于给出地列表是按顺序排列的，如果给出[1,2,3,4,5], k =3
#那么当out = [1,5] 再要选一个数，或者 out = [4],再要选两个数的时候，之后的回溯什么的都是无解的
#我们再上面的解法中对for循环内的i取了一个下界，每次都要后移一位，这里我们也应该对i取一个上界。
#上界的判断是根据还要取多少个数来确定的，如果还要取两个数则i 的上界为 （n-2+1）左闭右开的缘故
#所以设置i的上界为 n-(k-count)+1
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
      output = []

      def backtrack(out,count,index):
        if count == k:
          output.append(out.copy())
          return 
        for i in range(index,n - (k - count) + 1):#这里为了防止重复使用，每次起始坐标后移
          backtrack(out + [i+1],count+1,i+1)

      backtrack([],0,0)
      return output
if __name__ == "__main__":
    s = Solution()
    print(s.combine(6,3))




    
