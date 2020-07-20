"""
[99. 恢复二叉搜索树](https://leetcode-cn.com/problems/recover-binary-search-tree/)
二叉搜索树中的两个节点被错误地交换。

请在不改变其结构的情况下，恢复这棵树。

示例 1:

输入: [1,3,null,null,2]
#
	   1
	  /
	 3
	  \
	   2
	
输出: [3,1,null,null,2]
#
	   3
	  /
	 1
	  \
	   2
示例 2:

输入: [3,1,4,null,null,2]
#
	  3
	 / \
	1   4
	   /
	  2
	
输出: [2,1,4,null,null,3]
#
	  2
	 / \
	1   4
	   /
	  3
进阶:

使用 O(n) 空间复杂度的解法很容易实现。
你能想出一个只使用常数空间的解决方案吗？
***
"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = []
        err = []
        def insort(root):#定义一个中序遍历
            if not root: return 
            insort(root.left)
            res.append(root.val)
            insort(root.right)

        def change(root):#定义一个遍历交换
            if not root: return 
            if root.val in err:
                root.val = err[0] if root.val == err[1] else err[1]
            change(root.left)
            change(root.right)

        insort(root)#中序遍历，得到序列数组
        sorted_res = sorted(res)#对其序列进行排序，找到错误的两个数的位置
        for i in range(len(res)):#
            if sorted_res[i] != res[i]:
                err.append(res[i])
        change(root)   #遍历一次，交换两个错误的数值     
        

