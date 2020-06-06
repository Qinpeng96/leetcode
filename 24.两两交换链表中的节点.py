# -*- coding: utf-8 -*-
"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

 

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
使用递归来进行交换  1->2->3->4 每次都只交换两个节点，
分为first节点　和　second节点　每次交换这两个节点　其中交换后的first节点指向剩下的节点
将剩下的链表进行递归
每次返回是返回的第二个节点，因为每次进行交换之后的链表second节点变到最前面了
"""
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 对节点是否为空 或者 只有一个节点进行判断  
        # 如果成立就返回该链表（空或者1个）
        if not (head.next and head):
            return head
        #赋值
        firstnode = head
        secondnode = head.next

        #进行递归和交换操作
        firstnode.next = self.swapPairs(secondnode.next)
        secondnode.next = firstnode

        #每次返回的是第二个节点，因为第二个节点在交换后变成了头节点
        retrun secondnode
"""
第二种解法：按照顺序，逐次交换。
但是这里有一个问题：每次交换的时候虽然是两个节点之间的交换，但是其中涉及到的节点个数是三个因为链表的特殊性质，
例如交换1->2->3-4的前两个，我们需要设置一个新的头节点ListNode(0)，0->1->2->3->
 2->1->3->4需要交换3，4,但是交换3，4的时候我们需要2->指向3，4交换后的头节点，所以虽然是两个节点之间的交换，但是实际上我们需要用到三个节点。

下面这种方法就是使用三个节点进行后两个节点之间的交换，每次的需要交换的首节点是保持不变的，后面两个节点进行交换。
"""

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        First = ListNode(0)
        First.next = head#设置一个头节点，并将之与要交换的链表连接
        p = First#从整个链表头开始，因为每一次交换的三个节点中，头节点不会交换
        while p.next and p.next.next:#判断需要交换的两个节点是否存在: 0->1->2->3->4
            a, b = p.next, p.next.next #如果存在，则分别赋值给p=0,a=1,b=2:0->1->2->3->4 
            p.next, a.next = b, b.next:# P:0->2->3->4   a：1->3->4 b:2->3->4
            b.next = a#这两条语句对后面两个节点进行了交换 b:2->1->3->4 p:0->2->1->3->4 a：1->3->4 
            p = b.next#后移链表头到待交换处前 p:1->3->4,由于头节点不变，即1不变，下一轮又对3，4交换
        return First.next


