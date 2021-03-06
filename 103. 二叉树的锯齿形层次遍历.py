"""
[103. 二叉树的锯齿形层次遍历](https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/)
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],
#
	    3
	   / \
	  9  20
	    /  \
	   15   7
返回锯齿形层次遍历如下：
#
	[
	  [3],
	  [20,9],
	  [15,7]
	]
***
这道题的思路还是和之前的层次遍历是一样的，只不过每次需要转变一下方向，每层增加一个标志位，每次翻转输出即可。
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        Flag = 1
        queue = collections.deque([root])
        while queue:
            level = []
            Flag = -Flag
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            
            if Flag == 1:
                res.append(level[::-1])
            elif Flag == -1:
                res.append(level)
        return res
