"""
[372. 超级次方](https://leetcode-cn.com/problems/super-pow/)
你的任务是计算 ab 对 1337 取模，a 是一个正整数，b 是一个非常大的正整数且会以数组形式给出。

示例 1:

输入: a = 2, b = [3]
输出: 8
示例 2:

输入: a = 2, b = [1,0]
输出: 1024
- (a + b) % p = (a % p + b % p) % p （1）

- (a - b) % p = (a % p - b % p ) % p （2）

- (a * b) % p = (a % p * b % p) % p （3）
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200818203845639.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)
代码：
"""
```python
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if not b:return 1
        res = b.pop()
        return (((a**res)%1337)*(self.superPow(a, b)**10%1337))%1337
```
