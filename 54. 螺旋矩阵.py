"""
[54. 螺旋矩阵](https://leetcode-cn.com/problems/spiral-matrix/)
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:

输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]
***

 1. 从[0, 0]开始顺时针旋转一圈，得到的值记录在res中。
 2. 之后又以[1,1]为起始点，顺时针旋转记录一圈。
 3. 特数的情况是只有一行，或者只有一列的时候。
 4. 每旋转一圈，其中的剩余矩阵长宽减少2。

"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        def helper(start_i, start_j, row, col):#输入起始的坐标，和剩余矩形长宽，计算一个环
            res = []
            for i in range(col):#第一行
                res.append(matrix[start_i][start_j+i])
            for i in range(1, row-1):#最后一列
                res.append(matrix[start_i+i][start_j+col-1])
            for i in range(col-1,-1,-1):#最后一行
                res.append(matrix[start_i+row - 1][start_j+i])
            for i in range(row-2, 0, -1):#第一列
                res.append(matrix[start_i+i][start_j])
            return res

        if not matrix: return []#如果为空，直接返回
        m, n = len(matrix), len(matrix[0])
        i = 0
        out = []
        while m > 0 and n > 0 and matrix[i][i] not in out:#弹出条件，行，列不为0，并且起始点没使用过
            if m == 1 and n > 0:#当只有一行的时候，直接加入
                for k in range(n):
                    out.append(matrix[i][i+k])
                return out
            elif n == 1 and m > 0:#当只有一列的时候，直接加入W
                for k in range(m):
                    out.append(matrix[i+k][i])
                return out
            #如果不止一行，或者一列，则需要计算一个环，使用helper函数
            out = out + helper(i, i, m, n)#
            i += 1
            m -= 2
            n -= 2
        return out

