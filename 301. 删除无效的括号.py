"""
[301. 删除无效的括号](https://leetcode-cn.com/problems/remove-invalid-parentheses/)
删除最小数量的无效括号，使得输入的字符串有效，返回所有可能的结果。

说明: 输入可能包含了除 ( 和 ) 以外的字符。

示例 1:

输入: "()())()"
输出: ["()()()", "(())()"]
示例 2:

输入: "(a)())()"
输出: ["(a)()()", "(a())()"]
示例 3:

输入: ")("
输出: [""]
***
这道题的问题是最小删除次数，所以这里优先选用 BFS.
- 首先建立一个判断是否括号合法的函数，可以使用计数也可以使用栈。
- BFS首先加入s到字符串集合中
- 判断当前的集合内的字符串是否有合法的，如果有就提前返回
- 如果没有就要考虑删除字符串的的一些括号，我们每一层的删除之后就传递给下一层，如果下一层还是没有合法的，就继续上一层的删除后的字符串继续删除。
- 总的来说就是每一层对集合内的字符串，每一个字符串选择一个括号删除，所以一个字符串内有多少个括号，一个字符串就有多少个删除可能性，把每一个字符串的
    删除可能性加入到下一层的集合内部，放到下一层进行判断。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200813165718432.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)

"""

```python
class Solution:
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s):#使用栈来判断是否合法
            stack = []
            for i in range(len(s)):
                if s[i] == '(':
                    stack.append('(')
                elif s[i] == ')' :
                    if stack:
                        stack.pop()
                    else:
                        return False
            return True if not stack else False


        level = {s}#建立第一个层级，这个层级没有删除元数
        # print(level)
        while level:#层次BFS
            res = []
            for s in level:#找这个层级内的合法字串
                if isValid(s):
                    res.append(s)
            if res != []: return res

            next_level = set()#创建下一个层级
            for s in level:
                for i in range(len(s)):
                    if s[i] in ['(',')']:#对当前层级的每一个字符串的每一个括号，进行删除后加入集合
                        next_level.add(s[:i]+s[i+1:])
            level = next_level#集合的赋值，变成当前集合

```
