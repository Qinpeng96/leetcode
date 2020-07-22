[86. 分隔链表](https://leetcode-cn.com/problems/partition-list/)
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

示例:

输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5
***
本题的方法就是将每一个节点分到两个不同的链表中，最后再把两个链表组合到一起即可。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        node1 = dummy1
        node2 = dummy2
        while head:
            if head.val < x:
                node1.next = ListNode(head.val) 
                head = head.next
                node1 = node1.next
            else:
                node2.next = ListNode(head.val)
                node2 = node2.next
                head = head.next

        node1.next = dummy2.next
        return dummy1.next
```
官方的题解，唯一不同就是直接加入的head节点，但是最后需要添加一个空，保证较大的链的尾部为空。这点比较关键，
之前我也是每次连接的head,但是第二条链表的末尾没有加空None，导致超时。

```python
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        # before and after are the two pointers used to create two list
        # before_head and after_head are used to save the heads of the two lists.
        # All of these are initialized with the dummy nodes created.
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)

        while head:
            # If the original list node is lesser than the given x,
            # assign it to the before list.
            if head.val < x:
                before.next = head
                before = before.next
            else:
                # If the original list node is greater or equal to the given x,
                # assign it to the after list.
                after.next = head
                after = after.next

            # move ahead in the original list
            head = head.next

        # Last node of "after" list would also be ending node of the reformed list
        after.next = None
        # Once all the nodes are correctly assigned to the two lists,
        # combine them to form a single list which would be returned.
        before.next = after_head.next

        return before_head.next

作者：LeetCode
链接：https://leetcode-cn.com/problems/partition-list/solution/fen-ge-lian-biao-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
