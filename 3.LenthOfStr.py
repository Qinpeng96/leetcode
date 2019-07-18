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
