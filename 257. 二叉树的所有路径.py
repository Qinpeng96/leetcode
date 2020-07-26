"""
[257. 二叉树的所有路径](https://leetcode-cn.com/problems/binary-tree-paths/)
给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

示例:

输入:
#
	   1
	 /   \
	2     3
	 \
	  5
	
输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
***
使用DFS，从根节点往下面回溯寻找每一条链路，并且将其加入字符串，到达叶子节点的时候，就加入到输出out。
"""

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = ""
        out = []
        def backtrack(root, res):
            if not root: return 
            if not root.left and not root.right:
                res +=  '->' + str(root.val)
                out.append(res[2:])
                return 

            if root.left:
                backtrack(root.left, res + '->' + str(root.val))
            if root.right:
                backtrack(root.right, res + '->' + str(root.val))

        backtrack(root, "")
        return out

            
```
