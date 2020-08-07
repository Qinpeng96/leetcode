"""
[剑指 Offer 05. 替换空格](https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/)
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

示例 1：

输入：s = "We are happy."
输出："We%20are%20happy."
***
我的思路就是原地替换，每次替换之后由于多加入的两个字符，所以总长度n要加2，比较指针 i 多了两个元素也加2。在不替换的情况下，指针 i 加一。

"""
```python
class Solution:
    def replaceSpace(self, s: str) -> str:
        n = len(s)
        i = 0
        while i < n:
            if s[i] == ' ':
                s = s[:i] + '%20'+ s[i+1:]
                i += 2
                n += 2
            i += 1
        return s
```
