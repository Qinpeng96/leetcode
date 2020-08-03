"""
[415. 字符串相加](https://leetcode-cn.com/problems/add-strings/)
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：

num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
***
自己瞎搞整了这么多，看着烦。
"""
```python
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        Flag = 0
        num1 = list(num1[::-1])
        num2 = list(num2[::-1])
        m, n = len(num1), len(num2)
        
        if m < n:
            num1, num2 = num2, num1
        else:
            m, n = n, m
            
        for i in range(m):
            if Flag:
                temp = int(num1[i]) + int(num2[i]) + 1
                Flag = 0
            else:
                temp = int(num1[i]) + int(num2[i])

            num = temp % 10
            Flag = temp // 10
            num1[i] = str(num)

        while Flag and m < n:#处理短的算完之后，单个的进位
            if int(num1[m]) + 1 < 10:
                num1[m] = str(int(num1[m])+1)
                Flag = 0
            else:
                num1[m] = str(0)
                m = m + 1
        if Flag: num1.append('1')#两个数都算完了，但是还有进位

        return ''.join(num1[::-1])
```
看看大佬的代码。高下立判：

```python
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res = str(tmp % 10) + res
            i, j = i - 1, j - 1
        return "1" + res if carry else res

作者：jyd
链接：https://leetcode-cn.com/problems/add-strings/solution/add-strings-shuang-zhi-zhen-fa-by-jyd/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
