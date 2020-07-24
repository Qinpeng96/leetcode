"""
[216. 组合总和 III](https://leetcode-cn.com/problems/combination-sum-iii/)
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：

所有数字都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: k = 3, n = 7
输出: [[1,2,4]]
示例 2:

输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]
***
使用回溯方法：
1.确定回溯的弹出条件，列表的值相等，数量也为k
2.回溯中的循环，由于不能有重复，需要一个索引参数index。
3.每次改变的右索引值index, 临时输出res, 剩余数量num， 计数器cnt
"""

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        out = []
        #index：每次开始索引，不能重复
        #res：临时输出
        #num: n - 之前数字相加的总和 得到的剩余值
        #cnt：已经使用了个数

        def backtrack(index, res, num, cnt):
            if cnt == k and num == 0:
                out.append(res[:])
    
            for i in range(index, 10):
                if i <= num:#当之后待加入的数字比需要的数字大，直接跳过，相当于剪枝
                    res.append(i)
                    backtrack(i+1, res, num-i, cnt+1)
                    res.pop()
        backtrack(1, [], n, 0)
        return out
