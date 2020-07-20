"""
[113. 路径总和 II](https://leetcode-cn.com/problems/path-sum-ii/)
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，
#
	              5
	             / \
	            4   8
	           /   / \
	          11  13  4
	         /  \    / \
	        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]
***
相当于DFS，每次计算到叶子节点。
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        out = []
        target = 0

        def helper(root,target,res):
            if not root: return
            res.append(root.val)#每次进入加入当前值到列表和总和中
            target += root.val
            # print(res, target)
            if sum == target and not root.left and not root.right:#如果为叶子节点，且总和等于sum输出
                out.append(res[:])
                return 
            if root.left:#如果左边不为空
                helper(root.left, target, res) 
                res.pop()
            if root.right:#如果右边不为空
                helper(root.right, target, res)
                res.pop()

        helper(root,0,[])
        return out


