"""
[1552. 两球之间的磁力](https://leetcode-cn.com/problems/magnetic-force-between-two-balls/)
题目：在代号为 C-137 的地球上，Rick 发现如果他将两个球放在他新发明的篮子里，它们之间会形成特殊形式的磁力。Rick 有 n 个空的篮子，第 i 个篮子的位置在 position[i] ，Morty 想把 m 个球放到这些篮子里，使得任意两球间 最小磁力 最大。已知两个球如果分别位于 x 和 y ，那么它们之间的磁力为 |x - y| 。给你一个整数数组 position 和一个整数 m ，请你返回最大化的最小磁力。
在代号为 C-137 的地球上，Rick 发现如果他将两个球放在他新发明的篮子里，它们之间会形成特殊形式的磁力。Rick 有 n 个空的篮子，第 i 个篮子的位置在 position[i] ，Morty 想把 m 个球放到这些篮子里，使得任意两球间 最小磁力 最大。

已知两个球如果分别位于 x 和 y ，那么它们之间的磁力为 |x - y| 。

给你一个整数数组 position 和一个整数 m ，请你返回最大化的最小磁力。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200818145524416.png#pic_center)
输入：position = [1,2,3,4,7], m = 3
输出：3
解释：将 3 个球分别放入位于 1，4 和 7 的三个篮子，两球间的磁力分别为 [3, 3, 6]。最小磁力为 3 。我们没办法让最小磁力大于 3 。
***
求最小值的最大值，这种问法大佬说就是二分。
- 首先确定二分的内容是什么？这里的二分内容是磁力。磁力的最大值就是两个端点间的距离，磁力的最小值就是两两篮子之间的最小距离。
- 怎么移动二分值，如果使用当前的mid二分值去篮子里面取值，可以得到的区间数量大于等于给出的(m-1)个区间数量。说明mid偏小。反之，如果得到的区间数量小于（m-1）个区间数量，那么说明二分之偏大。

代码：
"""
```python
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)
        left = min([position[i+1]-position[i] for i in range(n-1)])#取得间隔磁力的最大值，最小值
        right = position[-1]-position[0]
    
        def check(dis):
            i, j = 0, 0
            count = 0
            while j < n:#从左到右计算两两之间的长度间隔，如果有大于等于所取的dis, 并且个数为大于等于m-1个
                while j < n and position[j]-position[i]<dis:#
                    j += 1
                if j < n:
                    count += 1
                i = j
            return count >= m-1#因为m是篮球的个数，所以组成的区间间隔有m-1个
        
        while left <= right:#二分法找到合适的值，注意这里是闭区间
            dis = left + (right-left)//2
            if check(dis):
                left = dis+1
            else:
                right = dis-1
        return left-1
```
