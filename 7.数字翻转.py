"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
"""
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        a = str(x)
        y = list(a)
        y.reverse()
        if y[-1] == "-":
            y.remove('-')
            y.insert(0, '-')
        if y[0] == 0:
            y.remove('0')
        y2 = ''.join(y)
        z = int(str(y2))
        if z < (-2**31) or z > (2**31-1):
            z = 0
        return z


class Solution:
    def reverse(self, x):
        #首先对输入进行预处理[-9,9]w
        if -10 < x <10: return x
        str_x = str(x)
        if str_x[-1] == 0: str_x = str_x[:-1]

        if str_x[0] == '-':
            str_x = "-" + str_x[:0:-1]
        else:
            str_x = str_x[::-1]
        str_x = int(str_x)
        if  2**31 - 1 < str_x or str_x < -(2**31):
            return 0 
        else:
            return str_x


if __name__ == "__main__":
    s = Solution()
    out = s.reverse(-132654)
    print(out)
"""
    s = "abcdefg"
    print(s[2::-1])#逆序输出[0:3]
    print(s[:3:-1])#逆序输出最后三个
    print(s[-2:-4:-1])#逆序输出倒数第二个和第三个
"""