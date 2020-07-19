#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def find_mid(pre, post):#使用快慢指针，找到中间的那个数
            first = pre
            second = pre
            while second != post and second.next != post:#当快指针当前和下一个节点不为尾节点
                first = first.next
                second = second.next.next
            return first

        def helper(head, tail):#递归调用
            if head == tail: return #弹出条件
            node = find_mid(head, tail)
            root = TreeNode(node.val)
            root.left = helper(head, node)#左边递归
            root.right = helper(node.next, tail)#右边递归
            return root
        return helper(head, None)
# @lc code=end

