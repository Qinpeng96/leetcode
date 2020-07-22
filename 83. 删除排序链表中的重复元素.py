"""
[83. 删除排序链表中的重复元素](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/)
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3
***

 1. 首先是确定一个头节点的位置，赋值为node,防止以后操作之后找不到头
 2. 当前节点不为空的时候，设置post为head之后的节点，进行循环去重的操作
 3. 当post不为空，且post的值和head的值是一样的时候，post后移，知道post为空或者post的值不等于head的值的时候才跳出循环。
 4. 跳出循环之后，head连接post(不相等的值)，head后移。

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node = head#防止跑飞，复制一个头节点
        while head:
            post = head.next#当前值的下一个值设置为post
            while post and head.val == post.val :#post不为空并且两者相等，一直循环
                post = post.next
            head.next = post#找到不一样的值，或者搜索完毕，连接两个端点，链表头后移
            head = head.next
        return node

