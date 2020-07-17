"""
[108. 将有序数组转换为二叉搜索树](https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/)
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
#
	      0
	     / \
	   -3   9
	   /   /
	 -10  5
	
***


这里才使用的是递归，由于需要构建二叉搜索树，根据其性质，我们每次首先应该找到根节点。
但是在高度平衡二叉树中，我们的根节点一般都是中间值。

所以思路可以总结如下，首先在升序数组中找到中间值，设置为根节点，接着在数组左边找到一个中间值，设置为左子树的根节点，在右边数组内找一个中间值，设置为右子树的根节点。

由于每次都有一个找中间值，并且创建节点的重复步骤，所以考虑使用递归解决。
在对数组取中间值得时候，这里使用得是左闭右闭得区间进行数据得索引。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        def inorder(nums, start, end):
            if start > end: return None
            mid = start + (end - start) // 2#找到中间值得得索引
            root = TreeNode(nums[mid])#最中间值建立节点
            root.left = inorder(nums, start, mid-1)#左子树连接
            root.right = inorder(nums, mid+1, end)#右子树连接
            return root
        return inorder(nums, 0, len(nums)-1)

