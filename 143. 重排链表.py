"""
[143. 重排链表](https://leetcode-cn.com/problems/reorder-list/)
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1:

给定链表 1->2->3->4, 重新排列为 1->4->2->3.
示例 2:

给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
***
开始我想到另一个办法，就是效率太低了。
#
	[1,2,3,4,5] ->[1,5,4,3,2]->[1,5,2,3,4]->[1,5,2,4,3]
每次反转后面的链表，反转之后，往后移动一位。
但是会超时=-=
"""
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: return head
        def solve(cur):#反转该节点以及之后的链表
            pre = None
            while cur:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
            return pre
            
        while head.next:#对于每一个节点，依次翻转相连
            head.next = solve(head.next)
            head = head.next
    
```

这里使用的是使用快慢指针找到中点，反转后面的链表，然后再对前后两部分链表进行合并。这样做的效率就好很多。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: return head
        slow = head
        fast = head
        while fast.next and fast.next.next:#快慢指针找中点[1,2,3,4,5]
            slow = slow.next
            fast = fast.next.next
        #反转后面部分的链表
        pre = None
        cur = slow.next
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
    
        slow.next = pre#前半部分和后面反转后的一般连接起来 [1,2,3,5,4]
        #开始拼接
        p1 = head          #链表头
        p2 = slow.next     #反转头

        while p1 != slow:#交叉连接的顺序很重要，先连接尾部
            slow.next = p2.next
            p2.next = p1.next
            p1.next = p2
            p1 = p2.next
            p2 = slow.next
            
```