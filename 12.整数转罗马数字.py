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

"""

class Solution:
    def intToRoman(self, num: int) -> str:
        # 把阿拉伯数字与罗马数字可能出现的所有情况和对应关系，放在两个数组中
        # 并且按照阿拉伯数字的大小降序排列，这是贪心选择思想
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        index = 0
        res = ''
        while index < 13:
            # 注意：这里是等于号，表示尽量使用大的"面值"
            while num >= nums[index]:
                res += romans[index]
                num -= nums[index]
            index += 1
        return res


class Solution:
    def intToRoman(self, num: int) -> str:
        res = [0]*7
        i = 0
        out = ""
        roman_char = ["M","D","C","L","X","V","I"]
        roman = [1000,500,100,50,10,5,1]
        while num > 0:
            res[i] = num // roman[i]
            num -= res[i]*roman[i]
            i += 1
        print(res)
        i = 0
        while i < 6:
            if res[i] != 0 and res[i+1] != 4:
                out += res[i]*roman_char[i]
                i += 1
                continue
            elif res[i] == 1 and res[i+1] == 4:
                out += (roman_char[i+1]+roman_char[i-1])
                i += 2
                continue
            elif res[i] == 0 and res[i+1] == 4:
                out += (roman_char[i+1]+roman_char[i])
                i += 2
                continue
            else:
                i += 1
        if res[-1] != 4:
            out += roman_char[-1]*res[-1]
        return out

"""
12. 整数转罗马数字
罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。

https://leetcode-cn.com/problems/integer-to-roman/

                字符          数值
                I             1
                V             5
                X             10
                L             50
                C             100
                D             500
                M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，
所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。

示例 1:

                输入: 3
                输出: "III"
                示例 2:

                输入: 4
                输出: "IV"
                示例 3:

                输入: 9
                输出: "IX"
                示例 4:

                输入: 58
                输出: "LVIII"
                解释: L = 50, V = 5, III = 3.
                示例 5:

                输入: 1994
                输出: "MCMXCIV"
                解释: M = 1000, CM = 900, XC = 90, IV = 4.

*********************************************************************
本文使用的方法就是字典查找：

 1. 首先建立一个字典{数字："罗马数字"}
 2. 对输入的数字进行拆分，从后向前每次提取一位数字，并且保存其【位数】(个十百千万......)
 3. 对提取的每个数字进行判断，因为4和9的输出特别一点
 4. 将提取的每个罗马数字加入输出字符串。（注意：这是加入的时候是倒叙加入的罗马字符，比如数字4对应的罗马字符是 "IV", 但是在加入的时候时加入的 "VI"）
 5. 最后将字符串反转输出即可。
*********************************************************************

"""
from typing import List
class Solution:
    def intToRoman(self, num: int) -> str:
        dict ={1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}#建立字典
        i = 1 #设置位数{个十百千万}
        out = "" #建立输出的字符串
        while num > 0:
            res = num - ( num // 10 ) * 10 #从后向前取每个位上的数字
            if res < 4:#对所取得的数字进行分类（此时位数 i 也需要加入辅助输出）
                out = out + dict[i]*res
            elif res == 4:
                out = out + dict[5*i] + dict[i] 
            elif 4 < res < 9:
                out = out + dict[i] *(res % 5) + dict[5*i]
            else:
                out = out + dict[i*10] + dict[i]
            i *= 10 #位数向前进位 个位变十位。。。
            num = num // 10 #输入数字除去尾数
        return out[::-1] #反转输出
        
if __name__ == "__main__":
    s = Solution()
    out = s.intToRoman(58)
    print(out)  