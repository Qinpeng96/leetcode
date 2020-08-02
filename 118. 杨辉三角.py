"""
[118. 杨辉三角](https://leetcode-cn.com/problems/pascals-triangle/)
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
***
使用递归去解决因为有递归公式：
$$ f(i,j) = f(i-1,j-1)+f(i-1,j)  $$
$$if  (j ==0): f(i,j) = 1$$
$$if  (i ==j): f(i,j) = 1$$

同时在递归的过程中还有大量的重复计算，这里建立了一个字典记录重复的数值，减少运算的时间。
"""
```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dic = {}
        def solve(i,j):
            if i < 0 or j < 0: return
            if (i,j) in dic:
                return dic[(i,j)]
            if i == j: return 1
            if j == 0: return 1
            ans = solve(i-1, j) + solve(i-1, j-1)
            dic[(i,j)] = ans
            return ans
        # print(solve(4,2))
        out = []
        for i in range(numRows):
            res = []
            for j in range(i+1):
                res.append(solve(i,j))
            out.append(res)
        return out

```
