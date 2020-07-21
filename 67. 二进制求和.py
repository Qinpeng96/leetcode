"""
[67. 二进制求和](https://leetcode-cn.com/problems/add-binary/)
给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。

示例 1:
输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"
 
提示：

每个字符串仅由字符 '0' 或 '1' 组成。
1 <= a.length, b.length <= 10^4
字符串如果不是 "0" ，就都不含前导零。
***

 1. 首先将字符串变为链表，并且两者都进行翻转，将长度较长的那一个设置为a列表，短的设置为b列表
 2. 对两者长度较长的列表长度进行循环，其中两数相加的情况在 长度较小的范围内进行。这里设置了一个Flag用于表示进位信息
 3. 当短链表被加完之后，我们只对剩余的长链表和Flag标志位进行相加
 4. 最后如果Flag还为1，那么说明最后还有一个进位，需要在链表最后append一个1
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m = len(a)
        n = len(b)
        Flag = 0
        a = list(a)
        b = list(b)
        if m < n:#对链表进行翻转和交换，使得a始终最长
            a, b = b[::-1],a[::-1]
        else:
            a, b = a[::-1], b[::-1]
            
        for i in range(max(m,n)):# 1+1+F, 1+1, 1+0+F, 1+0, 0+0+F，0+0
            if i < min(m,n):#在两数相加的情况下的各种判断
                if a[i] == b[i] and  a[i]== '0' and Flag == 0:
                    a[i] = '0'
                    continue
                elif a[i] == b[i] and a[i]== '0' and Flag == 1:
                    a[i] = '1'
                    Flag = 0
                    continue
                elif a[i] != b[i] and Flag == 0:
                    a[i] = '1'
                    continue
                elif a[i] != b[i] and Flag == 1:
                    a[i] = '0'
                    continue
                elif a[i] == b[i] and a[i]== '1' and Flag == 0:
                    a[i] = '0'
                    Flag = 1
                    continue
                elif a[i] == b[i] == '1' and Flag == 1:
                    a[i] = '1'
                    continue
            else:#只有剩下的a和进位标志位相加
                if Flag:
                    if a[i] == '1':
                        a[i] = '0'
                    else:
                        a[i] = '1'
                        Flag = 0
        if Flag == 1:#最后如果还有进位，则添加一在末尾
            a.append('1')
            
        return ''.join(a[::-1])

