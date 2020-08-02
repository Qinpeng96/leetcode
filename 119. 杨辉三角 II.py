"""
[119. 杨辉三角 II](https://leetcode-cn.com/problems/pascals-triangle-ii/)
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。

在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 3
输出: [1,3,3,1]
进阶：

你可以优化你的算法到 O(k) 空间复杂度吗？
***
使用递归法，超时！
"""
```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dic = {}
        def solve(i,j):
            if i < 0 or j < 0: return 
            if j == 0: return 1
            if i == j: return 1
            if (i,j) in dic:
                return dic[(i,j)]
            ans = solve(i-1, j) + solve(i-1, j-1)
            return ans
        
        res = []
        for j in range(rowIndex+1):
            res.append(solve(rowIndex, j))
        return res
```
"""
第二种使用公式法：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200802215120511.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)
这里没有用上面的公式计算，而是用的另一种错位相加的办法。
例如
#
	[1,1] + [0,1,1] = [1,2,1]
	[1,2,1] + [0,1,2,1] = [1,3,3,1]
下面的row_right 表示右移一位，即左边补0，起始还可以优化，因为是对称的，所以可以计算减半。
"""
```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row_left = [1]
        row_right = [1]
        #row_right表示向右移动一位的列表
        for i in range(1, rowIndex+1):
            row_right = [0] + row_left#向右移位
            for j in range(i):#逐位相加
                row_right[j] = row_right[j] + row_left[j]
            row_left = row_right#最后得到的值要赋值给左边，因为右边的列表在下一轮还会继续右移
  
        return row_right

```
