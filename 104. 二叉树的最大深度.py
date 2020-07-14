"""              
104. 二叉树的最大深度
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。


##################################################
有自定向下和自底向上两种方法

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

###首先是自顶向下的方法
#首先是自顶向下的递归，第一步确定递归的返回条件：
#当本节点的子节点为空不存在的时候，我们就开始向下走。每走一层，深度信息增加以，
# 这样一层一层走下去，更新最大深度。

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def solve(root:TreeNode, depth):
            if not root:#节点为空，返回当前的深度
                return depth
            else:
                return max(solve(root.right, depth + 1), solve(root.left, depth + 1))
        return solve(root, 0)
        
####自底向上的方法
#接下来是自底向上的方法,递归返回的时候，每往上走一层就加一。最后一层返回的是0。
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def solve(root:TreeNode):
            if not root:#节点为空，返回当前层的深度
                return 0
            else:#由于自底向上，每一个节点深度都等于 max（左边最大深度, 右边最大深度）
                return max(solve(root.right) + 1, solve(root.left) + 1)#返回的时候每往上走一层就加一
        return solve(root)
 