"""
[107. 二叉树的层次遍历 II](https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/)
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],
#
	    3
	   / \
	  9  20
	    /  \
	   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]
***
和之前的遍历方法一样，只是最后结果翻转而已。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        out = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            res = []
            for _ in range(len(queue)):
                node = queue.popleft()
                res.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            out.append(res)

        return out[::-1]

