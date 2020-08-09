[5484. 找出第 N 个二进制字符串中的第 K 位](https://leetcode-cn.com/problems/find-kth-bit-in-nth-binary-string/)
给你两个正整数 n 和 k，二进制字符串  Sn 的形成规则如下：

S1 = "0"
当 i > 1 时，Si = Si-1 + "1" + reverse(invert(Si-1))
其中 + 表示串联操作，reverse(x) 返回反转 x 后得到的字符串，而 invert(x) 则会翻转 x 中的每一位（0 变为 1，而 1 变为 0）

例如，符合上述描述的序列的前 4 个字符串依次是：

S1 = "0"
S2 = "011"
S3 = "0111001"
S4 = "011100110110001"
请你返回  Sn 的 第 k 位字符 ，题目数据保证 k 一定在 Sn 长度范围以内。
***
首先找规律：
第n层的第n+1个数为1，左边为上一层的字串，右边为上一层的字串的取反的逆。
可以根据上述的规律找到对应元数之间的关系。

例如：
n = 3, k = 7，由于7大于中间的数4，所以是由上一层取反的逆而得到的。 
k - n - 1 =  3 上一层为 n = 2, 011,所以由上一层的第一个取反得到。具体的转换关系：
- 如果k刚好在当前层中间，直接返回1
- 如果k在在当前层左边递归， solve(n-1, k); 因为 k的长度在下一层内
- 如果k在当前层的右边，递归，slove(n-1, 2**n- k) ^ 1,k值大于上一层，而且还要翻转一下。最后和1取异或，0变1，1变0


```python
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # num = 2**n -1#31
        # if k == (num-1)//2 + 1:return 1
        # elif k <= (num-1)//2:
        def solve(n, k):
            if n == 1: return 0
            num = 2**n - 1
            if k == (num-1)//2+1:#等于中间，直接返回
                return 1
            elif k <= (num-1)//2:#k在当前层的左边
                return solve(n-1,k)
            else:#k在当前层的右边
                return 1 if not solve(n-1, 2**n -k) else 0
                
        return str(solve(n,k))                
```

