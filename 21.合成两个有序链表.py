# -*- coding: utf-8 -*-
"""
@author: 79877
"""
from typing import List 
##################################################
        #链表转成列表
def List2Numbers(list1):
        a1=[]
        while(list1):
            a1.append(list1.val)
            list1=list1.next
        return list1

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val >= l2.val:
                l1,l2 = l2,l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2
###################################################
#建立新的链表方法
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head1 = l1
        head2 = l2
        head = ListNode()
        p = head
        while head1.next and head2.next:
            if head1.val < head2.val:
                head = head1
                head1 = head1.next
            else:
                head = head2
                head2 = head2.next   
        if head1 == None:
            head.next = head2
        else:
            head.next = head1
        return p.next





