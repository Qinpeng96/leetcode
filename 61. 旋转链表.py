"""
[61. 旋转链表](https://leetcode-cn.com/problems/rotate-list/)
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL
***

 1. 首先算出链表的总长度，因为有时候循环移位的次数大于链表的长度。会出现重复的操作。
 2. 使用左右指针，找到倒数第k个节点位置，此时节点为left, 最右边的节点为right， 已经为空
 3. 将left前面节点pre_left后接None, righr前面一个pre_right后接head。

 最后输出left为首的链表即可

```python
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head: return #
        
        #计算链表的长度
        cnt = 0
        node = head
        while node:
            node = node.next
            cnt += 1
        k %= cnt #长度取模，减少循环的次数
        if k == 0: return head#刚好直接返回原链表

        left = right = head#创建一个左右节点，找到倒数第k个值
        while right:
            while k:
                right = right.next
                k -= 1
            pre_left = left#这里设置left左节点的上一个节点，因为需要从这里断开
            left = left.next
            pre_right = right
            right = right.next
        
        pre_left.next = None#left左边的节点后面接None,取值为空
        pre_right.next = head #把之后的right的next接到头部
        return left

