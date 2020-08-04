"""
[166. 分数到小数](https://leetcode-cn.com/problems/fraction-to-recurring-decimal/)
给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。

如果小数部分为循环小数，则将循环的部分括在括号内。

示例 1:

输入: numerator = 1, denominator = 2
输出: "0.5"
示例 2:

输入: numerator = 2, denominator = 1
输出: "2"
示例 3:

输入: numerator = 2, denominator = 3
输出: "0.(6)"
***
- 首先排除0
- 确定正负号，使用异或来确定，但是这里bool类型也可以使用异或。
- 使用divmod获得商和余数，如果余数为0，直接返回，如果余数不为0，说明有小数，继续判断。
- 主要是确定无限循环小数的问题，这里使用字典，每一个余数作为键， 其值就是所在的位置(长度)。
- 当有一样的余数出现的时候，我们就知道是一个循环小数，将左括号插入到重复的余数出现的位置，列表末尾再附上一个右括号。
- 如果一直没有重复的余数出现，一会就会被除尽，即余数为0的时候弹出。
-  开始我是用的字符串，但是发现在有重复余数时插入左括号不方便（其实也可以插入）
"""
```python
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0: return "0"
        out = []

        if (numerator > 0) ^ (denominator > 0):#判断正负
            out.append('-')
        numerator, denominator = abs(numerator), abs(denominator)#知道正负之后就可以变成正数计算
        #接下来就是有小数系列
        a, b = divmod(numerator, denominator)
        out.append(str(a))
        if b == 0:
            return "".join(out)
        out.append('.')
        loc = {b:len(out)}#记录余数的位置，
        while b:
            b *= 10
            a, b = divmod(b, denominator)#余数乘以10再除
            out.append(str(a))
            if b in loc:#之前有余数的记录,说明出现循环,注意这里括号应该插入到之前的位置
                out.insert(loc[b],'(')#如果一开始就使用字符串的话不能修改插入
                out.append(')')
                break
            loc[b] = len(out)
        return "".join(out)
```
使用字符串插入：

```python
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0: return "0"
        res = ""
        # 首先判断结果正负, 异或作用就是 两个数不同 为 True 即 1 ^ 0 = 1 或者 0 ^ 1 = 1
        if (numerator > 0) ^ (denominator > 0):
            res += "-"
        numerator, denominator = abs(numerator), abs(denominator)
        # 判读到底有没有小数
        a, b = divmod(numerator, denominator)
        res += str(a)
        # 无小数
        if b == 0:
            return res
        res += "."
        # 处理余数
        # 把所有出现过的余数记录下来
        loc = {b: len(res)}
        while b:
            b *= 10
            a, b = divmod(b, denominator)
            res += str(a)
            # 余数前面出现过,说明开始循环了,加括号
            if b in loc:
                res = res[:loc[b]] + '(' + res[loc[b]:]
                # res.insert(loc[b], "(")
                res += ")"
                break
            # 在把该位置的记录下来
            loc[b] = len(res)
        return res

```
