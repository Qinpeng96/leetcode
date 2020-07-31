"""
[354. 俄罗斯套娃信封问题](https://leetcode-cn.com/problems/russian-doll-envelopes/)
给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h) 出现。当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。

请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。

说明:
不允许旋转信封。

示例:

输入: envelopes = [[5,4],[6,4],[6,7],[2,3]]
输出: 3 
解释: 最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
***
这道题的思路就是首先对长度进行递增排序，在这个长度递增的情况下，我们取宽度的最长递增个数作为输出的长度。
但是注意：当有一些信封的长度相同的时候，我们需要对宽度进行降序排序，这样做的目的是，每个长度的信封，我们只取其中一个。
但是我们在取信封的时候，只看到信封的宽度信息，看到不到长度信息就在取最长递增宽度，所以如果我们对相同的长度信封的 宽度取一个降序排序，
那么每一个长的信封钟，我们就能取到最合适的哪一个（非最宽就好）。

但是这里开始我用的是dp数组，需要for循环两次，所以效率不高
"""
```python
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:return 0
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        n = len(envelopes)
        dp = [1]*n
        height = [item[1] for item in envelopes]#提出每个排序后的信封的宽度
        for i in range(n):#进行dp的最长递增个数的更新
            for j in range(i):
                if height[i] > height[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
```
"""
接下来使用的是二分法：
分析上面的最长递增序列个数，我们可以发现，是否可以维护一个num(包含）的一个最长递增的列表。

 1. 如果后续待加入的值比tail列表内的值都大， 那么说明可以加载到列表的末尾
 2. 如果后续待加入的值比列表钟的某一个值小，比其之前一个值大。那么我们可以进行替换。换成这个较小的值，方便以后有较大的值可以加入进行，维护一个最佳的递增列表。
 3. 所以在查找的时候，我们就可以使用二分查找，找到的索引为弹出的left.

具体的代码实现如下：
"""
```python
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:return 0
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        n = len(envelopes)
        tail = [1]*n
        height = [item[1] for item in envelopes]#提出每个排序后的信封的宽度

        #接下来使用二分查找进行最长递增宽度的寻找
        res = 0
        for num in height:
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                if num > tail[m]:
                    i = m + 1
                else:
                    j = m
            if j == res: res += 1#num比所有的tail内的数都大，于是需要增容
            tail[i] = num#假如增容，就是连接在最后；没有增容，就是替换成一个更小的num
        return res


```

