"""
[59. 螺旋矩阵 II](https://leetcode-cn.com/problems/spiral-matrix-ii/)
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
***
这道题和之前的提取螺旋矩阵是一样的思维：每一次循环，填入一圈的数，下一次迭代，填入下一圈的数。
**注意** 当n为奇数，最后一次填充的时候就只有一个数，这个时候循环填充会填充两次，第一行&最后一行，所以比之前的题目多了一个填最后一个数的判断语句。


"""
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        i = j = 0
        num = 1

        def helper(start_i, start_j, row, col):#输入起始的坐标，和剩余矩形长宽，计算一个环
            nonlocal num
            if row == 1 and col == 1:
                matrix[start_i][start_j] = num
                return
            for i in range(col):#第一行
                matrix[start_i][start_j+i] = num
                num += 1
            for i in range(1, row-1):#最后一列
                matrix[start_i+i][start_j+col-1] = num
                num += 1
            for i in range(col-1,-1,-1):#最后一行
                matrix[start_i+row - 1][start_j+i] = num
                num += 1
            for i in range(row-2, 0, -1):#第一列
                matrix[start_i+i][start_j] = num
                num += 1
        for i in range((n)//2+1):
            helper(i,i,n-2*i,n-2*i)#起始位置每次横纵坐标加一，矩阵范围每次少二
        return matrix
 