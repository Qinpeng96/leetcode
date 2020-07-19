#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#199. 二叉树的右视图
# 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，
# 返回从右侧所能看到的节点值。

# 示例:

# 输入: [1,2,3,null,5,null,4]
# 输出: [1, 3, 4]
# 解释:

#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        queue = collections.deque()
        queue.append(root)
        out = []
        res = None
        while queue:
            for _ in range(len(queue)):
                node  = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                res = node.val
            out.append(res)
            res = None
        return out
# @lc code=end

