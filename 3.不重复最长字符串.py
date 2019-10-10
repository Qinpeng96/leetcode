"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1

来源：力扣（LeetCode）

"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        record = dict()     #记录每个字母最后一次出现的下标,key是字母，val是下标
        res, start = 0,0
        for end in range(len(s)):
            if s[end] in record:
                start = max(start, record[s[end]]+1)#取得相同字符的最大下标
            record[s[end]] = end    #"给字典里面的key赋值value"
            res = max(res, end - start + 1)#取的最大长度
        return res
