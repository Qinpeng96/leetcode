"""
110. 平衡二叉树
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。


这道题需要计算节点两边的高度差，应该还是使用递归最简单。

 1. 首先我们需要计算出当前节点的高度： 其高度值等于左子树高度和右子树高度的最大值。在计算高度的时候，
    如果节点为空，赋值 -1，没有子节点的节点赋值为0
 2. 自顶向下的进行递归，首先确定初始值，即递归的返回条件， root 为空 则返回True。
 3. 递归返回的是三个条件  左子树和右子树高度是否平和； 左子树是否平衡； 右子树是否平衡；

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#左子树高 和 右子树高相差最多为1，首先我们需要计算出子树高度

class Solution:
    def height(self, root: TreeNode)-> int:
        if not root: return -1
        else:
            return max(self.height(root.left),self.height(root.right))+1

    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        if root: 
            return self.isBalanced(root.left) and self.isBalanced(root.right)\
                and abs(self.height(root.left) - self.height(root.right)) < 2