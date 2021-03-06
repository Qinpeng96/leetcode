"""
[5485. 找出最长的超赞子字符串](https://leetcode-cn.com/problems/find-longest-awesome-substring/)
给你一个字符串 s 。请返回 s 中最长的 超赞子字符串 的长度。

「超赞子字符串」需满足满足下述两个条件：

该字符串是 s 的一个非空子字符串
进行任意次数的字符交换重新排序后，该字符串可以变成一个回文字符串
 

示例 1：

输入：s = "3242415"
输出：5
解释："24241" 是最长的超赞子字符串，交换其中的字符后，可以得到回文 "24142"
示例 2：

输入：s = "12345678"
输出：1
示例 3：

输入：s = "213123"
输出：6
解释："213123" 是最长的超赞子字符串，交换其中的字符后，可以得到回文 "231132"
示例 4：

输入：s = "00"
输出：2
***
这里一看数据量就知道这道题不对劲，而且是要求连续的字符串是回文。还是老实打开题解把。
经过分析之后发现，如果一个字符串的随意交换位置之后是回文，那么这个字符串中的词频中奇数个的字符只有一个才会满足回文的条件。大佬的思路来了：
由于只有0-9的数字，也就是10个数，可以使用一个10个长度的二进制数来判断这个字符串内的字符出现次数。使用的位运算就i是异或运算。
#
	0 ^ 0 = 0
	1 ^ 1 = 0
	0 ^ 1 = 1
	1 ^ 0 = 0
可以发现，后面两行每次和1进行异或就相当于是取反。这里我们的 奇偶性也是这样，根据数字的增加 奇偶交替进行，所以使用异或来判断这个字符串是否满足要求（奇数个词的个数为1个）。由于只有十个数字，所以也只需要十个bit位就行。
#
	1010 1010 10  ^ 1 << 1 = 1010 1010 00
	1010 1010 00  ^ 1 << 1 = 1010 1010 10
大佬的思路确实厉害，这样就不用取去看这个字符串是否连续了。

接下来就是重点了
-  每次加入一个数字 i (0~9)，我们就把它移动至它的位置( 1<< i ) 去和state储存状态的字符进行异或，来确定当前这个给字符串内的字符是否满足只有一个为奇数的条件。
- 确定回文的方式有两个，第一个：当两个状态相同的时候，就可以确定当前状态和之前的相同状态字符串两者之间的差（字符串）是一个回文串。可以这么想，一个状态经过进制为二的变换之后得到原来的状态，那么经过的次数肯定是偶数次的。所以将每一个状态加入字典，如果当前的状态在字典中，那么我们计算两者的索引差值就可以得到这个回文字符串长度。
- 还有一种情况就是：有一个状态与之前的状态不同，这就是上面说的，有一个为奇数次数，其他都为偶数次数的状态。但是我们不知道是哪一个数字的个数是奇数，所以就要遍历九个数字，挨个查找，看是否存在一个奇数，其他都是偶数的情况。找到的话就把字典中对应的索引值取出来相减就是对应字符串长度。
	
"""

```python
class Solution:
    def longestAwesome(self, s: str) -> int:
        dic = {0:-1}#为了可以找出单个的值
        out = 0
        state = 0

        for i, v in enumerate(s):
            state = state ^ (1<<int(v))#每一个数字的对应位值计算出现的次数奇偶
            if state not in dic:#如果之前就在字典内，那么就取出对应索引相减，得到字符串长度
                dic[state] = i
            else:
                out = max(out, i - dic[state])
            for j in range(10):#由于存在一个奇数，其他都是偶数，这样也是一个回文串的情况，所以遍历这种情况，确定那一个数是奇数
                newstate = state ^ (1<< j)
                if newstate in dic:
                    out = max(out, i - dic[newstate])
        return out
```
