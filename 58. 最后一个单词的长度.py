"""
[58. 最后一个单词的长度](https://leetcode-cn.com/problems/length-of-last-word/)
给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指仅由字母组成、不包含任何空格字符的 最大子字符串。

示例:

输入: "Hello World"
输出: 5
***
这道题本身简单，就是特殊例子很烦。下面列举几种特殊例子：
#
	"aa     "
	"       "
第一个特例才知道，需要将后面的空格去掉，才能开始统计最后一个单词的个数。
第二个例子如果在去空格的时候没有处理好，就会越界。

"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s: return 0
        while s and s[-1] == ' ':#去除字符串右边的空格
            s = s[:-1]
        cnt = 0
        n = len(s)
        for i in range(n-1, -1, -1):#从右向左开始查找非空的个数
            if s[i] != ' ':
                cnt += 1
            else:
                return cnt
        return n

