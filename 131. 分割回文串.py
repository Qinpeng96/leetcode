"""
[131. 分割回文串](https://leetcode-cn.com/problems/palindrome-partitioning/)
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例:

输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]
***
本题使用回溯算法：
1.首先回溯弹出的条件就是需要判断的字符串为空
2.回溯的过程，由于我们在判度是否是回文字符串的时候，使用的是s[:i]左闭右开的区间，所以在循环的时候，
    索引值为(1, len(s)+1)。只有当左边的字符串的是回文串的时候，才进行下一步的判度。
3.在进行下一层回溯的时候，我们需要把当前的已经判度过的回文串加入到临时输出中。但是注意这个有个坑，加入已经判度过的为一个单字符，
    也是回文串，但是list连接的时候，是不能连接字符的，所以需要加一个中括号，改成list类型。
"""

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output =[]
        def backtrack(s, cur):
            if not s:
                output.append(cur)#没有需要判断的字符，加入输出
            for i in range(1, len(s)+1):#对每一个可能的分割点进行分割
                if s[:i] == s[:i][::-1]:#如果前一段是回文串，那么判断下一段是否是回文，并且把之前判断过的回文串加入到临时待定的输出中。
                    backtrack(s[i:],cur + [s[:i]])
        backtrack(s, [])
        return output
```
