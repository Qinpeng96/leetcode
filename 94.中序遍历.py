"""
94. 二叉树的中序遍历
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
"""
# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#前序遍历   中，左， 右
#中序遍历   左，中， 右
#后序遍历   左，右， 中

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def solve(root):
            if not root:
                return 0
            solve(root.left)#       左
            res.append(root.val)#   中
            solve(root.right)#      右
        solve(root)
        return res