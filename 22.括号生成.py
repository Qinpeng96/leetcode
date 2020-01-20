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
if __name__ == "__main__":
    a = Solution()
    print(a.generateParenthesis(3))
    

