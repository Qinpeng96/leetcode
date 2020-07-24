"""
哈希表是一种使用哈希函数组织数据，以支持快速插入和搜索的数据结构。


作者：LeetCode
链接：https://leetcode-cn.com/problems/design-hashset/solution/she-ji-ha-xi-ji-he-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



有两种不同类型的哈希表：哈希集合和哈希映射。
#
	哈希集合是集合数据结构的实现之一，用于存储非重复值。
	哈希映射是映射 数据结构的实现之一，用于存储(key, value)键值对。
在标准模板库的帮助下，哈希表是易于使用的。大多数常见语言（如Java，C ++ 和 Python）都支持哈希集合和哈希映射。

#### 哈希表的原理
哈希表的关键思想是使用哈希函数将**键映射到存储桶**。更确切地说，
#
	当我们插入一个新的键时，哈希函数将决定该键应该分配到哪个桶中，并将该键存储在相应的桶中；
	当我们想要搜索一个键时，哈希表将使用相同的哈希函数来查找对应的桶，并只在特定的桶中进行搜索。
	 

##### 1. 哈希函数
哈希函数是哈希表中最重要的组件，该哈希表用于将键映射到特定的桶。在上一篇文章中的示例中，我们使用 y = x % 5 作为散列函数，其中 x 是键值，y 是分配的桶的索引。

 **散列函数**将取决于键值的范围和桶的数量。
下面是一些哈希函数的示例：


![在这里插入图片描述](https://img-blog.csdnimg.cn/20200724115619854.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)

哈希函数的设计是一个开放的问题。其思想是尽可能将键分配到桶中，理想情况下，完美的哈希函数将是键和桶之间的一对一映射。然而，在大多数情况下，哈希函数并不完美，它需要在桶的数量和桶的容量之间进行权衡。

#### 2. 冲突解决
理想情况下，如果我们的哈希函数是完美的一对一映射，我们将不需要处理冲突。不幸的是，在大多数情况下，冲突几乎是不可避免的。例如，在我们之前的哈希函数（y  =  x ％ 5）中，1987 和 2 都分配给了桶 2，这是一个冲突。

冲突解决算法应该解决以下几个问题：
**1.如何组织在同一个桶中的值？
2.如果为同一个桶分配了太多的值，该怎么办？
3.如何在特定的桶中搜索目标值？
4.根据我们的哈希函数，这些问题与桶的容量和可能映射到同一个桶的键的数目有关。**

让我们假设存储最大键数的桶有 N 个键。

通常，如果 N 是常数且很小，我们可以简单地使用一个数组将键存储在同一个桶中。如果 N 是可变的或很大，我们可能需要使用高度平衡的二叉树来代替.。
***
#### HashSet 数据结构

为了实现 HashSet 数据结构，有两个关键的问题，即哈希函数和冲突处理。

**哈希函数：目的是分配一个地址存储值。理想情况下，每个值都应该有一个对应唯一的散列值。
冲突处理：哈希函数的本质就是从 A 映射到 B。但是多个 A 值可能映射到相同的 B。这就是碰撞。因此，我们需要有对应的策略来解决碰撞。总的来说，有以下几种策略解决冲突：
单独链接法：对于相同的散列值，我们将它们放到一个桶中，每个桶是相互独立的。
开放地址法：每当有碰撞， 则根据我们探查的策略找到一个空的槽为止。
双散列法：使用两个哈希函数计算散列值，选择碰撞更少的地址。**

#### 单独链接法
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200724130435587.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)

##### 使用二叉搜索树作为桶
在上述的方法中，有一个缺点，我们需要扫描整个桶才能验证一个值是否已经在桶中（即查找操作）。

我们可以将桶作为一个排序列表，可以使用二分搜索使查找操作的时间复杂度是 \mathcal{O}(\log{N})O(logN)，优于 上面方法中的 \mathcal{O}({N})O(N)。

另一方面，如果使用排序列表等连续空间的数组来实现，则会产生线性时间复杂度的更新操作，因此需要其他的方式。

有数据结构具有 \mathcal{O}(\log{N})O(logN) 时间复杂度的查找，删除，插入操作吗？

当然有，就是二叉搜索树。二叉搜索树的特性使得我们能够优化时间复杂度。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200724131057798.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)
***
[705. 设计哈希集合](https://leetcode-cn.com/problems/design-hashset/)
不使用任何内建的哈希表库设计一个哈希集合

具体地说，你的设计应该包含以下的功能

add(value)：向哈希集合中插入一个值。
contains(value) ：返回哈希集合中是否存在这个值。
remove(value)：将给定值从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。

示例:

MyHashSet hashSet = new MyHashSet();
hashSet.add(1);         
hashSet.add(2);         
hashSet.contains(1);    // 返回 true
hashSet.contains(3);    // 返回 false (未找到)
hashSet.add(2);          
hashSet.contains(2);    // 返回 true
hashSet.remove(2);          
hashSet.contains(2);    // 返回  false (已经被删除)

注意：

所有的值都在 [0, 1000000]的范围内。
操作的总数目在[1, 10000]范围内。
不要使用内建的哈希集合库。
***
具体的程序如下：
1.首先是要建立一个链表bucket链，有多少个hash长度就建立多少个。
2.我们在插入，删除，验证存在操作的时候，首先要确定是在哪一个序列的hash buckect
"""



```python
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyRange = 769#设定hash长度
        self.bucketArray = [Bucket() for i in range(self.keyRange)]#建立一个bucket链

    def _hash(self, key):
        return key % self.keyRange

    def add(self, key: int) -> None:#插入
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].insert(key)

        

    def remove(self, key: int) -> None:#删除一个数值
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].delete(key)
        

    def contains(self, key: int) -> bool:#是否存在
        """
        Returns true if this set contains the specified element
        """
        bucketIndex = self._hash(key)
        return self.bucketArray[bucketIndex].exists(key)
        
class Node:#创建节点类
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode

class Bucket:
    def __init__(self):
        self.head = Node(0)
    
    def exists(self, value):#判断一个值是否存在
        cur = self.head.next#首先得到起始节点
        while cur is not None:#如果节点后面一直有值，就一直后移判断
            if cur.value == value:
                return True
            cur = cur.next
        return False
    
    def insert(self, newValue):
        if not self.exists(newValue):#如果待插入的值不存在，即可以插入
            newNode = Node(newValue,self.head.next)
            self.head.next = newNode
    
    def delete(self, value):#删除节点
        prev = self.head#需要提前设置一个头节点
        curv = self.head.next
        while curv is not None:
            if curv.value == value:
                prev.next = curv.next
                return 
            prev = curv
            curv = curv.next
    

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
```

使用二叉搜索树作为容器的方法还没看：

```python
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyRange = 769
        self.bucketArray = [Bucket() for i in range(self.keyRange)]

    def _hash(self, key) -> int:
        return key % self.keyRange

    def add(self, key: int) -> None:
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].insert(key)

    def remove(self, key: int) -> None:
        """
        :type key: int
        :rtype: None
        """
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].delete(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        bucketIndex = self._hash(key)
        return self.bucketArray[bucketIndex].exists(key)

class Bucket:
    def __init__(self):
        self.tree = BSTree()

    def insert(self, value):
        self.tree.root = self.tree.insertIntoBST(self.tree.root, value)

    def delete(self, value):
        self.tree.root = self.tree.deleteNode(self.tree.root, value)

    def exists(self, value):
        return (self.tree.searchBST(self.tree.root, value) is not None)

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class BSTree:
    def __init__(self):
        self.root = None

    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None or val == root.val:
            return root

        return self.searchBST(root.left, val) if val < root.val \
            else self.searchBST(root.right, val)

    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        if val > root.val:
            # insert into the right subtree
            root.right = self.insertIntoBST(root.right, val)
        elif val == root.val:
            return root
        else:
            # insert into the left subtree
            root.left = self.insertIntoBST(root.left, val)
        return root

    def successor(self, root):
        """
        One step right and then always left
        """
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def predecessor(self, root):
        """
        One step left and then always right
        """
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        # delete from the right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # delete from the left subtree
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # delete the current node
        else:
            # the node is a leaf
            if not (root.left or root.right):
                root = None
            # the node is not a leaf and has a right child
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            # the node is not a leaf, has no right child, and has a left child
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)

        return root

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

作者：LeetCode
链接：https://leetcode-cn.com/problems/design-hashset/solution/she-ji-ha-xi-ji-he-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
