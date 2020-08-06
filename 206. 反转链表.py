"""
[206. 反转链表](https://leetcode-cn.com/problems/reverse-linked-list/)
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
***
反转一个链表有两种方法：
迭代法和递归法。
迭代法就是每次提出一个左边元数，插入到之前的一个链表中去。
#
	[1,2,3,4,5,None]
	[1,None] 			[2,3,4,5,None]
	[2,1,None] 			[3,4,5,None]
	[3,2,1, None] 		[4,5,None]
	[4,3,2,1,None] 		[5,None]
	[5,4,3,2,1,None] 	[None]
"""
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre
```
"""
下面是递归法做：
递归不要想太多，就指向head之后都倒序了这一种情况就可以了。
#
	[1->2<-3<-4<-5<-6]	head = 1,之后的数都是反转好了的，并且每次返回都是返回的头节点，即6
	此时 只需要把2->1, 1->None， 再返回头节点6就可以了。
"""
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        last = self.reverseList(head.next)#默认已经排好序了
        head.next.next = head
        head.next = None
        return last
```
