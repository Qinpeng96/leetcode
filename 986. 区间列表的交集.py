"""
[986. 区间列表的交集](https://leetcode-cn.com/problems/interval-list-intersections/)
给定两个由一些 闭区间 组成的列表，每个区间列表都是成对不相交的，并且已经排序。

返回这两个区间列表的交集。

（形式上，闭区间 [a, b]（其中 a <= b）表示实数 x 的集合，而 a <= x <= b。两个闭区间的交集是一组实数，要么为空集，要么为闭区间。例如，[1, 3] 和 [2, 4] 的交集为 [2, 3]。）


输入：A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
输出：[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
***
首先是排除两种没有交集的情况
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200731130902490.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)
接下来就是四种有并集的情况：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200731131020220.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)
我们可以发现求并集的时候，并集的区间表达式左边界为两者的左边界求max,右边界为两者的右边界求min。
除此之外，我们还发现有可能一段A，会与多段B有并集。所以还要考虑一段对应多段的情况。
"""
```python
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        m = len(A)
        n = len(B)
        res = []
        i, j = 0, 0
        while i < m and j < n:
            if not (A[i][1] < B[j][0] or A[i][0] > B[j][1]): #有交集，求max，min
                res.append([max(A[i][0], B[j][0]), min(A[i][1], B[j][1])])
            if i+1 < m and A[i+1][0] <= B[j][1]:#下一个的A与本次B有并
                i += 1
            elif j+1 < n and B[j+1][0] <= A[i][1]:#下一个B与本次A有并
                j += 1
            else:
                i += 1
                j += 1
        return res
```
