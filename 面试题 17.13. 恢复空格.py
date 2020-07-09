"""
面试题 17.13. 恢复空格
哦，不！你不小心把一个长篇文章中的空格、标点都删掉了，并且大写也弄成了小写。
像句子"I reset the computer. It still didn’t boot!"已经变成了"iresetthecomputeritstilldidntboot"。
在处理标点符号和大小写之前，你得先把它断成词语。当然了，你有一本厚厚的词典dictionary，不过，有些词没在词典里。
假设文章用sentence表示，设计一个算法，把文章断开，要求未识别的字符最少，返回未识别的字符数。

注意：本题相对原题稍作改动，只需返回未识别的字符数

 

示例：

输入：
dictionary = ["looked","just","like","her","brother"]
sentence = "jesslookedjustliketimherbrother"
输出： 7
解释： 断句后为"jess looked just like tim her brother"，共7个未识别字符。
提示：

0 <= len(sentence) <= 1000
dictionary中总字符数不超过 150000。
你可以认为dictionary和sentence中只包含小写字母。
"""
from typing import List
class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        if dictionary == []: return len(sentence)
        if sentence == "": return 0
        num = len(sentence)
        dp = [0] * (num+1)

        for i in range(1, num+1):
            dp[i] = dp[i-1] + 1#每一个数进来首先就加1位，之后再判断是否可减
            for j in dictionary:#循环判断每一个字典中的字符串
                if len(j) > i:#如果待匹配的长度比s中的当前s[:i]长，说明肯定不能匹配
                    continue
                if j == sentence[i-len(j):i]:#这里由于i是从[1.n+1]的，所以增大了1
                    #由于是对每一个字符串进行判断，可能存在长度不一，但是结尾一致的匹配，
                    #此时回对dp[i]多次更新，选择最小的一个
                    dp[i] = min(dp[i-len(j)], dp[i])

        return dp[-1]
      



if __name__ == "__main__":
    s = Solution()
    dictionary = ["looked","just","like","her","brother"]
    sentence = "jesslookedjustliketimherbrother"
    print(s.respace(dictionary, sentence))


    
