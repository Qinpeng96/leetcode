"""
[剑指 Offer 65. 不用加减乘除做加法](https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/)
写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。

 

示例:

输入: a = 1, b = 1
输出: 2
 

提示：

a, b 均可能是负数或 0
结果不会溢出 32 位整数
***
在使用位运算计算数值的时候，注意有可能有负值参与计算，看[大佬的解释](https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/solution/mian-shi-ti-65-bu-yong-jia-jian-cheng-chu-zuo-ji-7/)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200812235418853.png#pic_center)
#
	print(hex(1)) # = 0x1 补码
	print(hex(-1)) # = -0x1 负号 + 原码 （ Python 特色，Java 会直接输出补码）
	
	print(hex(1 & 0xffffffff)) # = 0x1 正数补码
	print(hex(-1 & 0xffffffff)) # = 0xffffffff 负数补码
	
	print(-1 & 0xffffffff) # = 4294967295 （ Python 将其认为正数）
"""
```python
class Solution:
    def add(self, a: int, b: int) -> int:
        x = 0xffffffff
        a, b = a & x, b & x
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)

作者：jyd
链接：https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/solution/mian-shi-ti-65-bu-yong-jia-jian-cheng-chu-zuo-ji-7/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
