"""
[240. 搜索二维矩阵 II](https://leetcode-cn.com/problems/search-a-2d-matrix-ii/)
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 fal
***
这道题巧妙地地方就在于：
**每行的元素从左到右升序排列。
每列的元素从上到下升序排列**
越往左上角值越小，越往右下角值越大。所以如果但前值比目标值大的话，我们应该减小当前值，选择左移，或者上移。如果目标值比当前值小的话，选择右移或者下移
但是这样会出现两种选择，其实我们可以设定初始点为右上角，或者左下角，这样一来，我们变大或者变小就只需要执行一个方向的操作了。
"""

```python
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix: return False
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n-1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            if matrix[i][j]> target:
                j -= 1
            else:
                i += 1
        return False

```
