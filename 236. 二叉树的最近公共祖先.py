"""
236. 二叉树的最近公共祖先
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]



 

示例 1:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
示例 2:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
 

说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉树中。

############################################################################################

左子树或自己含p 就返回p，右子树或自己含q就返回q，左右子树返回一p一q则返回自己，
如果某子树返回了答案（另一子树必然返回None），则返回答案，剩下就是两个子树都返回空，则返回空。 经过逻辑化简：

先分析自己，自己是p,q,None中的一者，自然返回自己。
然后分析左右子树的返回值，如果其中一个是None，则返回另一个，作为传递，无论是传递最终的答案，还是传递p和q。
如果左右子树返回p和q，当然返回root。 Python中的None即C/C++/Java 中的Null/null
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def solve(root, p, q):
            if not root or root == p or root == q: return root#如果根节点找到一个或者空，那么返回当前节点
            left = solve(root.left, p, q) #在左边找
            right = solve(root.right, p, q)#在右边找
            #对节点root左右两边的情况对比分析
            if left == None and right != None: return right
            elif right == None and left != None: return left
            elif left == None and right == None: return None
            else: return root

        return solve(root, p, q)