"""
[452. 用最少数量的箭引爆气球](https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/submissions/)
在二维空间中有许多球形的气球。对于每个气球，提供的输入是水平方向上，气球直径的开始和结束坐标。由于它是水平的，所以y坐标并不重要，
因此只要知道开始和结束的x坐标就足够了。开始坐标总是小于结束坐标。平面内最多存在104个气球。

一支弓箭可以沿着x轴从不同点完全垂直地射出。在坐标x处射出一支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend， 
且满足  xstart ≤ x ≤ xend，则该气球会被引爆。可以射出的弓箭的数量没有限制。 弓箭一旦被射出之后，可以无限地前进。我们想找到使得所有气球全部被引爆，所需的弓箭的最小数量。

Example:

输入:
[[10,16], [2,8], [1,6], [7,12]]

输出:
2

解释:
对于该样例，我们可以在x = 6（射爆[2,8],[1,6]两个气球）和 x = 11（射爆另外两个气球）。
***
这道题和上一道题的思路是类似的，只不过这里需要的是找到一个可以引爆的区域，看之后的气球是否在这个区域。[435. 无重叠区间](https://leetcode-cn.com/problems/non-overlapping-intervals/)

"""

```python
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:return 0
        points.sort(key = lambda x: x[1])
        print(points)
        res = []
        cnt = 0
        for item in points:
            if not res:
                res.append(item)
            else:
                if item[0] <= res[-1][1]:#如果一个本次的开始小于等于前一个的截至
                    res.append((item[0],res[-1][1]))#那么将这个可爆炸区域加入res
                else:
                    cnt += 1#如果不能引爆，则射击次数加一
                    res.append(item)
        return cnt+1
```
"""
上面使用了一个res来存储每一的可引爆区域或者是下一个不能引爆的气球区域，下面这种方法更加简洁。直接每次就不考虑引爆区域
，每次更新的是引爆区域的右边界，下一个气球的左边界和可引爆区域的右边界进行对比。
"""
```python
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:return 0
        points.sort(key = lambda x: x[1])
        x_end = points[0][1]#可引爆区域的右边界
        cnt = 0
        for item in points[1:]:
            if item[0] > x_end:#如果下一个气球的左边界大于可引爆区域的右边界，则射击次数加一
                cnt += 1
                x_end = item[1]
        return cnt+1
```
