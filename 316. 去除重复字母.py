"""
[316. 去除重复字母](https://leetcode-cn.com/problems/remove-duplicate-letters/)
给你一个仅包含小写字母的字符串，请你去除字符串中重复的字母，使得每个字母只出现一次。
需保证返回结果的字典序最小（要求不能打乱其他字符的相对位置）。
示例 1:

输入: "bcabc"
输出: "abc"
示例 2:

输入: "cbacdcbc"
输出: "acdb"
***
用栈来存储最终返回的字符串，并维持字符串的最小字典序。每遇到一个字符，如果这个字符不存在于栈中，
就需要将该字符压入栈中。但在压入之前，需要先将之后还会出现，并且字典序比当前字符小的栈顶字符移除，
然后再将当前字符压入。


"""
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if not s: return ""
        n = len(s)
        stack = [s[0]]
        for i in range(1,n):
            if s[i] not in stack:#首先判断是否在栈中，如果已经包含了，那么就是无需再次排序
                while stack and s[i] < stack[-1] and stack[-1] in s[i+1:]:#栈顶元素之后还有，并且小于待加入的元素，那么可以弹栈。
                    stack.pop()
                stack.append(s[i])
        return ''.join(stack)


