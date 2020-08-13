"""
[647. 回文子串](https://leetcode-cn.com/problems/palindromic-substrings/)
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。

示例 1:

输入: "abc"
输出: 3
解释: 三个回文子串: "a", "b", "c".
示例 2:

输入: "aaa"
输出: 6
说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
注意:

输入的字符串长度不会超过1000。
***
回文的数据量不大，所以可以考虑使用O(N*N)的方法。
首先是动态归的方法：由于当个的字符也是一个回文串，所以我们设置dp table的时候，设置为二维的dp, dp[i][j]表示为索引i~j内是否构成回文串。

下面的配图来自：
[https://leetcode-cn.com/problems/palindromic-substrings/solution/647-hui-wen-zi-chuan-dong-tai-gui-hua-fang-shi-qiu/](https://leetcode-cn.com/problems/palindromic-substrings/solution/647-hui-wen-zi-chuan-dong-tai-gui-hua-fang-shi-qiu/)

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200813152709108.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)
可以看到，一致的单个的字符串是回文串，所以中间的b是回文， dp[2][2] =True, 之后我们考虑dp[i+1][j-1]的状态，可以看出 s[i+1] == s[j-1],并且内部的是s[2]还是一个回文，所以dp[i+1][j-1]也是回文。由此可以推出动态转移方程：
$$dp[i][j] = dp[i+1][j-1]  ;  if :s[i] == s[j] $$
还有一种特殊情况就是当 j == i + 1，并且 s[i] == s[j],这个时候可以直接赋值dp[i][j] = True。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200813153616300.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)

"""
```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        out = 0 
        dp = [[False]*n for _ in range(n)]
        for i in range(n):#对角线上一个元数全为True
            dp[i][i] = True
        
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:#如果两个元数相等
                    if j-1 == i:#并且两个元数相邻
                        dp[i][j] = True#直接赋值True
                    else:#否则当前的dp状态和之前内部的状态有关
                        dp[i][j] = dp[i+1][j-1]
                else:#不等，直接赋值False
                    dp[i][j] = False

                if dp[i][j] == True:#统计右上角的回文个数
                    out += 1
        # print(dp)
        return out+n
```
***
除此之外还有一种中心展开的方法，分别以奇数回文和偶数回文进行展开。

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        self.out = 0
        def count(s, i, j):
            while 0 <= i and j < n:
                if s[i] == s[j]:
                    self.out += 1
                    i -= 1
                    j += 1
                else:
                    break
        
        for i in range(n):
            count(s, i, i)#统计奇回文
            count(s, i, i+1)#统计偶回文
        return self.out

```
