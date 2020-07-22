"""
[90. 子集 II](https://leetcode-cn.com/problems/subsets-ii/)
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
***
这道题也是回溯算法里面的一个经典例子，但是就是要出去重，后一个元数在与前一个元数相同的时候，我们就可以跳过这次递归。

所以这里重要的就是去重的条件判断

 1. nums[ j ] == nums[ j - 1 ]
 2. j 要大于当前的起始索引值， 例如这里就是 j > index
 3. 由于每个元素只能使用一次，我们每次的索引值都加一
"""
```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        n = len(nums)
        #参数含义分别为
        # index :每次回溯的开始位置，因为不能重复使用
        # cnt：计数，每一加一个数，就增加一.为下一次选择列表取数的起始位置
        # out: 缓存的输出列表
        # i: 每次需要的列表输出长度

        def backtrack(index, cnt, out, i):
            if cnt == i:#达到本次需要的输出长度
                output.append(out[:])
                return
            
            for j in range(index, n):
                if j > index and nums[j] == nums[j-1]:#去重操作，注意是 j > index
                    continue
                backtrack(j+1, cnt+1, out+[nums[j]], i)


        for i in range(n+1):
            backtrack(0, 0, [], i)
            
        return output

#powcai大佬的方法,直接超过90%多，秀啊
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        def helper(idx, tmp):#回溯函数定义，索引值，输出值
            res.append(tmp)
            for i in range(idx, n):#索引值之前进行循环，得到的列表长度是倒过来的，很巧妙
                if i > idx and nums[i] == nums[i-1]:
                    continue
                helper(i+1, tmp + [nums[i]])
        helper(0, [])
        return res

```


