# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 13:41:53 2019

@author: 79877
"""
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dic: stack.append(c)                #入栈操作,加入 { [ ( ?
            elif dic[stack.pop()] != c: return False    
        return len(stack) == 1
"""
class Solution:
    def isValid(self, s: str) -> bool:
        dict = {'[':']','(':')','{':'}'}
        num = len(s)
        res = []
        for i in range(num):
            if len(res) == 0:
                res.append(s[i])
            elif res[-1] in dict and dict[res[-1]] == s[i]:
                res.pop()
            else:
                res.append(s[i])
        if len(res) == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    s = Solution()
    print(s.isValid("{([][]}()"))
    # print(s.fourSum([0,0,0,0],0))
"""
