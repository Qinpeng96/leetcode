"""
[438. 找到字符串中所有字母异位词](https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/)
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。

字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

说明：

字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。
示例 1:

输入:
s: "cbaebabacd" p: "abc"

输出:
[0, 6]

解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
 示例 2:

输入:
s: "abab" p: "ab"

输出:
[0, 1, 2]

解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
***
具体的解释看之前的两道题目，这里就不赘述了。
[567. 字符串的排列](https://leetcode-cn.com/problems/permutation-in-string/)
[76. 最小覆盖子串](https://leetcode-cn.com/problems/minimum-window-substring/)
"""
```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left, right = 0, 0
        valid = 0
        out = []
        n = len(p)
        need = {}
        win = {}

        for c in p:#建立原始数组的频率字典
            if c not in need:
                need[c] = 1
            else:
                need[c] += 1

        while right < len(s):#对字符串s进行遍历
            c = s[right]
            right += 1
            
            if c in need:#统计字符段内与need字典相同的值以及个数，并统计有效值valid
                if c not in win:
                    win[c] = 1
                else:
                    win[c] += 1
                if win[c] == need[c]:
                    valid += 1
            #当有效值个数相等的时候，缩小左边界。如果两者长度相同，有效值也相同，那么加入到输出      
            while valid == len(need):
                if right - left == n:#加入输出
                    out.append(left)
                d = s[left]
                left += 1#对左边界进行收缩
                if d in need:
                    if win[d] == need[d]:
                        valid -=1
                    win[d] -= 1
        return out
```
