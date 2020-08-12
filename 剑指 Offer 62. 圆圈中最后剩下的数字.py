"""
[剑指 Offer 62. 圆圈中最后剩下的数字](https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/)
0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。

例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。
示例 1：

输入: n = 5, m = 3
输出: 3
示例 2：

输入: n = 10, m = 17
输出: 2
 

限制：

1 <= n <= 10^5
1 <= m <= 10^6
***
约瑟夫环问题：
下面的题解来自:
[https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/solution/huan-ge-jiao-du-ju-li-jie-jue-yue-se-fu-huan-by-as/](https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/solution/huan-ge-jiao-du-ju-li-jie-jue-yue-se-fu-huan-by-as/)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200812211816852.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)
需要删除的次数等于 n-1 次
- f(n, m)表示还剩n个人， 每次间隔m,活下来的人的序号
- 递推公式 f(n, m) = [f(n-1, m) + m] % n
- 本次的序号右移m个之后，取上一次人数的余就是上一次能够活下来的编号
例如上面的例子，从f(7,3)转移到f(8,3),需要对索引G先进行补偿，补偿被杀死的C, 之后再向右位移3位，但是我们在位移的时候可能回溢出。所以只需要取模即可。

"""
```python
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:

        pos = 0#最后一次是在0索引
        for i in range(2, n+1):
            pos = (pos + m) % i
        return pos

```
