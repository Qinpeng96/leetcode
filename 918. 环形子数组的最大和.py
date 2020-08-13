"""
[918. 环形子数组的最大和](https://leetcode-cn.com/problems/maximum-sum-circular-subarray/)
给定一个由整数数组 A 表示的环形数组 C，求 C 的非空子数组的最大可能和。

在此处，环形数组意味着数组的末端将会与开头相连呈环状。（形式上，当0 <= i < A.length 时 C[i] = A[i]，而当 i >= 0 时 C[i+A.length] = C[i]）

此外，子数组最多只能包含固定缓冲区 A 中的每个元素一次。（形式上，对于子数组 C[i], C[i+1], ..., C[j]，不存在 i <= k1, k2 <= j 其中 k1 % A.length = k2 % A.length）

 

示例 1：

输入：[1,-2,3,-2]
输出：3
解释：从子数组 [3] 得到最大和 3
示例 2：

输入：[5,-3,5]
输出：10
解释：从子数组 [5,5] 得到最大和 5 + 5 = 10
示例 3：

输入：[3,-1,2,-1]
输出：4
解释：从子数组 [2,-1,3] 得到最大和 2 + (-1) + 3 = 4
示例 4：

输入：[3,-2,2,-3]
输出：3
解释：从子数组 [3] 和 [3,-2,2] 都可以得到最大和 3
示例 5：

输入：[-2,-3,-1]
输出：-1
解释：从子数组 [-1] 得到最大和 -1
***
![在这里插入图片描述](https://img-blog.csdnimg.cn/2020081323155387.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)
主要有两种情况，一种是最大值在中间不需要跨越边界，另一种就是最大值需要跨越边界，在两头。
- 最大值在内部的情况可以使用Kadane算法机型计算连续的最大值。
- 最大值在跨越边界的情况可以考虑裁剪中间一段，获得两头的值相加。即列表总和减去中间的连续最小值。方法计算也是和求连续最大值类似的。
- 最后还要考虑全部数值都为负数的情况。就直接返回最大值即可。

"""
 
```python
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        n = len(A)
        allsum = sum(A)
        B = A[:]
        maxval = A[0]
        minval = B[0]

        for i in range(1, n):#求一个连续最大值
            A[i] = max(A[i], A[i]+A[i-1])
            maxval = max(maxval, A[i])
        if maxval < 0: return max(B)#排除全部值都为负数的情况
        for i in range(1, n):#最一个连续最小值
            B[i] = min(B[i], B[i]+B[i-1])
            minval = min(minval, B[i])
        
        return max(maxval, allsum - minval)
```
