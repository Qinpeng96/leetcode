"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。
"""
# -*- coding: utf-8 -*-
# Definition for singly-linked list.
from typing import List 
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        left = head
        right = head
        """删除倒数第n个节点，使用双指针，间隔n，只需要一次遍历即可完成""""
        while n > 0:
            right = right.next
            n -= 1
        if not right: return head.next
        
        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next
        return head