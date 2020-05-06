"""
9. 回文数
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:

你能不将整数转为字符串来解决这个问题吗？
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        if 0<= x <10:return True
        str_x = str(x)
        n = len(str_x)
        left, right = 0, n-1
        while left <= right:
            if str_x[left] == str_x[right]:
                left += 1
                right -= 1
            else:
                break
        if left > right:
            return True
        else:
            return False

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        str_x = str(x)
        if str_x == str_x[::-1]:
            return True
        else:
            return False
if __name__ == "__main__":
    s = Solution()
    out = s.isPalindrome(-9)
    print(out)
    # str1 = "     this is string example....wow!!!     "
    # print (str1.lstrip())
    # str1 = "88888888this is string example....wow!!!8888888"
    # print (str1.lstrip('8'))
