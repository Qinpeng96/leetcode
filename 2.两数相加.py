"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，
并且它们的每个节点只能存储一位数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807


"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
 
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if self.getLength(l1) < self.getLength(l2): #保证l1永远比l2更长
            l1, l2 = l2, l1#两者交换位置
            
        head = l1   #设置头链表为l1
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
