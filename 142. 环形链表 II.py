"""
[142. 环形链表 II](https://leetcode-cn.com/problems/linked-list-cycle-ii/)
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。

 

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。
***
快慢指针在第一次相遇的时候，一定在环上，这个时候做一个设定。

 1. 设起点到环入口距离为a
 2. 快慢指针首次相遇的地方距离入口为b
 3. 我们可以知道慢指针走了 (a+b) , 而快指针走了 2*(a+b)，如果慢指针在走(a+b)[相当于快指针]，那么慢指针又会回到第一次相遇的位置。
 4. 由于我们需要找到入口位置，那么慢指针只需要走a的长度就可以达到入口位置，如果此时起点和慢指针一起走，那么我们就可以找到入口位置。
***
"""

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head: return None
        fast = head
        slow = head

        while fast.next:
            fast = fast.next.next
            slow = slow.next

            if not fast:
                return None
            elif fast == slow:
                while head != slow:
                    head = head.next
                    slow = slow.next
                return slow
        return None
```
