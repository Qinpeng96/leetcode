# -*- coding: utf-8 -*-
"""
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""暴力法，取出所有的数值在进行排序，创建链表"""
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        self.node = []
        head = piont = ListNode(0)
        for l in lists:
            while l:
                self.node.append(l.val)
                l = l.next
        for i in sorted(self.node):
            piont.next = ListNode(i)
            piont = piont.next
        return head.next


"""归并排序，从底部两个两个融合，创建链表
    在从底部两两融合的
    interval为1：首先间隔为2，相邻的两个链表融合
    interval为2：间隔为4，相邻为2的两个链表融合
    interval为4：间隔为8，相邻为4的两个链表融合
    这个归并写的很好，好好学习！
"""
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        num = len(lists)
        interval = 1
        while interval < num:
            for i in range(0, num - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if num > 0 else lists

    def merge2Lists(self, l1, l2):
        head = piont = ListNode(0)
        while l1 and l2:
            if l1.val > l2.val:
                piont.next = l2
                l2 = l2.next
            else:
                piont.next = l1
                l1 = l1.next
        if not l2:
            piont.next = l1
        else:
            pinot.next = l2
        return head.next

# if __name__ == "__main__":
#     a = Solution()
#     print(a.generateParenthesis(3))

