# -*- coding: utf-8 -*-

"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""

from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def double_tree(S = '',left = 0, right = 0):
            if len(S) == 2*n:
                ans.append(S)
                return 
            if left < n:
                double_tree(S + '(', left + 1, right)
            if right < left:
                double_tree(S + ')', left , right + 1)
        double_tree()
        return ans
"""方法二 直接生成
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def generate(S:str, c, val:int,count:int):
            S = S + c
            if val < 0: return 0
            if len(S) == 2*n and val == 0:
                res.append(S)
                return 0
            if count > 2*n:
                return 0
            else:
                generate(S ,'(',val+1,count+1)
                generate(S , ')',val-1,count+1)
        generate("",'(',1,1)
        return res
"""
if __name__ == "__main__":
    a = Solution()
    print(a.generateParenthesis(3))
    

