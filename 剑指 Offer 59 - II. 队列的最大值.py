"""
[剑指 Offer 59 - II. 队列的最大值](https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/)
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。

若队列为空，pop_front 和 max_value 需要返回 -1

示例 1：

输入: 
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]
示例 2：

输入: 
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]
 
限制：

1 <= push_back,pop_front,max_value的总操作数 <= 10000
1 <= value <= 10^5
***
这道题的思路和上一道题[剑指 Offer 59 - I. 滑动窗口的最大值](https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/)思路是类似的，都是维护一个递减的队列。这里也是一样，只需要建立一个双向队列来存储当前字段的一个递减的列表。

有以下几种情况：
- 由于我们维护的是一个递减的队列，如果待加入的数大于我们辅助队列的最后一个值，那么我们就要pop()队列的最后一个值
- 在主队列pop的时候，如果此时popleft()的是当前的队列内的最大值，即辅助队列的第一个元数，那么我们的辅助队列的第一个元数也应该跟着popleft()。
- 如果此时主队列pop的不是当前辅助队列的最大元数，那么辅助队列就不需要popleft(),因为其还是剩余的队列内的最大值。

"""
```python
class MaxQueue:

    def __init__(self):
        self.queue = collections.deque()
        self.maxv = collections.deque()

    def max_value(self) -> int:
        if self.maxv:
            return self.maxv[0]
        else:
            return -1

    def push_back(self, value: int) -> None:
        self.queue.append(value)
        while self.maxv and self.maxv[-1] < value:#辅助队列维护一个递减队列
            self.maxv.pop()
        self.maxv.append(value)

    def pop_front(self) -> int:
        if self.queue:
            temp = self.queue.popleft()
            if temp == self.maxv[0]:#当主队列弹出的是辅助队列内部的最大值的时候，辅助队列才popleft()
                self.maxv.popleft()
            return temp
        else:
            return -1
        
# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
```
