# -*- coding: utf-8 -*-
"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 
"""
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        num = len(strs)
        if num == 0:
            return ""
        if num == 1:
            return strs[0]
        num1 = len(strs[0])
        res = ""
        for i in range(num):
            if strs[i] == "":
                return ""
        for i in range(num):
            num1 = min(len(strs[i]),num1)

        for i in range(num):
            if strs[i][0] != strs[0][0]:
                return ("")
        j = 0
        while j < num1:
            i = 0
            while i < num:
                if (strs[i][j] == strs[0][j]):
                    i += 1
                else:
                    return (res)
            res += (strs[0][j])
            j += 1 
        return res

            
        
if __name__ == "__main__":
    a = Solution()
    print(a.longestCommonPrefix(["aacc","aa","aa","aa","aaca"]))
#    print(a.longestCommonPrefix(["",""]))
"""
思路：
思路 1：
Python 特性，取每一个单词的同一位置的字母，看是否相同。

思路 2：
取一个单词 s，和后面单词比较，看 s 与每个单词相同的最长前缀是多少！遍历所有单词

思路 3：
按字典排序数组，比较第一个，和最后一个单词，有多少前缀相同。

代码:
思路一：
class Solution:
    def longestCommonPrefix(self, strs):
        

        # :type strs: List[str]
        # :rtype: str

        res = ""
        for tmp in zip(*strs):
            tmp_set = set(tmp)
            if len(tmp_set) == 1:
                res += tmp[0]
            else:
                break
        return res
思路二：
PythonJava
class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        if not s:
            return ""
        res = s[0]
        i = 1
        while i < len(s):
            while s[i].find(res) != 0:
                res = res[0:len(res)-1]
            i += 1
        return res
思路三：
PythonJava
class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        if not s:
            return ""
        s.sort()
        n = len(s)
        a = s[0]
        b = s[n-1]
        res = ""
        for i in range(len(a)):
            if i < len(b) and a[i] == b[i]:
                res += a[i]
            else:
                break
        return res

作者：powcai
链接：https://leetcode-cn.com/problems/longest-common-prefix/solution/duo-chong-si-lu-qiu-jie-by-powcai-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        num = len(strs)
        if num == 0:return ""

        res = min(len(i) for i in strs )
        for i in range(num-1):
            for j in range(res):
                if strs[i][j] == strs[i+1][j]:
                    pass
                else:
                    res = min(res,j)
                    break  
        return strs[0][:res]      


if __name__ == '__main__':
    solution = Solution()
    out = solution.longestCommonPrefix([])
    print(out)
            