"""
[剑指 Offer 50. 第一个只出现一次的字符](https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/)
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例:

s = "abaccdeff"
返回 "b"

s = "" 
返回 " "
 

限制：

0 <= s 的长度 <= 50000
***
每次判断字符，如果字符不在字典，就加入字典，键值为索引号，否则把键值赋值为正无穷。
第二步就是对键值进行排序，取序号最小且不等于正无穷得进行输出。
"""
```python
class Solution:
    def firstUniqChar(self, s: str) -> str:
        if not s: return " "
        n = len(s)
        dic = {}
        for i in range(n):
            if s[i] not in dic:
                dic[s[i]] = i
            else:
                dic[s[i]] = float('inf')
        dic = sorted(dic.values(), key = lambda x:x)
        return s[dic[0]] if  dic[0] != float('inf') else " "
```


看看大佬得代码：
快太多了，实则佩服
```python
class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for c in s:
            dic[c] = not c in dic#加入的是一个bool值，之前存在加入False, 否则加入True
        for c in s:
            if dic[c]: return c
        return ' '

作者：jyd
链接：https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/solution/mian-shi-ti-50-di-yi-ge-zhi-chu-xian-yi-ci-de-zi-3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
