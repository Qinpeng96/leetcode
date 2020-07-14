"""
106. 从中序与后序遍历序列构造二叉树
根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7


前+后
首先我们可以显然知道当前根节点为pre[pre_start],并且它在后序中的位置为post_end，因此这里我们需要找到能区分左右子树的节点。
我们知道左子树的根节点为pre[pre_start+1]，因此只要找到它在后序中的位置就可以分开左右子树（index的含义）

前+中
首先我们可以显然知道当前根节点为pre[pre_start],只用找出它在中序中的位置，就可以把左右子树分开（index的含义）
 
中+后
首先我们可以显然知道当前根节点为post[post_end]，只用找出它在中序中的位置，就可以把左右子树分开（index的含义）

"""
from typing import List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder: return
        index = inorder.index(postorder[-1])
        root = TreeNode(postorder[-1])
        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[index+1: ], postorder[index:-1])
        return root
         

