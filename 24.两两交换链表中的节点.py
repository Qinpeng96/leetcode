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



