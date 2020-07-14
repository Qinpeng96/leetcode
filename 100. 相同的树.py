"""
100. 相同的树
给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:

输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true
示例 2:

输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false
示例 3:

输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

输出: false
"""

from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:return True#q p当前都为空
        if not p or not q: return False#q p 当前有一个为空，一个不为空
        if p.val != q.val:return False#两者当前值不相等，返回Fasle
        #还有一种情况就是两者都不为空，并且值相等，需要左右向下寻找
        #只有所有的都为True，最中结果才会为True
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)




