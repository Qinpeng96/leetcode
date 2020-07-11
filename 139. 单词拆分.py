"""
139. 单词拆分
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，
判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
"""
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s: return False
        wordDict.sort(key = lambda x:len(x))#对字典进行排序
        n = len(s)#计算字符串长度
        dp = [0] * (n + 1)#初始化动态数组
        for i in range(1, n+1):#这里从1开始
            for j in wordDict:
                length = len(j)
                if length > i:#对字典中的字符串排序了的，减少时间
                    break
                if j  == s[i-length:i]:#字符串相等
                    #这里需要去一个max,防止就尾部一小块单独匹配
                    dp[i] = max(dp[i], dp[i-length] + length)
        if dp[-1] == n:
            return True 
        else:
            return False



if __name__ == "__main__":
    s = Solution()
    sentence = "abcd"
    dictionary = ["a", "abc", "b", "cd"]
    # sentence = "dogs"
    # dictionary = ["dog","s", "gs"]
    print(s.wordBreak(sentence, dictionary))


    
