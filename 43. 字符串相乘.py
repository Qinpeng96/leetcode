"""
43. 字符串相乘
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
"""

from typing import List
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
      len_num1 = len(num1)#计算两个字符串的长度
      len_num2 = len(num2)
      res = [0] * (len_num1 + len_num2)#创建输出长度，默认为0 
      #从后向前对两个字符串内的数进行相乘，得到的结果放在res
      for i in range(len_num1-1, -1, -1):
        key = i + len_num2 #这里的key值就是放在输出数组的位置
        for j in range(len_num2-1, -1, -1):
          temp = int(num1[i]) * int(num2[j])#单独的数字相乘
          res[key] = ((temp % 10) + int(res[key])) #获得当前位的个位数值
          if res[key] > 9:#如果第i 位要进位
            res[key] %= 10
            res[key-1] += 1 
          res[key-1] = (temp // 10 + int(res[key-1]))#相乘后的十位
          if res[key-1] > 9:#如果十位进位后的数还要进位
            res[key-1] %= 10
            res[key-2] += 1 
          key -= 1
      print(res)

      #计算出来的是列表的形式，列表前面可能还有0
      out = res[0]
      for i in range(1, len_num1 + len_num2):#从前到后，依次累加计算出数值
        out = out*10 + res[i]
        print(out)

      return str(out)#最后输出的时候将数值转换为字符串

       

if __name__ == "__main__":
  s = Solution()
  num1 = "3"
  num2 = "1"
  print(s.multiply(num1, num2))




