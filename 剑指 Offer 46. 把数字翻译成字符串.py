"""
[剑指 Offer 46. 把数字翻译成字符串](https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/)
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可
能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。


示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
***
使用回溯算法，每次需要判断下当前字符串的合法性。
- 长度为1的时候，什么都可以加入
- 长度为2的时候，首字符不能为0， 并且字符的大小在 '0' ~ '25'内。
"""
```python
class Solution:
    def translateNum(self, num: int) -> int:
        s = str(num)
        out = 0
        print(s)        
        def backtrack(s):
            nonlocal out
            if not s:
                out += 1
                return 
            for i in range(1, len(s)+1):
                if (len(s[:i])  == 2 and s[0] != '0' and '0' < s[:i] <= '25') or len(s[:i]) == 1:
                    backtrack(s[i:])
            return out
                    
        return backtrack(s)
```
***
大佬们都说这是一道动态规划的题目，仔细以看好像还真是。 =- =
下面是[K神的思路做法](https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/solution/mian-shi-ti-46-ba-shu-zi-fan-yi-cheng-zi-fu-chua-6/)：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200810191041732.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)
动态转移方程为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/2020081019134181.png#pic_center)

```python
class Solution:
    def translateNum(self, num: int) -> int:
        s = str(num)
        n = len(s)
        dp = [1]*(n+1)

        for i in range(2,n+1):
            if '10'<= s[i-2:i] <= '25':
                dp[i] = dp[i-1]+dp[i-2]
            else:
                dp[i] = dp[i-1]
            print(dp)

        return dp[-1]
```
由于只需要保存前面两个状态，所以还可以进一步压缩空间。

```python
class Solution:
    def translateNum(self, num: int) -> int:
        s = str(num)
        a = b = 1
        for i in range(2, len(s) + 1):
            tmp = s[i - 2:i]
            c = a + b if "10" <= tmp <= "25" else a
            b = a
            a = c
        return a

作者：jyd
链接：https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/solution/mian-shi-ti-46-ba-shu-zi-fan-yi-cheng-zi-fu-chua-6/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
