"""
[111. 二叉树的最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/)
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],
#
	    3
	   / \
	  9  20
	    /  \
	   15   7
返回它的最小深度  2.
***
这道题会有一种特殊情况就是单变二叉树，这样的话就不能简单的使用==ans = min(solve(root.left), solve(root.right)) + 1==，因为单边，另一边的值一直为1，这样求min,算出来的最小深度不对，所以只有分开单边的情况讨论。即一边为空，就递归另一边。

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        
        def solve(root):
            if not root: return 0
            if not root.right:#这是两种单边的情况，需要单独谈论，单边就不需比较，只对另一边求解。
                ans = solve(root.left)+1
            elif not root.left:
                ans = solve(root.right)+1
            else:#节点左右两边都有值，所以需要比大小
                ans = min(solve(root.left), solve(root.right)) + 1
            return ans
        return solve(root)

