"""
[230. 二叉搜索树中第K小的元素](https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/)
给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。

说明：
你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。

示例 1:

输入: root = [3,1,4,null,2], k = 1
#
	   3
	  / \
	 1   4
	  \
	   2
输出: 1
示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
#
	       5
	      / \
	     3   6
	    / \
	   2   4
	  /
	 1
输出: 3
进阶：
如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？
***
我是用的是中序遍历，只要找到第K个就直接返回，为了可以逐层递归返回，我对递归函数做了一个if判断，如果为真就一直往上层返回True,快速返回，结束递归。
"""
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res = []
        def solve(root):
            if not root: return 
            if solve(root.left): return True
            res.append(root.val)
            if len(res) == k:
                return True
            if solve(root.right): return True
        solve(root)
        return res[-1]
        
```
