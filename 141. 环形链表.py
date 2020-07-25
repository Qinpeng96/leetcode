"""
[141. 环形链表](https://leetcode-cn.com/problems/linked-list-cycle/)
给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。



示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。
***
使用快慢指针，如果快指针到了空null，则为false.
如果快慢指针相遇，说明存在有环。
"""
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head: return False
        fast = head
        slow = head
        while fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
            elif not fast:
                return False
        return False
```
