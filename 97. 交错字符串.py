"""
97. 交错字符串
给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。

示例 1:

输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出: true
示例 2:

输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出: false

"""
from typing import List
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        row = len(s1)
        col = len(s2)
        full = len(s3)
        if row + col != full:return False
        if row == 0 and s2 != s3: return False
        if col == 0 and s1 != s3: return False
        dp = [[False]*(col+1) for _ in range(row+1)]
        dp[0][0] = True#上述条件判断完，可以开始尝试匹配
        #初始化；dp 表的第一行和第一列
        for i in range(1, row+1):
            dp[i][0] = dp[i-1][0] and (s1[i-1] == s3[i-1])

        for j in range(1, col+1):
            dp[0][j] = dp[0][j-1] and (s2[j-1] == s3[j-1])

        #对dp表的剩余元数进行判断
        for i in range(1, row+1):
            for j in range(1, col+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or \
                    (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        return dp[-1][-1]
        print(dp)

if __name__ == "__main__":
    s = Solution()
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print(s.isInterleave(s1, s2, s3))