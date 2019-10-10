"""
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

"""
class Solution(object):
    def convert(self, s, n):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        #麻瓜解法：开个数组，把输入按要求放进去，然后再按输出顺序读出来
        if n <= 1:
            return s
        l = len(s)
        #创建一个二维的列表[0]*5 for _ in range(3)即
        #创建一个3*5的0列表
        #1. 从上往下压， 定义state = "down"，
        #每次x += 1，当x触底就转换state为"up"
        #2. 从左下往右上压， 定义state = "up"，
        #每次 x -= 1, y += 1， 当x归零就转换state为"down"
        record = [[0] * l for _ in range(n)]
        x, y = 0, 0
        state = "down"
        #for (index,char) in enumerate(S)同时使用下标和元素进行循环
        for i, char in enumerate(s):
            # print x, y, char
            record[x][y] = char
            if state == "down":
                if x != n - 1:
                    x += 1
                else:
                    state = "up"
                    x -= 1
                    y += 1
                continue
            
            elif state == "up":
                if x != 0:
                    x -= 1
                    y += 1
                else:
                    state = "down"
                    x += 1
        # print record
        res = ""
        for row in record:
            for char in row:
                if char != 0:
                    res += char
        
        return res
