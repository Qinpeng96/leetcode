"""
105. 从前序与中序遍历序列构造二叉树
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7



首先要知道一个结论，前序/后序+中序序列可以唯一确定一棵二叉树，所以自然而然可以用来建树。

看一下前序和中序有什么特点，前序1,2,4,7,3,5,6,8 ，中序4,7,2,1,5,3,8,6；

有如下特征：

1.前序中左起第一位1肯定是根结点，我们可以据此找到中序中根结点的位置node；

2.中序中根结点左边就是左子树结点，右边就是右子树结点，即 inorder[左子树结点，根结点，右子树结点]，我们就可以得出左子树结点个数为int left = rootin - leftin;；

3.前序中结点分布应该是：[根结点，左子树结点，右子树结点]；

4.根据前一步确定的左子树个数，可以确定前序中左子树结点和右子树结点的范围；
如果我们要前序遍历生成二叉树的话，下一层递归应该是：
**左子树：root->left = buildTree(前序左子树范围，中序左子树范围);；
右子树：root->right = buildTree(前序右子树范围，中序右子树范围);。**
每一层递归都要返回当前根结点root；

"""
from typing import List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:  # 递归终止条件
            return
        root = TreeNode(preorder[0])  # 先序为“根左右”，所以根据preorder可以确定root
        idx = inorder.index(preorder[0])  # 中序为“左根右”，根据root可以划分出左右子树
        # 下面递归对root的左右子树求解即可
        root.left = self.buildTree(preorder[1:1 + idx], inorder[:idx])
        root.right = self.buildTree(preorder[1 + idx:], inorder[idx + 1:])
        return root

作者：LotusPanda
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solution/xiong-mao-shua-ti-python3-xian-xu-zhao-gen-hua-fen/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。