# -*- coding: utf-8 -*-
"""
罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。

示例 1:

输入: 3
输出: "III"

示例 2:


输入: 4
输出: "IV"
示例 3:

输入: 9
输出: "IX"
示例 4:

输入: 58
输出: "LVIII"
解释: L = 50, V = 5, III = 3.
示例 5:

输入: 1994
输出: "MCMXCIV"
解释: M = 1000, CM = 900, XC = 90, IV = 4.
[1000,500,100,50,10, 5, 1]
[  1,  1,   4, 1, 4, 0, 4]
"""

from typing import List 
class Solution:
    def intToRoman(self, num: int) -> str:
        res = [0]*7
        i = 0
        out = ""
        roman_char = ["M","D","C","L","X","V","I"]
        roman = [1000,500,100,50,10,5,1]
        #将一个数进行除法，得到每一个分量的大小
        while num > 0:
            res[i] = num // roman[i]
            num -= res[i]*roman[i]
            i += 1
        print(res)
        i = 0
        #循环得出前面的字符个数乘以该字符
        while i < 6:
            if res[i] != 0 and res[i+1] != 4:
                out += res[i]*roman_char[i]
                i += 1
                continue
            elif res[i] == 1 and res[i+1] == 4: #此处为判断9的情况
                out += (roman_char[i+1]+roman_char[i-1])
                i += 2
                continue
            elif res[i] == 0 and res[i+1] == 4:#此处为判断4的情况
                out += (roman_char[i+1]+roman_char[i])
                i += 2
                continue
            else:
                i += 1
        "考虑最后单独的一个数字不为4的情况"
        if res[-1] != 4:
            out += roman_char[-1]*res[-1]
        return out
if __name__ == "__main__":
    a = Solution()
    print(a.intToRoman(5))
