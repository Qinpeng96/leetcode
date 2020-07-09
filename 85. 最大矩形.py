"""
85. 最大矩形
给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例:

输入:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
输出: 6
"""
from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        m = len(matrix)
        n = len(matrix[0])
        out = 0
        #构建一个矩阵，每行的左右两端增加一个0
        column = [[0 for i in range(n+2)] for i in range(m)]

        for i in range(0, m):#将原始的字符矩阵换成数字矩阵
            for j in range(1, n+1):
                column[i][j] = int(matrix[i][j-1])
        #对数字矩阵的每行进行判断，如果每行有值（不为0），则累加该行上一行的对应元素值
        #这样做的目的是，构建m（行数）个柱形图。类似于leetcode 84题，使用84的求柱状图的最大面积
        #将一个矩阵，分解为行数个柱状图，进行求解。
        for i in range(1, m):
            for j in range(1,n+1):
                if column[i][j] == 1:
                    column[i][j] += column[i-1][j]

        #使用的是84题，单调递增栈的做法，计算柱状图的最大面积
        def max_area(s: List[int])->int:
            res = 0
            stack = []
            for i in range(n+2):
                while stack and s[stack[-1]] > s[i]:
                    height_index = stack.pop()
                    res = max(res, (i - stack[-1] - 1) * s[height_index])
                stack.append(i)
            return res
        #循环重复m次，计算出每一行的最大柱状面积，再找一个最大值输出
        for i in range(m):
            out = max(out, max_area(column[i]))
        return out
            
if __name__ == "__main__":
    s = Solution()
    print(s.maximalRectangle(["1","0","1","1","1"]))

    # print(s.maximalRectangle([
    #     ["1","0","1","0","0"],
    #     ["1","0","1","1","1"],
    #     ["1","1","1","1","1"],
    #     ["1","0","0","1","0"]
    # ]))
