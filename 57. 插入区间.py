"""
[57. 插入区间](https://leetcode-cn.com/problems/insert-interval/)
给出一个无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

示例 1:

输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
输出: [[1,5],[6,9]]
示例 2:

输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出: [[1,2],[3,10],[12,16]]
解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
***
这道题就是上一道题目加一个插入操作而已，就不细说了。看详解看[56. 合并区间](https://leetcode-cn.com/problems/merge-intervals/)
"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)+1
        intervals.append(newInterval)
        intervals.sort(key = lambda x: x[0])
        out = [intervals[0]]

        for x, y in intervals[1:]:
            if out[-1][1] >= x:
                out[-1][1] = max(out[-1][1], y)
            else:
                out.append([x, y])
        return out

