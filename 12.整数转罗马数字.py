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