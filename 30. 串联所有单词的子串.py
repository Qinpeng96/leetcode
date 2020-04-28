
"""
给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

 

示例 1：

输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。

**********************************************
本方法为滑动窗口法，得到word长度在s字符串上进行滑动匹配
每次滑动的过程中还需将窗口内的字符串分解为单个的单词

对每个窗口内的单词频数和待匹配的words内的单词频数进行比较
这样就省去了对[a,b,c]进行打乱排序的操作。比较的是两者的频数。

from collections import Counter
例如：Counter({'foo': 1, 'bar': 1})

注意：
列表的快速使用方法：
a = [1,2,3,4]
xx  = [s[i，i+j] for j in range(a)]

word_list = [s[j:j+1] for j in range(words_len)]
**********************************************
输入：
    s = "wordgoodgoodgoodbestword"
    words = ["good","good","best","word"]

1.对s中进行窗口滑动，
wordgoodgoodgood
ordgoodgoodgoodb
rdgoodgoodgoodbe
dgoodgoodgoodbes
goodgoodgoodbest
oodgoodgoodbestw
odgoodgoodbestwo
dgoodgoodbestwor
goodgoodbestword

2.按照词长度分割单词
['word', 'good', 'good', 'good']
['ordg', 'oodg', 'oodg', 'oodb']
['rdgo', 'odgo', 'odgo', 'odbe']
['dgoo', 'dgoo', 'dgoo', 'dbes']
['good', 'good', 'good', 'best']
['oodg', 'oodg', 'oodb', 'estw']
['odgo', 'odgo', 'odbe', 'stwo']
['dgoo', 'dgoo', 'dbes', 'twor']
['good', 'good', 'best', 'word']

3.比较每一列别的词频，如果词频一致就匹配成功，使用函数Counter

"""
from typing import List
from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[str]:
        if not words or not s:return [] #判断为空的条件
        #得到字符串长度， 单词列表内单词的个数以及单词的长度
        s_len =len(s)
        words_len = len(words)
        word_len = len(words[0])

        words_counter = Counter(words)#计算出每个单词的个数，转换为字典
        output = [] #设置输出列表

        for i in range(0, s_len - words_len*word_len + 1):
            # print(s[i : i + words_len*word_len])
            #将滑动窗口内的单词分割
            word_list = [s[i+j*word_len:i+(j+1)*word_len] for j in range(words_len)]
            # print(word_list)
            #计算两者词频是否一致
            if Counter(word_list) == words_counter:
                output.append(i)#将词频一致的首词的下标加入输出列表
        return output

if __name__ == "__main__":
    #初试的预设值
    s = "wordgoodgoodgoodbestword"
    words = ["good","good","best","word"]
    # s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
    # words = ["fooo","barr","wing","ding","wing"]
    # pattern=Counter(words)
    # print(pattern)
    
    #实例化类
    solution = Solution()
    output = solution.findSubstring(s, words)
    print(output)
