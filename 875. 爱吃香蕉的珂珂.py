"""
[875. 爱吃香蕉的珂珂](https://leetcode-cn.com/problems/koko-eating-bananas/)
珂珂喜欢吃香蕉。这里有 N 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 H 小时后回来。

珂珂可以决定她吃香蕉的速度 K （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 K 根。如果这堆香蕉少于 K 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。  

珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。

返回她可以在 H 小时内吃掉所有香蕉的最小速度 K（K 为整数）。

 

示例 1：

输入: piles = [3,6,7,11], H = 8
输出: 4
示例 2：

输入: piles = [30,11,23,4,20], H = 5
输出: 30
示例 3：

输入: piles = [30,11,23,4,20], H = 6
输出: 23
 

提示：

1 <= piles.length <= 10^4
piles.length <= H <= 10^9
1 <= piles[i] <= 10^9
***
这道题还是使用二分法。
首先找到二分法的上界和下界，可以直到上界就是列表中最大的那个数，下界设置为1。

- 注意是左闭右开，所以在取上界的right的时候加了一个一
- 在每次判断使用时间的时候，如果不能完全除尽，剩余的余数还需要加一个小时
- 最后有三种情况，cnt 等于，大于，小于 H
- 当cnt等于H的时候，我们不能立即输出mid,因为这里要找的是最小值，所以还需要寻找一个左边界。于是，right = mid, 寻找左边界。最后把三种情况合并成为两种。
"""
```python
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        left, right = 1, max(piles)+1
        while left < right:
            mid = (left + right) // 2
            cnt = 0
            for i in range(len(piles)):#计算需要的小时数
                if piles[i] > mid:
                    cnt += (piles[i] // mid)
                    if piles[i] % mid != 0:#有余数不能除尽，增加一个小时
                        cnt += 1
                else:#不足一个小时的量的，增加一个小时
                    cnt += 1
                    
           if cnt > H:#时间用的比较多，加大进食量
                left = mid + 1
            else:#时间用的少，可以减少进食量
                right = mid
        return left
```
