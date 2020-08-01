"""
[1011. 在 D 天内送达包裹的能力](https://leetcode-cn.com/problems/capacity-to-ship-packages-within-d-days/)
传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。

传送带上的第 i 个包裹的重量为 weights[i]。每一天，我们都会按给出重量的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。

返回能在 D 天内将传送带上的所有包裹送达的船的最低运载能力。

 

示例 1：

输入：weights = [1,2,3,4,5,6,7,8,9,10], D = 5
输出：15
解释：
船舶最低载重 15 就能够在 5 天内送达所有包裹，如下所示：
第 1 天：1, 2, 3, 4, 5
第 2 天：6, 7
第 3 天：8
第 4 天：9
第 5 天：10

请注意，货物必须按照给定的顺序装运，因此使用载重能力为 14 的船舶并将包装分成 (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) 是不允许的。 
示例 2：

输入：weights = [3,2,2,4,1,4], D = 3
输出：6
解释：
船舶最低载重 6 就能够在 3 天内送达所有包裹，如下所示：
第 1 天：3, 2
第 2 天：2, 4
第 3 天：1, 4
示例 3：

输入：weights = [1,2,3,1,1], D = 4
输出：3
解释：
第 1 天：1
第 2 天：2
第 3 天：3
第 4 天：1, 1
 

提示：

1 <= D <= weights.length <= 50000
1 <= weights[i] <= 500
***
这道题是采用的二分法，首先二分法就是要确定上下界。可以分析得到最小的界限就是货物的单个最大重量，最大的边界就是货物的总重量。所以这样算出来的运算天数在 [1, i ]天，i 为货物的件数。

使用二分法，计算一个mid运载能力，然后根据运载能力算出总共需要的天数。
 -  如果需要的天数大于D, 那么此时说明我们的mid运载能力小了，应该增大运载能力，即 left = mid + 1。
 - 如果需要的天数小于等于D, 说明此时的运载能力超过了或者刚刚好，这时候我们应该缩小运载能力，即right= mid + 1。
***
在固定运载能力计算需要天数的时候有几种情况：（本次货物重量weight[; 之前的没有运走的为 res）
 - res == 0, weight == mid,刚好没有剩余，cnt加一
 - res != 0, weight == mid,这个时候只能把之前的作为一批，本次的做一批，算成两批，cnt += 2
 - weight < mid, res + weight < mid, 说明还可以继续加，cnt不变
 - weight < mid, res + weight == mid, 刚好算一批，cnt加一，记得要res 清零
 - weight  < mid, res + weight > mid, 之前的算作一批，本次的留作res在计算，cnt 加一
 - weight  > mid: 这个不可能出现，因为我们定上下界的时候已经定好了，肯定是单个的可以算作一批的
- 最后循环完之后，如果res != 0，说明还有一些剩余的，这时候我们cnt加一，再送走一次。
"""

```python
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        n = len(weights)
        left, right = max(weights), sum(weights)#计算上下界
        while left < right:#开始进行二分查找
            mid = (left + right) // 2
            cnt, res = 0, 0
            for i in range(n):#每次都对货物进行一次遍历，找出需要的天数
                if weights[i] == mid and res != 0:
                    cnt += 2
                    res = 0
                    continue
                elif weights[i] == mid and res == 0:
                    cnt += 1
                    continue
                elif weights[i] < mid and res + weights[i] < mid:
                    res += weights[i]
                    continue
                elif weights[i] < mid and res + weights[i] == mid:
                    cnt += 1
                    res = 0
                    continue
                elif weights[i] < mid and res + weights[i] > mid:
                    cnt += 1
                    res = weights[i]
                    continue
                #elif weights[i] > mid:
                    #cnt = float('inf')
            if res != 0: cnt += 1#最后一天还有剩余，再送一个批次
            
            if cnt > D:#天数过多，增加运载能力
                left = mid + 1
            else:#天数刚好，或者过少，减少运载能力
                right = mid
        return left
                
```
