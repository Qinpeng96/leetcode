"""
[146. LRU缓存机制](https://leetcode-cn.com/problems/lru-cache/)
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。

获取数据 get(key) - 如果关键字 (key) 存在于缓存中，则获取关键字的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字/值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。 

进阶:

你是否可以在 O(1) 时间复杂度内完成这两种操作？

 示例:

LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回  1
cache.put(3, 3);    // 该操作会使得关键字 2 作废
cache.get(2);       // 返回 -1 (未找到)
cache.put(4, 4);    // 该操作会使得关键字 1 作废
cache.get(1);       // 返回 -1 (未找到)
cache.get(3);       // 返回  3
cache.get(4);       // 返回  4
***

要让 put 和 get ⽅法的时间复杂度为 O(1)，我们可以总结出 cache 这个数据结构必要的条件：查找快，插⼊快，删除快，有顺序之分。

因为显然 cache 必须有顺序之分，以区分最近使⽤的和久未使⽤的数据；⽽且我们要在 cache 中查找键是否已存在；如果容量满了要删除最后⼀个数据；每次访问还要把数据插⼊到队头。
那么，什么数据结构同时符合上述条件呢？哈希表查找快，但是数据⽆固定顺序；链表有顺序之分，插⼊删除快，但是查找慢。所以结合⼀下，形成⼀种新的数据结构：哈希链表。
LRU 缓存算法的核⼼数据结构就是**哈希链表，双向链表和哈希表的结合体**。这个数据结构⻓这样：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200728121632854.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)
***
   #### 注意，这里插入尾部的时候需要注意操作顺序，顺序不对，功夫白费
   #### 先左pre,右next,插入进去。然后再左next,右pre连接。
   每次访问一个值，需要将这个值移动到尾部。使用双向链表的好处就是方便插入，删除。
 """
```python

class ListNode:#建立一个双向的链表
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        #建立两个新节点 head and tail
        self.head = ListNode()
        self.tail = ListNode()
        #初始化链表 head<->tail
        self.head.next = self.tail
        self.tail.pre = self.head

    def move_node_to_tail(self, key):
        #找到哈希键的节点,移除key连接左右
        node = self.hashmap[key]
        node.pre.next = node.next
        node.next.pre = node.pre
        #将node节点插入到最后，注意顺序
        node.pre = self.tail.pre
        node.next = self.tail
        self.tail.pre.next = node
        self.tail.pre = node 


    def get(self, key: int) -> int:
        if key in self.hashmap:#如果该值在字典中，则移动到最后一个
            self.move_node_to_tail(key)
        res = self.hashmap.get(key, -1)#不存在返回-1，存在返回value
        if res == -1:
            return res
        else:
            return res.value

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].value = value
            self.move_node_to_tail(key)
        else:#如果put的键值不在hashmap,则根据容量来看怎么加入
            if self.capacity == len(self.hashmap):#如果容量已满，删除最不常用的，即堆顶,在连接
                self.hashmap.pop(self.head.next.key)
                self.head.next = self.head.next.next
                self.head.next.pre = self.head
            #容量未满，插入到尾部
            new = ListNode(key, value)
            self.hashmap[key] = new
            #注意，这里插入尾部的时候需要注意操作顺序，顺序不对，功夫白费
            #先左pre,右next,插入进去。然后再左next,右pre连接
            new.pre = self.tail.pre
            new.next = self.tail
            self.tail.pre.next = new
            self.tail.pre = new

# SyntaxError: invalid character in identifier
#                         ^
#     def　move_node_to_tail(self, key):
# Line 13  (Solution.py)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```
