"""
[498. 对角线遍历](https://leetcode-cn.com/problems/diagonal-traverse/)
给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。

 

示例:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

输出:  [1,2,4,7,5,3,6,8,9]

解释:

 说明:

给定矩阵中的元素总数不会超过 100000 。
***
下面图源力扣官网解析：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200803111405409.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)


![在这里插入图片描述](https://img-blog.csdnimg.cn/20200803111412397.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)
由上面两幅图可以看出，每当在边界的时候，四个边界对应的情况不一样，并且还有两种向上可行和向下可行两种状态，一共就是有六种状态。
"""
```python
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        UP = 1
        DOWN = 0
        out = []
        i, j = 0, 0
        while 0 <= i < m and 0 <= j < n:
            if UP:#向上
                if 0 <= i-1 and j+1 < n:
                    out.append(matrix[i][j])
                    i = i - 1
                    j = j + 1
                elif i == 0 and j+1 < n:#向上的时候遇到顶部，转为向下
                    out.append(matrix[i][j])
                    j = j + 1
                    UP = 0
                    DOWN = 1
                elif i+1 < m and j == n-1:#向上的时候遇到右边界，转为向下
                    out.append(matrix[i][j])
                    i = i + 1
                    UP = 0
                    DOWN = 1
            if DOWN:#向下
                if i+1 < m and 0 <= j-1:
                    out.append(matrix[i][j])
                    i = i + 1
                    j = j - 1
                elif i+1 == m and  j+1 < n:#向下的时候遇到底部边界，转为向上
                    out.append(matrix[i][j])
                    j = j + 1
                    UP = 1
                    DOWN = 0
                elif i+1 < m and j == 0:#向下的时候遇到左边界，转为向上
                    out.append(matrix[i][j])
                    i = i + 1
                    UP = 1
                    DOWN = 0
            if i == m - 1 and j == n - 1:#最后一个值由于边界限制，那里都去不了，所以最后加上
                out.append(matrix[i][j])
                break
        return out
                
```
"""
下面是powcai大佬的思路：
由于斜对角线上面的元数的坐标横纵值相加是一定的，所以可以有多条斜的对角线值。
#
	[
	 [ 1, 2, 3 ],
	 [ 4, 5, 6 ],
	 [ 7, 8, 9 ]
	]
例如上面的斜对角线上的坐标值分别为 2； 3； 4； 5； 6五条，每组值加入的顺序也是从小到大的。
"""
```python
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        lookup = collections.defaultdict(list)
        row, col = len(matrix), len(matrix[0])

        for i in range(row):#建立斜对角线的值列表
            for j in range(col):
                lookup[j + i].append(matrix[i][j])
                
        res = []
        flag = True
        for k, v in sorted(lookup.items()):#对列表内的值排序后，依次翻转取出
            if flag:
                res.extend(v[::-1])
            else:
                res.extend(v)
            flag = not flag
        return res

作者：powcai
链接：https://leetcode-cn.com/problems/diagonal-traverse/solution/dui-xiang-xian-heng-lie-zuo-biao-zhi-he-xiang-deng/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
