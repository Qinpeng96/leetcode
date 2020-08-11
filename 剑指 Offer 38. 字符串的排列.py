"""
[剑指 Offer 38. 字符串的排列](https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/)
输入一个字符串，打印出该字符串中字符的所有排列。


你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

 示例:

输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
 

限制：

1 <= s 的长度 <= 8
***

开始使用回溯，但是如果不适用集合就会超时
"""
```python
class Solution:
    def permutation(self, s: str) -> List[str]:
        if not s: return [""]
        out = set()#加入的集合，过滤重复的字符串
        def backtrack(s,  res):
            if not s:
                out.add(res)
            for i in range(len(s)):
                backtrack(s[:i]+s[i+1:], res + s[i])

        backtrack(s, "")
        # out = out.sort()
        return list(out)
```
重复方案与剪枝： 当字符串存在重复字符时，排列方案中也存在重复方案。为排除重复方案，需在固定某位字符时，保证 “每种字符只在此位固定一次” ，即遇到重复字符时不交换，直接跳过。从 DFS 角度看，此操作称为 “剪枝” 。

但是上面的方法运行的很慢，还有一个问题就是重复的字符不能够跳过，例如：
#
	[a,a,b] 
我们开始以第一个a作为起始字符的时候，第二个a会被添加到待输出字符串内。但是在以第二个a为首字符的时候，之后的所有组合情况都已经在上一次计算过了，所以可以不用再计算了。这就是可以剪枝的地方。下面的程序就是对原始的字符串进行了字符排序，如果当前字符和前一个字符是一样的，就剪枝跳过。

```python

class Solution:
    def permutation(self, s: str) -> List[str]:
        if not s: return [""]
        s = [s[i] for i in range(len(s))]
        sorted_s = sorted(s)
        out = []

        def backtrack(s, res):
            if not s:#所以不可能有重复的字符串
                out.append(res)
            for i in range(len(s)):
                if i > 0 and s[i] == s[i-1]:#剪枝跳过的条件
                    continue
                else:
                    backtrack(s[:i]+s[i+1:], res+s[i])
        backtrack(sorted_s, "")
        return out
        
```
还是看看大佬的思路：
这里的剪枝我们可以先不排序，做出一个集合记录之前谁用过的字符，如果出现重复的字符，就跳过，少一个排序，相邻元数比较的过程。

```python
class Solution:
    def permutation(self, s: str) -> List[str]:
        self.res = []
        n = len(s)

        def backtrack(s, path):
            if not s:
                self.res.append(path)
            seen = set()
            for i in range(len(s)):
                if s[i] in seen: continue
                seen.add(s[i])
                backtrack(s[:i]+s[i+1:], path + s[i])

        backtrack(s, "")
        return self.res
```
