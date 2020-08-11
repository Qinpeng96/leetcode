"""
[剑指 Offer 30. 包含min函数的栈](https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/)
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度]都是 O(1)。

 

示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.
 

提示：

各函数的调用总次数不超过 20000 次
 ***
 建立一个辅助栈，只有当每次待加入的元数小于辅助栈栈顶的元数的时候，才会加入辅助栈，否则辅助栈就复制加入一个自己栈顶的元数。维护一个当前栈的最小值。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200811095253609.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)
下面是自己用最小堆的方法，每次生成一个最小堆，不太行，耗时
"""
```python
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minheap = []
        self.queue = []
        self.reveser = []


    def push(self, x: int) -> None: 
        self.queue.append(x)

    def pop(self) -> None:
        self.queue.pop()

    def top(self) -> int:
        return self.queue[-1]


    def getMin(self) -> int:
        heap = self.queue[:]
        # print(heap)
        heapq.heapify(heap)
        return heap[0]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```
这是大佬的双栈思路，辅助栈保存当前的栈中最小值。
```python
class MinStack:

    # 辅助栈和数据栈同步
    # 思路简单不容易出错

    def __init__(self):
        # 数据栈
        self.data = []
        # 辅助栈
        self.helper = []

    def push(self, x):
        self.data.append(x)
        if len(self.helper) == 0 or x <= self.helper[-1]:
            self.helper.append(x)
        else:
            self.helper.append(self.helper[-1])

    def pop(self):
        if self.data:
            self.helper.pop()
            return self.data.pop()

    def top(self):
        if self.data:
            return self.data[-1]

    def getMin(self):
        if self.helper:
            return self.helper[-1]

作者：liweiwei1419
链接：https://leetcode-cn.com/problems/min-stack/solution/shi-yong-fu-zhu-zhan-tong-bu-he-bu-tong-bu-python-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
