"""
[剑指 Offer 09. 用两个栈实现队列](https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/)
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

示例 1：

输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
示例 2：

输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
提示：

1 <= values <= 10000
最多会对 appendTail、deleteHead 进行 10000 次调
***
使用两个栈。一个专门用于添加数据，另一个专门用于作为删除头节点时候的临时中转站。
"""
```python
class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []


    def appendTail(self, value: int) -> None:
        self.stack1.append(value)


    def deleteHead(self) -> int:
        if not self.stack1:
            return -1

        while self.stack1:
            self.stack2.append(self.stack1.pop())

        res = self.stack2.pop()

        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return res

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
```
"""
***
大佬方法：每次入栈就只给A入栈，出栈从B出栈。
＃
	例如入栈123，A = [1,2,3],  B = [ ] ; 
	第一次出栈：B为空， A->B, A =[ ]; B = [3,2,1],  B 出栈1； B = [3,2]
	第二次出栈：B不为空，从B出栈；B= [3]
"""
```python
class CQueue:
    def __init__(self):
        self.A, self.B = [], []

    def appendTail(self, value: int) -> None:
        self.A.append(value)

    def deleteHead(self) -> int:
        if self.B: return self.B.pop()#出栈的时候首先从B出栈，因为B中的元数是倒序的，B为空才把A移动到B
        if not self.A: return -1
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()

作者：jyd
链接：https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/solution/mian-shi-ti-09-yong-liang-ge-zhan-shi-xian-dui-l-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
