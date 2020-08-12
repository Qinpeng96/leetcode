[剑指 Offer 64. 求1+2+…+n](https://leetcode-cn.com/problems/qiu-12n-lcof/)
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

示例 1：

输入: n = 3
输出: 6
示例 2：

输入: n = 9
输出: 45
***

下面这样的写法是位运算的写法，但是使用了一些关键字，所以不可取

```python
class Solution:
    def sumNums(self, n: int) -> int:
        #加法的位运算，递归的时候转化为 和 与 进位相加
        def add(a, b):
            if b == 0: return a
            return add( a^b, (a&b) << 1)
        #位运算乘法
        def mul(a, b):
            ans = 0
            while b:
                if (b & 1):
                    ans = add(ans, a)
                a <<= 1
                b >>= 1
            return ans
        return mul(n, n+1) >> 1
```
看看大佬的做法：

```python
class Solution:
    def __init__(self):
        self.res = 0
    def sumNums(self, n: int) -> int:
        n > 1 and self.sumNums(n - 1)
        self.res += n
        return self.res

作者：jyd
链接：https://leetcode-cn.com/problems/qiu-12n-lcof/solution/mian-shi-ti-64-qiu-1-2-nluo-ji-fu-duan-lu-qing-xi-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
