"""
[973. 最接近原点的 K 个点](https://leetcode-cn.com/problems/k-closest-points-to-origin/)
我们有一个由平面上的点组成的列表 points。需要从中找出 K 个距离原点 (0, 0) 最近的点。

（这里，平面上两点之间的距离是欧几里德距离。）

你可以按任何顺序返回答案。除了点坐标的顺序之外，答案确保是唯一的。

 

示例 1：

输入：points = [[1,3],[-2,2]], K = 1
输出：[[-2,2]]
解释： 
(1, 3) 和原点之间的距离为 sqrt(10)，
(-2, 2) 和原点之间的距离为 sqrt(8)，
由于 sqrt(8) < sqrt(10)，(-2, 2) 离原点更近。
我们只需要距离原点最近的 K = 1 个点，所以答案就是 [[-2,2]]。
示例 2：

输入：points = [[3,3],[5,-1],[-2,4]], K = 2
输出：[[3,3],[-2,4]]
（答案 [[-2,4],[3,3]] 也会被接受。）
 

提示：

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
***


使用字典记录每一个点的距离，在对每一个点的距离从小到大进行排序，取前K个点的坐标。
"""
```python
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dic = {}
        out = []
        cnt = 0
        for point in points:
            if (point[0],point[1]) not in dic:
                dic[(point[0],point[1])] = point[0]**2 + point[1]**2
        dic = sorted(dic.items(), key = lambda x: x[1])#对字典内的点的距离进行排序
        # print(dic)
        for c in dic:#取前K个点的坐标
            out.append(c[0])
            cnt += 1
            if cnt == K:
                return out
```
"""
****
这道题还可以使用最小堆来进行维护，容量为K。
由于python只有最小堆，并且每次pop的时候，都是pop的最小值，本题要求的就是最小值。
查阅资料后发现，我们要比较的数（距离）都是正整数，所以我们在比较排序的时候就把其当作负值来判断。这样每次pop的时候就会弹出那些值最大的索引。
"""
```python
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        out = []
        for point in points:
            heapq.heappush(heap, (-(point[0]**2+point[1]**2),(point[0],point[1])))
            if len(heap) > K:
                heapq.heappop(heap)
        # print(heap)
        for c in heap:
            out.append(c[1])
        return out
```
