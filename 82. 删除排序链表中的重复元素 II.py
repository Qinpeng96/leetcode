"""
[82. 删除排序链表中的重复元素 II](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/)
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:

输入: 1->1->1->2->3
输出: 2->3
***
这道题和上一道题类似[83. 删除排序链表中的重复元素](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/)，
但是这里要求的是删除所有重复的链表节点，而上一题可以保留一个。
分析一下这道题，删除所有重复的节点，加入有两个节点被删除，例如[1,2,2,3]，那么在进行对比的时候需要保留一个节点在1的位置，
寻找重复的两个指针一个左边的在第一个2，右边的第一次在第二个2，第二次在3。这个时候我们需要把1->3连接起来。

通过上面的分析，知道了需要四个指针。

 1. 初始的头节点保存
 2. 写入输出链表需要一个
 3. 查找重复元素的时候需要两个

***
具体的流程如下：

 1. 初始就是设立头节点0，连接到head。设定Flag 标识位。
 2. 当head不为空的时候，取 post = head.next, 对两者进行对比，如果post不为空，且两者的数值相同，那么post就后移。
 3. 在找到不相同二点两个数之后，我们就还需要进一步判断，是连续两个不相同的数，还是中间有重复的数值，已经跳过的不相同的两个数。可以根据Flag来判断。
 4. 如果Flag为0，那么说明是两个连着的不相同的数，这个时候可以直接与node节点先连接，并且node节点后移一位。head也后移一位。
 5. 有重复的节点有点麻烦，首先分为6，7两种情况。
 6. 例如[1, 2, 2, 3, 4.......]重复的数字2可以删除，此时的 head = 2(第一个)； post = 3； Flag = 1； node = 1;我们需要把post连接到node后面，再更新node到后一位。
 7. 例如[1, 2, 2, 3, 3, 4,......]按照上述的head = 2(第一个)； post = 3； Flag = 1； node = 1;我们需要把post连接到node后面，再更新node到后一位。
    这个时候node已经连接上了3(第一个),但是之后还有个3与之重复。所以第6中，==我们不能再有重复(Flag == 1)，直接遇到两个不一样的值就更新node后移==，
    否则再遇到连续的重复组时，就会把有重复的数添加进去。
 8. 所以，在Flag == 1的情况下，我们只连接不一样的post值，但是我们不更新节点node后移。意思就是这个值先连接上，我待定加不加入（此时待定的数为下一轮的head）。
    如果之后没有与待定重复的数，那么下一轮不相等的时候我们在更新加入。如果下一轮中有和待定数重复的数，就会node接下一轮的不相等数post。

**注意**：为什么每次更新值在Flag = 0里面更新。但是Flag =1的时候还要加一个node.next = post，这里的post就是下一轮head, 下一轮如果可以加入，
也是加入的head, 即node.next = post，内的post。为什么看起来多此一举？
因为如果链表内的数字都非单存在，那么加入没有 node.next = post，我们最后返回链表还是原来的链表，没有该表。但是如果加上node.next = post，
此时post的值为空，因为所有都是非单的。那么在最后输出的时候才能得到正解。
"""
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node = ListNode(0)
        Flag = 0#设立标志位
        root = node
        node.next = head
        while head:
            post = head.next
            while post and head.val == post.val:
                Flag = 1
                post = post.next
            if not Flag:#没有重复的节点
                node.next = head#直接连接到node
                node = node.next#更新node的值，后移
                head = head.next#更新head为下一个位置
            else:#有重复的节点
                node.next = post##非常关键的一句
                head = post
                Flag = 0
        return root.next
              
```

下面是powcai大佬的两种解法，学习一下：
第一种是迭代法，使用快慢指针，快指针跳过重复，与后面的慢指针相连。
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        dummy = ListNode(-1000)
        dummy.next = head
        slow = dummy#初始为-1节点
        fast = dummy.next#初始为头节点
        while fast:#头节点不为空时
            if  fast.next and fast.next.val == fast.val:#下一个数存在且与当前值相同
                tmp = fast.val#缓存当前值
                while fast and tmp == fast.val:#找到一个不相等的值，赋给fast
                    fast = fast.next
            else:#两个数不相等或者fast的下一个节点为空时
                slow.next = fast#慢指针指向快指针
                slow = fast#慢 = 快，赋值
                fast = fast.next #快指针后移
        slow.next = fast#连接一个空节点
        return dummy.next

作者：powcai
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/solution/kuai-man-zhi-zhen-by-powcai-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
第二种是递归的方法：
注意递归的方式不同：
1.l两者值相同的时候，直接返回的 **递归函数**
2.两者的值不同的时候， 是**当前节点连接上 之后的递归函数返回值**

可以这么理解，有相同的数，之前的相同值都会被删除，直接看递归作用后面的数。但是当两数不一样的时候，
需要把当前值提出来，连接 递归后面的返回值。有点难理解~~~~
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:return head#链表为空，直接返回
        if head.next and head.val == head.next.val:#链表的下一个节点存在，且值和当前值一样
            while head.next != None and head.val == head.next.val:#找到一个不同的值
                head = head.next
            return self.deleteDuplicates(head.next)对不同的值之后的链表递归删除重复数字
        else:#链表节点为空，或者当前值和下一个值不用，直接递归下一个开始的链表
            head.next = self.deleteDuplicates(head.next)
        return head
        

作者：powcai
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/solution/kuai-man-zhi-zhen-by-powcai-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
