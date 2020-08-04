"""
[202. 快乐数](https://leetcode-cn.com/problems/happy-number/)
编写202. 快乐数一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。

如果 n 是快乐数就返回 True ；不是，则返回 False 。

 

示例：

输入：19
输出：true
解释：
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
***
如果得到值算出来和之前的重复了，那么说明开始陷入一个循环，就不是快乐数。

"""
```python
class Solution:
    def isHappy(self, n: int) -> bool:
        res = 0
        visited = set()
        while True:
            if n > 9:
                res += (n % 10)**2
                n = n // 10
            else:
                res += n**2
                if res not in visited:#将每次计算的结果放入集合，如果有相同说明开始循环，Fasle
                    visited.add(res)
                else:
                    return False
                n = res#如果本次算出来一个新值
                if n == 1:
                    return True
                res = 0#注意这里需要清零

```
