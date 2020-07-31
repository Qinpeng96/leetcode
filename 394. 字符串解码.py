"""
[394. 字符串解码](https://leetcode-cn.com/problems/decode-string/)
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

 
示例 1：

输入：s = "3[a]2[bc]"
输出："aaabcbc"
示例 2：

输入：s = "3[a2[c]]"
输出："accaccacc"
示例 3：

输入：s = "2[abc]3[cd]ef"
输出："abcabccdcdcdef"
示例 4：

输入：s = "abc3[cd]xyz"
输出："abccdcdcdxyz"
***
显先示说一说里面的坑：

 1. 字符串的重复个数可能是大于十的，所以需要累加
 2. 字符可能是小写，也可能是大写，小写和大写中间的字符还包括了  " [ ", " ] "。
 3. 开始的时候每次我只存上一步的 乘数和重复后的字符串。导致多重括号失效
 4. 这里的栈是用来存储两个东西，上一段的重复串，和当前【】内的重复次数
 5. 当没有括号的时候，就是表示这个字符串的个数是1，由于这里是直接存在stack中，相当于一个前串。否则按照老套路非要找一个【】来计算重复次数，就很难。
 6. 总之，这里stack.append([mul, res])是亮点。
"""
```python
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        mul = 0
        res = ""
        # out = ""
        for item in s:
            if item == '[':#已经算出之前的重复串，得到了当前的乘数值，保存在栈中
                stack.append([mul, res])
                mul, res = 0, ""#保存之后清零
            elif 'A' <= item <= 'Z' or 'a' <= item <= 'z':#这里有可能是大写，有可能是小写
                res += item
            elif item == ']':#尾括号就应该计算放前的重复串，计算后和之前的重复串相加
                cur_mul, pre_res = stack.pop()#弹出上一个重复串和本次的乘数
                res = pre_res + cur_mul * res
            else:
                mul = mul*10+int(item)#乘数有可能是多位数
        return res
```
