"""
[76. 最小覆盖子串](https://leetcode-cn.com/problems/minimum-window-substring/)
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：

如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。
***
思路很直接，但是显然，这个算法的复杂度肯定⼤于 O(N^2) 了，不好。

**滑动窗⼝算法**的思路是这样：
1、我们在字符串  S  中使⽤双指针中的左右指针技巧，初始化  left = right = 0 ，把索引左闭右开区间  [left, right)  称为⼀个「窗⼝」。

2、我们先不断地增加  right  指针扩⼤窗⼝  [left, right) ，直到窗⼝中的字符串符合要求（包含了  T  中的所有字符）。

3、此时，我们停⽌增加  right ，转⽽不断增加  left  指针缩⼩窗⼝ [left, right) ，直到窗⼝中的字符串不再符合要求（不包含  T  中的所有字符了）。同时，每次增加  left ，我们都要更新⼀轮结果。

4、重复第 2 和第 3 步，直到  right  到达字符串  S  的尽头。

这个思路其实也不难，第 2 步相当于在寻找⼀个「可⾏解」，然后第 3 步在优化这个「可⾏解」，最终找到最优解，也就是最短的覆盖⼦串。左右指针轮流前进，窗⼝⼤⼩增增减减，窗⼝不断向右滑动，这就是「滑动窗⼝」这个名字的来历。
下⾯画图理解⼀下， needs  和  window  相当于计数器，分别记录  T  中字符出现次数和「窗⼝」中的相应字符的出现次数


现在开始套模板，只需要思考以下四个问题：
1、当移动  right  扩⼤窗⼝，即加⼊字符时，应该更新哪些数据？
2、什么条件下，窗⼝应该暂停扩⼤，开始移动  left  缩⼩窗⼝？
3、当移动  left  缩⼩窗⼝，即移出字符时，应该更新哪些数据？
4、我们要的结果应该在扩⼤窗⼝时还是缩⼩窗⼝时进⾏更新？

如果⼀个字符进⼊窗⼝，应该增加  window  计数器；如果⼀个字符将移出窗⼝的时候，应该减少  window  计数器；当  valid  满⾜  need  时应该收缩窗⼝；应该在收缩窗⼝的时候更新最终结果。
"""
```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0
        valid = 0
        need = {}
        win = {}
        length = float('inf')
        
        for c in t:
            if c not in need:
                need[c] = 1
            else:
                need[c] += 1
        while right < len(s):

            c = s[right]
            right += 1#边界右移
            #对s中的字符判断是否在need中，如果在need中，并且win中数量和need中的一致，那么vaild就加一
            if c in need:
                if c not in win:
                    win[c] = 1
                else:
                    win[c] += 1
                if win[c] == need[c]:
                    valid += 1
            #如果本窗口内的字符已经满足条件，现在需要缩小左边界，边缩小，边更新验证
            while valid == len(need):
                if right - left < length:#更新滑动窗口的范围和左边界
                    start = left
                    length = right - left
                
                d = s[left]
                left += 1#边界左缩
                #左移窗口的时候，如果移除的字符在need中，就需要将win[d] 减一，并且可能会使valid-1
                if d in need:
                    if win[d] == need[d]:
                        valid -= 1
                    win[d] -= 1
                    
        return s[start:start+length] if length != float('inf') else ""

```
