# -*- coding: utf-8 -*-
"""
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
说明:

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-strstr
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
自己写的，非常low
大家笑一笑就好
"""


"""
Sunday 算法

还可以使用偏移表进行匹配移动
如果当前的主字符串不匹配，则检测主字符串的下个字符是否在待匹配字符串中
如果不在，则主字符串中的指针位置就偏移到len(待匹配字符串)+1的位置，减少了中间的重复匹配环节
节约时间的消耗
"""
from typing import List
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = j = 0
        if len(needle) == 0 : return 0
        if len(needle) > len(haystack): return -1
        while j < len(needle):
            # 找到一个匹配的字符
            while i < len(haystack) and haystack[i] != needle[j]:
                i += 1
            if i >= len(haystack):
                return -1
            # 依次判断之后的字符是否匹配
            while j < len(needle) and i <= len(haystack) + j - len(needle) and haystack[i] == needle[j]:
                i += 1
                j += 1
            if j == len(needle) and len(needle) < len(haystack):
                return i-len(needle)
            elif j == len(needle) and j == len(haystack):
                return 0
            else:
                i = i - j + 1
                j = 0

# 系统自带的方法
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.index(needle) if needle in haystack else -1


if __name__ == "__main__":
    a = Solution()
    print(a.strStr("mississippi", "issipi"))
    print(a.strStr("hello", "ll"))
    print(a.strStr("aaa", "aaa"))
    print(a.strStr("mississippi", "pi"))

    