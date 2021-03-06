"""
[5470. 平衡括号字符串的最少插入次数](https://leetcode-cn.com/problems/minimum-insertions-to-balance-a-parentheses-string/)
给你一个括号字符串 s ，它只包含字符 '(' 和 ')' 。一个括号字符串被称为平衡的当它满足：

任何左括号 '(' 必须对应两个连续的右括号 '))' 。
左括号 '(' 必须在对应的连续两个右括号 '))' 之前。
比方说 "())"， "())(())))" 和 "(())())))" 都是平衡的， ")()"， "()))" 和 "(()))" 都是不平衡的。

你可以在任意位置插入字符 '(' 和 ')' 使字符串平衡。

请你返回让 s 平衡的最少插入次数。

 

示例 1：

输入：s = "(()))"
输出：1
解释：第二个左括号有与之匹配的两个右括号，但是第一个左括号只有一个右括号。我们需要在字符串结尾额外增加一个 ')' 使字符串变成平衡字符串 "(())))" 。
示例 2：

输入：s = "())"
输出：0
解释：字符串已经平衡了。
示例 3：

输入：s = "))())("
输出：3
解释：添加 '(' 去匹配最开头的 '))' ，然后添加 '))' 去匹配最后一个 '(' 。
示例 4：

输入：s = "(((((("
输出：12
解释：添加 12 个 ')' 得到平衡字符串。
示例 5：

输入：s = ")))))))"
输出：5
解释：在字符串开头添加 4 个 '(' 并在结尾添加 1 个 ')' ，字符串变成平衡字符串 "(((())))))))" 。
***
- 先把s入栈，每次弹出一个，判断是左括号还是右括号
- 如果是右括号，继续弹栈
- 如果是左括号，判断res内的右括号个数是否为奇数，如果是奇数，那么加一个，变成偶数，弹出两个
- 最后res里面全是右括号，或者为空。还有右括号就对右括号进行配对
"""
```python
class Solution:
    def minInsertions(self, s: str) -> int:
        if not s: return 0
        n = len(s)
        stack = []
        for i in range(n):#入栈
            stack.append(s[i])
        res = []
        cnt = 0
        while stack:#弹栈
            temp = stack.pop()
            if temp == ')':#右括号就入res栈
                res.append(')')
            else:#左括号先判断res内的奇偶
                if len(res) & 1:
                    res.append(')')
                    cnt += 1
                if res:
                    res.pop()
                    res.pop()
                else:
                    cnt += 2
        if res:#如果弹栈完成，就剩余的右括号配对
            n = len(res)
            if n & 1:
                cnt += n//2 + 2
            else:
                cnt += n//2

        return cnt
```
