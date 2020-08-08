"""
[927. 三等分](https://leetcode-cn.com/problems/three-equal-parts/)
给定一个由 0 和 1 组成的数组 A，将数组分成 3 个非空的部分，使得所有这些部分表示相同的二进制值。

如果可以做到，请返回任何 [i, j]，其中 i+1 < j，这样一来：

A[0], A[1], ..., A[i] 组成第一部分；
A[i+1], A[i+2], ..., A[j-1] 作为第二部分；
A[j], A[j+1], ..., A[A.length - 1] 是第三部分。
这三个部分所表示的二进制值相等。
如果无法做到，就返回 [-1, -1]。

注意，在考虑每个部分所表示的二进制时，应当将其看作一个整体。例如，[1,1,0] 表示十进制中的 6，而不会是 3。此外，前导零也是被允许的，所以 [0,1,1] 和 [1,1] 表示相同的值。

 

示例 1：

输入：[1,0,1,0,1]
输出：[0,3]
示例 2：

输出：[1,1,0,1,1]
输出：[-1,-1]
 

提示：

3 <= A.length <= 30000
A[i] == 0 或 A[i] == 1
 ***
超时的心累=-=
简单说下过程：
- 首先判断列表中1的个数，如果不是三的倍数，返回假
- 对1的个数除以3，得到的数值将是每一组所含有的1的个数cnt
- 计算A的长度，方便之后的返回索引
- 从左向右计算cnt个1在那一个位置,从右往左也计算cnt个1在哪个位置，分别命名为 j , i
- 对s1,s2,s3进行初步的判断，如果有相等，可以直接赋值out
- 接下来就是右移s1的右指针，左移s2的左指针。
- 最后输出out

"""
```python
class Solution:
    def threeEqualParts(self, A: List[int]) -> List[int]:
        num = sum(A)
        if num % 3 != 0: return[-1,-1]
        if num == 0: return [0,len(A)-1]
        n = len(A)
        A = [str(i) for i in A]

		#从左向右计算cnt个1在哪个索引
        cnt = num // 3
        i = n
        while cnt and i > 0:
            if A[i-1] == '1':
                cnt -= 1
            i -= 1
            
		#从右往左计算cnt个1在哪个索引
        cnt = num // 3
        j = 0
        while cnt and j < n:
            if A[j] == '1':
                cnt -= 1
            j += 1
		#初始化输出，三个列表的数值，去除左0
        out = [-1,-1]
        s1 = ''.join(A[:j]).lstrip('0')
        s2 = ''.join(A[j:i]).lstrip('0')
        s3 = ''.join(A[i:]).lstrip('0')
        #对三个列表值进行初步的判断，减少之后的运算
        if s1 == s2 == s3: return [j-1, i]
        if s1 == s3: out[0] = j-1
        if s2 == s3: out[1] = i
        #s1的指针右移，如果不是1，则加入s1，s1 == s3，或者右指针为1结束。如果找到s1 ==s3，直接返回
        while A[j] != '1' and s1 < s3:
            s1 += ('0')
            if s1 == s3:
                out[0] = j
                break
            j += 1 
		#s2的右指针左移，如果不是1，则s2减去末尾的值，同理
        while A[i-1] != '1' and s2 > s3:
            s2 = s2[:-1]
            if s2 == s3:
                out[1] = i-1
                break
            i -= 1
		#如果out中还有坐标为-1,说明某两个不相等
        if -1 in out:
            return [-1,-1]
        else:
            return out
```
