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
    
