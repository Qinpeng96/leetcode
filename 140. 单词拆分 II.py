"""
140. 单词拆分 II
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。

说明：

分隔时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
输出:
[
  "cats and dog",
  "cat sand dog"
]
示例 2：

输入:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
输出:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
解释: 注意你可以重复使用字典中的单词。
示例 3：

输入:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
输出:
[]

"""
from typing import List

##超时
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
#         out = []
#         def backtrack(s, output):
#             n = len(s)
#             if n == 0: out.append(output[1:])

#             for i in range(n):
#                 if s[:i+1] in wordDict:
#                     backtrack(s[i+1:], output + " " + s[:i+1])
#         backtrack(s, "")
#         return out
####
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}

        def backtrack(s, memo):
            res = []
            if s in memo: return memo[s]
            if s == "": return []

            for word in wordDict:
                if not s.startswith(word):#换一个字符匹配
                    continue
                if len(s) == len(word):#匹配完成
                    res.append(word)
                else:#前面的匹配成功，之后的还要继续匹配
                    rest = backtrack(s[len(word):], memo)#得到返回值
                    for item in rest:
                        item = word + " " + item#将本次匹配的头字典符加入
                        res.append(item) 

            memo[s] = res
            return res
        return backtrack(s,memo)


###可以使用，之前我的方法有几个问题，首先就是没有在回溯的过程中使用记录表
#导致每次都要计算，使得效率不高，第二：我在进行字符串匹配的时候，是一个一个的匹配，这样回溯的时候也是一个一个
#的回溯，所以可以考虑使用一个字符串一个字符串的进行匹配，回溯的时候也是一个字符串一个字符串的回溯，效率提升
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
#         res = []
#         memo = {}
#         return dfs(s, memo, wordDict)
    
# def dfs(s, memo, wordDict):
#     if s in memo:
#         return memo[s]
#     if s == '':
#         return []
#     res = []
#     for word in wordDict:
#         if not s.startswith(word):
#             continue
#         # 循环到最后而且匹配，则append
#         if len(word) == len(s):
#             res.append(word)
#         # 匹配但是没有循环到最后，于是继续往下，之后需要对返回的结果分别加上当前的word
#         else:
#             rest = dfs(s[len(word):], memo, wordDict)
#             for item in rest:
#                 item = word + ' ' + item
#                 res.append(item)
#     # 保存当前s的结果
#     memo[s] = res
#     return res

if __name__ == "__main__":
    s = Solution()
    ss = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    # ss = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    # wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    print(s.wordBreak(ss, wordDict))
    # s = "abc"
    # s1 = "cd"
    # s1 += 'c'
    # print(s1)

