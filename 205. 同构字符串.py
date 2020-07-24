"""
[205. 同构字符串](https://leetcode-cn.com/problems/isomorphic-strings/)

给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。

所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

示例 1:

输入: s = "egg", t = "add"
输出: true
示例 2:

输入: s = "foo", t = "bar"
输出: false
示例 3:

输入: s = "paper", t = "title"
输出: true
说明:
你可以假设 s 和 t 具有相同的长度。
***

 1. 对s[i]进行判断是否在字典中，如果在，就判断 dic[s[ i ]] == t[i] 是否相等，如果不等，出现错误，就返回False。
 2. 当s[i] 不在字典里面的时候，先判断t[i]是否在字典的值里面，如果t[i]早已在字典中，我们就返回Fasle,说明这个value已经被其他key对应了。
 3. 如果s[i]不在key中 ,t[i]不在value中，那么我们可以建立一个对应关系，加入字典中。
"""
```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        for i in range(len(s)):#
            if s[i] not in dic:
                if t[i] in dic.values():#如果s[i]不在key, t[i]却在val中
                    return False
                dic[s[i]] = t[i]
            else:#s[i]在字典key,对照value t[i]是否相等
                if dic[s[i]] != t[i]:   
                    return False
        return True 

```
