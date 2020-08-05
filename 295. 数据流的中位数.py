"""
[295. 数据流的中位数](https://leetcode-cn.com/problems/find-median-from-data-stream/)
中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

例如，
[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例：

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
进阶:

如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？
***
这道题还是看的[weiwei大佬的解法](https://leetcode-cn.com/problems/find-median-from-data-stream/solution/you-xian-dui-lie-python-dai-ma-java-dai-ma-by-liwe/)

使用的堆的思想来进行排序任务，如果使用一个堆，那么每次都要遍历计算索引对应的值，weiwei大佬这里使用的是双堆。一个最大堆表示中位数左边的那部分，
一个最小堆：表示中位数右边的那部分。这样以来，最大堆和最小堆的堆顶都是很容易的取出来，并且根据总个数的奇偶性我们就可以再保证两堆个数相差最多为1的情况下，取的我们的中位数。

下面的图都是来自weiwei大佬：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200805142153325.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)
![在这里插入图片描述](https://img-blog.csdnimg.cn/2020080514222566.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)
怎么平衡两个堆的个数了？
- 每次加入堆的时候是加入到的最小堆
- 如果我们在每次加入数据到堆后，如果总的数据个数是奇数，那么我们就把最小堆内的这个数弹出，加入到最大堆
- 这样一来，要么两边的个数相等，要么是最大堆多一个数，多出来的那个数就是中位数。
- 注意：python内自带函数没有最大堆，只有最小堆。所以我们实现最大堆在传入参数的时候，只能传入一个元组，第一个值是负值（-num， num）这样的类型。
默认的最小堆根据第一个数字排序，是一个增序，取一个符号，对第二个数的排序就是递减排序，就是一个最大堆。


"""
```python
import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minheap = []
        self.maxheap = []
        self.count = 0  

    def addNum(self, num: int) -> None:
        self.count += 1
        heapq.heappush(self.maxheap, (-num,num))
        _, maxnum = heapq.heappop(self.maxheap)
        heapq.heappush(self.minheap, maxnum)
        if self.count & 1:#个数为奇数
            num = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, (-num,num))
        
    def findMedian(self) -> float:
        if self.count & 1:
            return self.maxheap[0][1]
        else:
            return (self.minheap[0] + self.maxheap[0][1])/2
        
作者：liweiwei1419
链接：https://leetcode-cn.com/problems/find-median-from-data-stream/solution/you-xian-dui-lie-python-dai-ma-java-dai-ma-by-liwe/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
```
最后载来看一看liweiwei大佬自己实现的python最大堆和最小堆，真的不得不佩服：

```python
class MaxHeap:
    def __init__(self, capacity):
        # 我们这个版本的实现中，0 号索引是不存数据的，这一点一定要注意
        # 因为数组从索引 1 开始存放数值
        # 所以开辟 capacity + 1 这么多大小的空间
        self.data = [None for _ in range(capacity + 1)]
        # 当前堆中存储的元素的个数
        self.count = 0
        # 堆中能够存储的元素的最大数量（为简化问题，不考虑动态扩展）
        self.capacity = capacity

    def size(self):
        """
        返回最大堆中的元素的个数
        :return:
        """
        return self.count

    def is_empty(self):
        """
        返回最大堆中的元素是否为空
        :return:
        """
        return self.count == 0

    def insert(self, item):
        if self.count + 1 > self.capacity:
            raise Exception('堆的容量不够了')
        self.count += 1
        self.data[self.count] = item
        # 考虑将它上移
        self.__swim(self.count)

    def __shift_up(self, k):
        # 有索引就要考虑索引越界的情况，已经在索引 1 的位置，就没有必要上移了
        while k > 1 and self.data[k // 2] < self.data[k]:
            self.data[k // 2], self.data[k] = self.data[k], self.data[k // 2]
            k //= 2

    def __swim(self, k):
        # 上浮，与父结点进行比较
        temp = self.data[k]
        # 有索引就要考虑索引越界的情况，已经在索引 1 的位置，就没有必要上移了
        while k > 1 and self.data[k // 2] < temp:
            self.data[k] = self.data[k // 2]
            k //= 2
        self.data[k] = temp

    def extract_max(self):
        if self.count == 0:
            raise Exception('堆里没有可以取出的元素')
        ret = self.data[1]
        self.data[1], self.data[self.count] = self.data[self.count], self.data[1]
        self.count -= 1
        self.__sink(1)
        return ret

    def __shift_down(self, k):
        # 只要有左右孩子，左右孩子只要比自己大，就交换
        while 2 * k <= self.count:
            # 如果这个元素有左边的孩子
            j = 2 * k
            # 如果有右边的孩子，大于左边的孩子，就好像左边的孩子不存在一样
            if j + 1 <= self.count and self.data[j + 1] > self.data[j]:
                j = j + 1
            if self.data[k] >= self.data[j]:
                break
            self.data[k], self.data[j] = self.data[j], self.data[k]
            k = j

    def __sink(self, k):
        # 下沉
        temp = self.data[k]
        # 只要它有孩子，注意，这里的等于号是十分关键的
        while 2 * k <= self.count:
            j = 2 * k
            # 如果它有右边的孩子，并且右边的孩子大于左边的孩子
            if j + 1 <= self.count and self.data[j + 1] > self.data[j]:
                # 右边的孩子胜出，此时可以认为没有左孩子
                j += 1
            # 如果当前的元素的值，比右边的孩子节点要大，则逐渐下落的过程到此结束
            if temp >= self.data[j]:
                break
            # 否则，交换位置，继续循环
            self.data[k] = self.data[j]
            k = j
        self.data[k] = temp


class MinHeap:

    # 把最大堆实现中不等号的方向反向就可以了

    def __init__(self, capacity):
        # 因为数组从索引 1 开始存放数值
        # 所以开辟 capacity + 1 这么多大小的空间
        self.data = [0 for _ in range(capacity + 1)]
        self.count = 0
        self.capacity = capacity

    def size(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def insert(self, item):
        if self.count + 1 > self.capacity:
            raise Exception('堆的容量不够了')
        self.count += 1
        self.data[self.count] = item
        self.__swim(self.count)

    def __swim(self, k):
        # 上浮，与父节点进行比较
        temp = self.data[k]
        while k > 1 and self.data[k // 2] > temp:
            self.data[k] = self.data[k // 2]
            k //= 2
        self.data[k] = temp

    def extract_min(self):
        if self.count == 0:
            raise Exception('堆里没有可以取出的元素')
        ret = self.data[1]
        self.data[1] = self.data[self.count]
        self.count -= 1
        self.__sink(1)
        return ret

    def __sink(self, k):
        # 下沉
        temp = self.data[k]
        while 2 * k <= self.count:
            j = 2 * k
            if j + 1 <= self.count and self.data[j + 1] < self.data[j]:
                j += 1
            if temp <= self.data[j]:
                break
            self.data[k] = self.data[j]
            k = j
        self.data[k] = temp


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # 如果测试用例的容量增加，下面 10000 这个数值请大家自行调整
        self.max_heap = MaxHeap(10000)
        self.min_heap = MinHeap(10000)

    def addNum(self, num: 'int') -> 'None':
        # 大顶堆先进一个元素
        self.max_heap.insert(num);
        # 然后从大顶堆里出一个元素到小顶堆
        self.min_heap.insert(self.max_heap.extract_max())
        if self.max_heap.size() < self.min_heap.size():
            # 如果大顶堆的元素少于小顶堆
            # 就要从小顶堆出一个元素到大顶堆
            self.max_heap.insert(self.min_heap.extract_min())

    def findMedian(self) -> 'float':
        if self.max_heap.size() == self.min_heap.size():
            return (self.max_heap.data[1] + self.min_heap.data[1]) / 2
        else:
            return self.max_heap.data[1]

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

作者：liweiwei1419
链接：https://leetcode-cn.com/problems/find-median-from-data-stream/solution/you-xian-dui-lie-python-dai-ma-java-dai-ma-by-liwe/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
