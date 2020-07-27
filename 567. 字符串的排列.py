"""
[567. 字符串的排列](https://leetcode-cn.com/problems/permutation-in-string/)
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

换句话说，第一个字符串的排列之一是第二个字符串的子串。

示例1:
输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").
 
示例2:
输入: s1= "ab" s2 = "eidboaoo"
输出: False
 注意：

输入的字符串只包含小写字母
两个字符串的长度都在 [1, 10,000] 之间
***
和上一道[76. 最小覆盖子串](https://leetcode-cn.com/problems/minimum-window-substring/)题目的做法基本是一致的，
只不过这道题的字符串长度是固定的。所以只要当滑动窗口的长度一致，并且valid有效的个数也一样，那么就可以说明这个窗口内的字符是匹配的。

和之前的方法一样：

 1. 创建一个待匹配字符串的字典频率计数
 2. 在s2中使用双指针，右指针右移，直到窗口内的字符字典和待匹配的s1的字符字典相同的时候，缩小左边界。
 3. 左边界在缩小的过程中，如果窗口的长度等于s1的长度，并且valid值和s1的字典长度是相同的，说明刚好匹配，直接输出。
 4. 如果窗口长度小于s1的长度是肯定不能vaild == len(need)，会跳出循环
 5. 如果窗口长度大于s1的长度，就缩小左边界。如果左边界的弹出的值是s1字典中的值，那么win中的字典值也要对应减一，并且valid也要减一。
 6. 如果搜寻完了整个s2都没有匹配上，就返回False。
"""
```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right = 0, 0
        valid = 0
        win = {}
        need = {}
        length = float('inf')
        n = len(s1)

        for c in s1:#创建一个字典计数
            if c not in need:
                need[c] = 1
            else:
                need[c] += 1
        
        while right < len(s2):
            c = s2[right]
            right += 1#右移右边界
            if c in need:
                if c not in win:
                    win[c] = 1
                else:
                    win[c] += 1
                if win[c] == need[c]:
                    valid += 1
            
            #开始缩小左边界
            while valid == len(need):
                if right - left == n:#如果长度相等，并且valid相同，输出True
                    return True
                else:#长度大了，就缩小左边界。缩小的过程中如果删除了win中valid项，那么就跳出循环，增加右边界
                    d = s2[left]
                    left += 1
                    if d in need:
                        if win[d] == need[d]:
                            valid -= 1
                        win[d] -= 1
        return False
```
