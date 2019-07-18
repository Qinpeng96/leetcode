# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if self.getLength(l1) < self.getLength(l2): #保证l1永远比l2更长
            l1, l2 = l2, l1
            
        head = l1   
        while(l2):#执行加法
            l1.val += l2.val
            l1 = l1.next
            l2 = l2.next
        
        p = head
        while(p):#处理进位
            if p.val > 9:
                p.val -= 10
                if p.next:
                    p.next.val += 1
                else:
                    p.next = ListNode(1)
            p = p.next
                    
        return head
        
        
    def getLength(self, l):#计算链表长度
        length = 0
        while(l):
            length += 1
            l = l.next
        return length
