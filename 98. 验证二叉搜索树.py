"""
98. 验证二叉搜索树
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。


这道题使用中序遍历，每次遍历的过程中将值与之前res内的最大值作比较。res内的值必须是递增的，
所以如果当前值小于res[-1],那么我们就可以判断这不是一个二叉搜索树。

对于二叉搜索树，一般都是用中序遍历的解法求解。
"""
from typing import List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        res = [-float('inf')]
        valid = True 
        def solve(root):
            nonlocal valid
            if not root: return 
            solve(root.left)
            if valid == False: return #遇到错误，直接返回

            if root.val > res[-1]: # 如果中序遍历的值一直是递增的，那么加入列表
                res.pop()
                res.append(root.val)
            else:
                valid = False # 如果遍历的过程中，有值不是递增，valid赋值False
                return
                
            solve(root.right)
            if valid == False: return #遇到错误，直接返回

            return
        solve(root)
        # print(res)
        return valid


