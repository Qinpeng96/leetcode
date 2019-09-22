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





