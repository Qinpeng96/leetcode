"""
[147. 对链表进行插入排序](https://leetcode-cn.com/problems/insertion-sort-list/)
对链表进行插入排序。


插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。

 

插入排序算法：

插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
重复直到所有输入数据插入完为止。
 

示例 1：

输入: 4->2->1->3
输出: 1->2->3->4
示例 2：

输入: -1->5->3->4->0
输出: -1->0->3->4->5
***
主要是插入排序：
从左到右遍历节点，依次从链表头开始比较，找到一个合适的位置插入进去。
- 注意：如果需要比较的节点比前一个节点大，那么就不需要移动比较。跳过
- 如果需比较的节点node在链头，就只需要比较一个链头
- 如果待插入的位置在中间，我们需要比较前后两个节点值，如果node的值在两者中间，那么就插入
- 如果待插入的值比前后pre,post都大的话，那么pre,post后移一位。
"""

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if (not head) or (not head.next) : return head
        left = head
        while left.next:#对第二个开始的数进行判断
            node = left.next#取要判断的数为node
            if node.val >= left.val:#如果node值比大于等于前一个值，那么就不变，指针右移。
                left = left.next
                continue
            left.next = node.next#如果node值比前一个值小，说明需要排序，首先断开node节点。
			#设定左右比较值，pre & post
            pre = head
            post = head.next
            #把node值与pre和post进行比较，主要有三种情况。
            while pre != left.next:
                if node.val <= pre.val:
                    node.next = pre
                    head = node
                    break
                elif pre.val < node.val <= post.val:
                    pre.next = node
                    node.next = post
                    break
                else:
                    pre = post
                    post = post.next
                    
        return head
```
"""
其实完全可以利用前一个插入的位置进行提速，即每次先把当前要插入的元素和前一个插入点比较，如果比它大，
那么就从这里开始搜索，否则才需要从链表头开始搜索。这里也是一个可以优化的地方。
"""
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if (not head) or (not head.next) : return head
        left = head
        pre_insert = head
        while left.next:
            node = left.next
            if node.val >= left.val:
                left = left.next
                continue
            left.next = node.next

            #这里进行提速，本次插入的值和上一次插入的前一位置值作比较，如果node.val 大于上一次插入前的位置，那么比较
            #的起始位置就是从上一次插入的位置开始。否则就从头开始搜索。
            if node.val  > pre_insert.val:
                pre = pre_insert
                post = pre.next
            else:
                pre = head
                post = head.next
                
            while pre != left.next:
                if node.val <= pre.val:
                    node.next = pre
                    head = node
                    break
                elif pre.val < node.val <= post.val:
                    pre.next = node
                    node.next = post
                    pre_insert = pre#保存上一次插入位置
                    break
                else:
                    pre = post
                    post = post.next
                    
        return head
            
```
