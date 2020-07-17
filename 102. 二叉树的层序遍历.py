[102. 二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/)
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

 

示例：
二叉树：[3,9,20,null,null,15,7],
#
	    3
	   / \
	  9  20
	    /  \
	   15   7
返回其层次遍历结果：
#
	[
	  [3],
	  [9,20],
	  [15,7]
	]
***
使用BFS队列进行解题，借助N叉树的层序遍历，还是for循环那里的循环次数一固定，问题就比较好解。注意，加入队列的时候，需要一个一个加入，如果是直接加入，方便队列计数保存。
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        queue = collections.deque()
        res = []
        out = []
        queue.append(root)
        while queue:

            for _ in range(len(queue)):
                node = queue.popleft()
                res.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            out.append(res)
            res = []

        return out
