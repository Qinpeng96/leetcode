"""
[56. 合并区间](https://leetcode-cn.com/problems/merge-intervals/)
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
***
关键点在于首先需要对元素组的左边界进行排序。

 1. 首先对元素组的左边界进行排序
 2. 加入第一个元素组，之后的元素组与其相求并集
 3. 如果输出中的最后一个组的右边界大于待加入的元素组的左边界，那么说明有可能会加入，我们取这两个组中较大的右边界作为新的右边界。
 4. 如果输出中的最后一个元素组的右边界小于待加入的元素组的左边界，那么直接加入即可。

 ==本题的关键是对元素组的第一个元素进行排序==
 
"""
```python
#方式一, 
intervals = [value for index, value in sorted(enumerate(intervals), key = lambda intervals: intervals[1])]

#方式二
intervals.sort(key=lambda x: x[0])
```

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        n = len(intervals)
        intervals = [value for index, value in sorted(enumerate(intervals), key = lambda intervals: intervals[1])]#对组合的第一个数字排序
        out = []
        print(intervals)
        out.append(intervals[0])
        for i in range(1, n):#对之后的进行判断
            if out[-1][1] >= intervals[i][0] and out[-1][1] <= intervals[i][1]:
                temp = out.pop()
                out.append([temp[0],intervals[i][1]])#需要增大右区间
            elif out[-1][1] >= intervals[i][0] and out[-1][1] >= intervals[i][1]:
                continue#待加入的被包含了
            else:
                out.append(intervals[i])#没有交集，直接加入
        return out
```
***
大佬写的比较好的代码

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        intervals.sort()
        res = [intervals[0]]
        for x, y in intervals[1:]:
            if res[-1][1] < x:
                res.append([x, y])
            else:
                res[-1][1] = max(y, res[-1][1])
        return res

作者：powcai
链接：https://leetcode-cn.com/problems/merge-intervals/solution/pai-xu-by-powcai/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
