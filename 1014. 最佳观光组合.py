"""
1014. 最佳观光组合
给定正整数数组 A，A[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的距离为 j - i。

一对景点（i < j）组成的观光组合的得分为（A[i] + A[j] + i - j）：景点的评分之和减去它们两者之间的距离。

返回一对观光景点能取得的最高分。

 

示例：

输入：[8,1,5,2,6]
输出：11
解释：i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
 

提示：

2 <= A.length <= 50000
1 <= A[i] <= 1000

****
最佳观光路线就是 A[i] + A[j] + i - j的值，我们可以拆分一下，在确定 j 的位置的时候，
寻找A[i] + i - j的最大值，再变形一下，确定A[i] + i 的最大值。即再确定 A[j] - j 的情况下，
寻找之前的一个最大 A[i] + i；
***
"""
from typing import List
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        num = len(A)
        start_max = out = 0
        for i in range(1,num):
            start_max = max(start_max,A[i-1]+i-1)
            out = max(out, start_max+A[i]-i)
        return out
                    

if __name__ == "__main__":
    s = Solution()
    print(s.maxScoreSightseeingPair([8,1,5,2,6]))