"""
60. 第k个排列
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：

给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。
示例 1:

输入: n = 3, k = 3
输出: "213"
示例 2:

输入: n = 4, k = 9
输出: "2314"
"""
from typing import List
"""
#本方法就是回溯算法，取到第k个的时候，剪枝弹出，但是会超时
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
      output = []
      used = []
      count = []
      nums = [ i+1 for i in range(n)]
      
      def backtrack(out):
        if len(out) == n: 
          count.append(0)
          if len(count) == k:#剪枝，排到第k个就加入输出，剪枝返回
            output.append(out.copy())
            return True
          return False
        for i in range(n):
          if i not in used:
            used.append(i)
            if backtrack(out+[nums[i]]):
              return True
            used.pop()
      backtrack([])
      
      return ''.join(str(output[0][i]) for i in range(n))
"""
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
      res = []
      nums = [i+1 for i in range(n)]#创建一个原始排列【1，2，3】
      used = [i for i in range(n)]#创建一个记录使用的列表
      """
      #建立一个列表nums，用于记录每一位有多少种可能的组合
      #例如5为列表[120, 24, 6, 2,1],但是我们是看该位在总的顺序终得位置
      #例如 [2,1,4,5,3],其中第一位为2，我们可以得知，其在24~48,左开右闭之间
      #之后我们再根据第二位，第三位。。判断，最终缩小空间到 K
      #因为要相除取商，所以最终列表为[24,6,2,1,1]
      """
      def sum(n):
        out = 1
        output = []
        for i in range(1,n):
          out *= i
          output.append(out)
        output = output[::-1]
        output.append(1)
        return output
      #建立好的序号列表赋值给index
      index = sum(n)
      #下面我们还是以12345，第28个举例
      for i in range(0,n):#由于每个数字都可以提供位置信息，所以需要循环n次
        val = k // index[i] #计算两者的商，得到本位的位置索引，例如28//24=1
        k = k % index[i] #计算 k 减去前一位的组合数之后的余数（模）
        if val > 0  and k == 0: #这种情况是刚好k被除尽，说明其在一个小分组的最后一组
           res.append(nums[used[val-1]])#加上本位数所对应的值
           used.pop(val-1)#弹出使用过的数
          #这是一种特数情况，在一个分组的最后， 意思是后面的是是按照最大的排列加入的
           for i in range(len(used)-1,-1,-1):#所以这里就要倒叙加入，直接输出
             res.append(nums[used[i]])
           return ''.join(str(res[i]) for i in range(n))
        else:#说明还有余数，就要重复依次判断所处位置对应的数值
          res.append(nums[used[val]])
          used.pop(val)
      return ''.join(str(res[i]) for i in range(n))

if __name__ == "__main__":
  s = Solution()
  print(s.getPermutation(5,28))
  print(s.getPermutation(9,353955))

   



    
