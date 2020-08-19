"""
[LCP 02. 分式化简](https://leetcode-cn.com/problems/deep-dark-fraction/)
有一个同学在学习分式。他需要将一个连分数化成最简分数，你能帮助他吗？
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200817184837538.png#pic_center)
连分数是形如上图的分式。在本题中，所有系数都是大于等于0的整数。

输入的cont代表连分数的系数（cont[0]代表上图的a0，以此类推）。返回一个长度为2的数组[n, m]，使得连分数的值等于n / m，且n, m最大公约数为1。

 示例 1：

输入：cont = [3, 2, 0, 2]
输出：[13, 4]
解释：原连分数等价于3 + (1 / (2 + (1 / (0 + 1 / 2))))。注意[26, 8], [-13, -4]都不是正确答案
***
例如[a, b, c, d]
从最后一个开始计算一个数，两个数，三个数。。。答案依次如下：
#
	[d,1]:			[d, 1]
	[c,d,1]:		[cd+1, d]
	[b,c,d,1]:		[bcd+b+d, cd+1]
	[a,b,c,d,1]:	[abcd+ab+ad+cd+1, bcd+b+d]
不难发现规律，列表前面加一个数计算出的
- 新分子等于旧分子乘以加入的数再加上旧分母。
- 新分母等于旧分子

"""
```python
class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        n = len(cont)
        A = cont[-1]
        B = 1
        for i in range(n-2, -1, -1):
            temp = B
            B = A
            A = A * cont[i] + temp
        return [A, B]
```
