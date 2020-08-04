"""
[328. 奇偶链表](https://leetcode-cn.com/problems/odd-even-linked-list/)
给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。

请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。

示例 1:

输入: 1->2->3->4->5->NULL
输出: 1->3->5->2->4->NULL
示例 2:

输入: 2->1->3->5->6->4->7->NULL 
输出: 2->3->6->7->1->5->4->NULL
说明:

应当保持奇数节点和偶数节点的相对顺序。
链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。
***
将整条链表分为奇偶两条链表，再把两条链表连接起来就可以。
- 首先是判断特殊情况，链表为空，或者链表内的只有一个数，那么直接返回链表。
- 取第一个数开始为寄链表，取第二个数开始为偶链表。
- 判断奇链表和偶链表的后面是否为空，级链表的后面一位就是偶链表的最后一位，所以开始的时候如果奇链表的后面是有值的，就看偶链表后面是否有值。
- 如果偶链表后面有值，那么奇链表就可以接这个数,例如[1,2,3],1就可以接3，然后奇链表头后移，偶链表接奇链表的下一个。
- 为啥不可以只判断偶链表的尾部了？例如[1,2,3]一次循环之后为 1-3， 2-None,这时候我们None没有next, 3的next为空，说明
链的长度是奇数，偶数可能会直接连上None,导致无法判断next.
- while循环的判断条件只能是先odd.next 再even.next。总个数为奇数的时候：先判断奇数的下一个，再判断偶数的下一个。
- 总个数为偶数的时候，由于奇数的next是下一个偶数，所以有效。但是偶数的下一个为空，无效。所以需要注意一下这里的循环判断条件的次序，以及为什么这么设置循环条件。
"""
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if (not head) or (not head.next): return head
        node = head#头节点

        odd = head#奇数链
        evenStart = head.next
        even = head.next#偶数链
        while odd.next and even.next:#注意这里的判断条件，先奇数，再偶数
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenStart
        return node
            
```
