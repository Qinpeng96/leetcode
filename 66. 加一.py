"""
[66. 加一](https://leetcode-cn.com/problems/plus-one/)
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
***
本题思路比较简单，就是翻转链表后第一位加一，之后对后面的每一位看是否值大于等于10。如果大于的话就需要求余数并且进位，如果是最后一位，就加一个 1 在末尾。

"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        n = len(digits)
        i = 0
        digits[0] += 1#反转后的第一位加一
        for i in range(n):
            if digits[i] >= 10 and i+1 < n:#值大于9，取余，后一位加一
                digits[i] %= 10
                digits[i+1] += 1
            elif digits[i] >= 10 and i+1 >= n:#值大于9，取余，后一位没数，就添加一个1
                digits[i] %= 10
                digits.append(1)
        digits = digits[::-1]
        return digits
