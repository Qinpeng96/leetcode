"""
[435. 无重叠区间](https://leetcode-cn.com/problems/non-overlapping-intervals/)
给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

注意:

可以认为区间的终点总是大于它的起点。
区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
示例 1:

输入: [ [1,2], [2,3], [3,4], [1,3] ]

输出: 1

解释: 移除 [1,3] 后，剩下的区间没有重叠。
示例 2:

输入: [ [1,2], [1,2], [1,2] ]

输出: 2

解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
示例 3:

输入: [ [1,2], [2,3] ]

输出: 0

解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
***
这道题是典型的时间排列问题，在规定的时间内怎么做到空闲的时间最少等等一系列问题。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200728095024655.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)
由于是单线程，所以只有上一个任务结束，下一个任务才能开始。所以要想下一个任务尽快开始，本次任务的结束时间就要早。于是，第一个任务就要选结束时间最少的。

对列表的矩阵内的每一行的第二个元素进行排序使用的是：
#
	intervals.sort(key = lambda x : x[1])
之后的元素如果开始时间在前一个时间的结束时间内，那么这个任务就不能完成。要寻找一个开始时间大于等于上一个任务结束时间的任务。	
	
"""
```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])#对每一时间段的结束时间进行排序
        res = []
        cnt = 0
        for item in intervals:
            if not res: 
                res.append(item)#列表为空，就加入元素
            else:
                if item[0] < res[-1][1]:#下一个的开始时间小于前一个的结束时间就删除
                    cnt += 1
                else:
                    res.append(item)#如果没有冲突就加入
        return cnt
```
