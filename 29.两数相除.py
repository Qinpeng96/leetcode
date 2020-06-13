# -*- coding: utf-8 -*-
"""
给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

 

示例 1：

输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""





"""

"""
from typing import List
# class Solution:
#     def findSubstring(self, s: str, words: List[str]) -> List[int]:

"""
其中字符串的全排列的函数如下 通过递归调用
首先是第一次大循环 i=0 j=0/1/2
    1 进入第一个循环 i=0 j=0:
        1.1 i=0 j=0：不改变；i=1 j=1:不改变；i=2 j=2：不改变；i=3：输出abc 回退到 i=1 j=2
                            i=1 j=2:调换；  i=2 j=2:不改变； i=3：输出acb 回退到 i=0 j=1 
        1.2 i=0 j=1: 要改变；i=1 j=1:不改变; i=2 j=2:不改变； i=3：输出bac 回退到 i=1 j=2
                            i=1 j=2:调换；  i=2 j=2:不改变； i=3：输出bca 回退到 i=0 j=2
        1.3 i=0 j=2: 要改变；i=1 j=1:不改变；i=2 j=2:不改变； i=3: 输出cba 回退到 i=1 j=2
                            i=1 j=2:调换;   i=2 j=2:不改变； i=3：输出cba 循环结束


def permutation(s,i):
    if i == len(s):
        print(s)
    else:
        for j in range(i,len(s)):
            s[j],s[i] = s[i],s[j]
            permutation(s,i+1)
            s[j],s[i] = s[i],s[j]



if __name__ == "__main__":
  test = "abc"
  s = list(test) # 字符串转为数组 ["a","b","c"]
  permutation(s,0)
    
"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        flag = False
        if dividend > 0 and divisor > 0:
            pass
        elif dividend > 0 and divisor < 0:
            divisor = -divisor
            flag = True
        elif dividend < 0 and divisor > 0:
            dividend = -dividend
            flag = True
        else:
            dividend = -dividend
            divisor = -divisor
        if dividend == 0 or dividend < divisor:
            return 0
        if dividend == divisor:
            if flag:
                return -1
            else:
                return 1
        i = 1
        temp = divisor
        while divisor < dividend:
            last_divisor = divisor
            divisor += divisor
            last_i = i
            i += i
        divisor -= last_divisor
        i -= last_i
        i += self.divide(dividend-divisor, temp)
        if flag:
            if -i >= 2147483648:
                return -2147483647
            return -i
        else:
            if i >= 2147483648:
                return 2147483647
            return i
if __name__ == "__main__":
    a = Solution()
    print(a.divide(-15, 4))
    print(a.divide(15, 4))
    print(a.divide(-15, -4))
    print(a.divide(15, -4))
    print(a.divide(0, -4))
    print(a.divide(1, -4))
    print(a.divide(1, 1))
    print(a.divide(-1, -1))
"""
先确定需返回结果的正负号
定义输出变量i = 1， 用divisor += divisor; i += i使divisor快速逼近dividend, 并记录下一共累加了多少次初始的divisor
当divisor>dividend后，使divisor和i都减半，然后用dividend与divisor的差值递归调用这个函数，并与将结果与i相加
最后判断结果有没有越界

作者：cumt_scx
链接：https://leetcode-cn.com/problems/divide-two-integers/solution/di-gui-by-cumt_scx/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        flag = 1 if (dividend >0 and divisor>0) or (dividend <0 and divisor<0) else -1 #设置flag
        dividend = abs(dividend)#将除数和被除数取绝对值
        divisor = abs(divisor)
        ans = 0
        pre_ans = 1
        pre_divisor = divisor#保留原始的除数值
        if dividend >= divisor:#这里其实是为了给递归做弹出的条件，如果小于则返回0
            while dividend >= divisor:
                dividend -= divisor #除数与被除数相减
                divisor += divisor #除数倍增
                ans += pre_ans #每一次的部分“商”累加
                pre_ans += pre_ans #每一次的部分商也倍加
        else:
            return 0 #为了给递归留的出口
        ans = ans + self.divide(dividend, pre_divisor) #递归
        
        ans = min(ans, 2**31-1) if flag == 1 else -min(ans, 2**31) #对输出结果限制
        return ans 