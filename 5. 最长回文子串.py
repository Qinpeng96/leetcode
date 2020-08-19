"""
[5. 最长回文子串](https://leetcode-cn.com/problems/longest-palindromic-substring/)
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
***
**中心扩散的方法**

 1. 首先根据回文列表元素的奇偶性，选择一个、或者两个元素作为起点，从左到右进行循环
 2. 每次循环都向左右进行判断是否是回文 [相当于暴力法]
 """
```python
#中心扩散（1）
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str 
        :rtype: str
        """
        max_l = 0
        res = ""
        for i in range(0, len(s)):
            #以s[i] 为中心向左右扩散
            left, right = i, i
            while(left >= 0 and right < len(s) and s[left] == s[right]):
                if max_l < right - left + 1:
                    max_l = right - left + 1
                    res = s[left:right + 1]
                left -= 1
                right += 1
                        
            #以s[i],s[i+1]为中心向左右扩散
            left, right = i, i + 1
            while(left >= 0 and right < len(s) and s[left] == s[right]):
                if max_l < right - left + 1:
                    max_l = right - left + 1
                    res = s[left:right + 1]
                left -= 1
                right += 1            
        return res
        
#中心扩散（2）
def force(self, s: str) -> str:
        
        if s==s[::-1]:
            return s
        max_len = 1
        res = s[0]
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                if j - i + 1 > max_len and s[i:j+1] == s[i:j+1][::-1]:
                    max_len = j - i + 1
                    res = s[i:j + 1]
        return res
```
"""
大佬的题解很好，这里贴一下：
[威威大佬的题解](https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zhong-xin-kuo-san-dong-tai-gui-hua-by-liweiwei1419/)

这道题还可以使用动态规划的方法：
设置dp[i][j]定义为从索引i到j,是否为一个回文，值为False和True。
- 建立一个n*n的dp table with Fasle
- 初始化左对角线上面的元素为True,因为单个的字符肯定是回文
- 接着就是开始dp，由于我们需要求的是最长的回文，那么答案应该在每一行都有可能出现（以每一个值作为起始）。
- 动态转移方程, 当s[i] == s[j]的时候，说明有两个字符相等，如果这俩字符相邻，那么直接赋值d[i][j] = true. 如果不相邻，那么当前的状态和之前的内部状态有关$dp[i][j] = dp[i+1][j-1]$。
- 每一行可以从对角线开始计数， 找到从左往右最长的True,这之间就是一个回文，每次都取一个最长的回文，在对每一行进行遍历，就可以得到结果。
- 由于我们的递推公式中当前值是与下一行的左边值可能有关，所以递推的顺序就是从下往上，从左往右计算。
- 最后，如果没有找到长度大于1的回文，那么直接返回s[0],单个的字符作为回文。

"""
```python
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n <= 1: return s
        maxlen = 1
        out = s[0]

        #creat dp table
        dp = [[False]*n for _ in range(n)]

        #init
        for i in range(n):
            dp[i][i] = True

        
        #start dp
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    if j - 1 ==  i:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                
                if dp[i][j] == True:
                    if j-i+1 > maxlen:
                        out = s[i:j+1]
                        maxlen = j-i+1
        return out
```
