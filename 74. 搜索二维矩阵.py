"""
[74. 搜索二维矩阵](https://leetcode-cn.com/problems/search-a-2d-matrix/)

编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
示例 1:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true
示例 2:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
输出: false
***
再二分查找的过程中需要注意两个问题
1.是寻找左边界还是右边界
2.不同的左右边界情况需要是否再取中值的时候加一

```python
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix  or not matrix[0]: return False
        m, n = len(matrix), len(matrix[0])
        top, down = 0, m-1
        while top < down:#二分法,这里取的是左边界
            mid = (top + down + 1) // 2#注意这里多加了一个1
            if matrix[mid][0]  > target:
                down = mid - 1
            else:
                top = mid

        left, right = 0, n-1
        while left < right:#这里取得是右边界
            mid = (left + right) // 2
            if matrix[top][mid] < target:
                left = mid + 1
            else:
                right = mid
        # print(matrix[top][left])
        return (matrix[top][left] == target)
