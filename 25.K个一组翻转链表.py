# -*- coding: utf-8 -*-
"""
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例 :

给定这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""

"""

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        piont = head
        index = 0
        while (index != k and piont):#例如交换三个节点，运行之后 index=3，p.val= 4
            piont = piont.next #p此时是作为尾节点存在，不会实质参与节点交换，只是起连接作用
            index += 1
        if index == k:#满足交换的个数条件
            piont = self.reverseKGroup(piont, k)#递归，继续判断之后链表是否满足交换条件
            """
            例如：1->2->3->4 			 h=1, t=2, p=4
			第一步：1->4； 2->3->4；		 h=2, t=3, p=1
			第二步：2->1->4； 3->4；		 h=3, t=4, p=2
			第三步：3->2->1->4；			 h=4, p=3 跳出循环后，将head=piont，head=3
			"""
            while (index != 0):#实际的交换过程
                temp = head.next 
                head.next = piont
                piont = head
                head = temp
                index -= 1
            head = piont

        return head #返回自己的头节点作为P,因为是递归，所以是从后往前处理的，
                    #返回的后一个链表的头节点作为本次运行的尾节点
"""
递归分步说明：(假定链表1->2->3->4->5->6->7,k=3):
第0轮：
head = 1->..
p = 4->..
    进入第1轮：
    head = 4->..
    p = 7
        进入第二轮：
        head = 7
        return head(7)
    回到第一轮：
    p=7
    循环进行链表翻转：
    index = 3
        temp = 5
        head = 4->7
        p = 4->7
        head = 5->6->4->7
    index = 2
        temp = 6
        head = 5->4->7
        p = 5->4->7
        head =6->5->4->7
    index = 1
        temp =5
        head = 6->5->4->7
        p = 6->5->4->7
        head = 6->5->4->7
    return 6->5->4->7
回到第0轮：
p = 6->5->4->7
循环进行链表翻转：
return 3->2->1->6->5->4->7


作者：Chen_Yang
链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group/solution/di-gui-fa-by-chen_yang/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
