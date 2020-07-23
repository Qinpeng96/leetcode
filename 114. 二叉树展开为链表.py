"""
[114. 二叉树展开为链表](https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/)
给定一个二叉树，原地将它展开为一个单链表。

例如，给定二叉树
#
	    1
	   / \
	  2   5
	 / \   \
	3   4   6
将其展开为：
#
	1
	 \
	  2
	   \
	    3
	     \
	      4
	       \
	        5
	         \
	          6
	         
***
这道题开始也没想明白怎么弄，只知道可以前序遍历之后，再重新组合成一个右子树，同时左子树清零。

但是还是有一些米奇妙妙屋的妙脆角方法:

方案一
#
	1.将左子树插入到右子树的地方
	2.将原来的右子树接到左子树的最右边节点
	3.考虑新的右子树的根节点，一直重复上边的过程，直到新的右子树为 null
	
方案二：
#
使用后序遍历，654321，然后6< --5, 4321,逐步连接。因为我们是需要把结果放在右子树。如果使用前序遍历，每遍历一个就修改，那么提取2到右子树时，
右子树会改变。所以要首先遍历右子树。可以知道，后序遍历刚好就是先遍历右节点。

方案三
#
前序遍历得到的值，直接依次接在右子树的右节点上面。

这里贴一个题解连接[力扣题解](https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by--26/)
"""
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = []
        def solve(root):#前序遍历，得到节点值
            if not root: return 
            res.append(root.val)
            solve(root.left)
            solve(root.right)
        solve(root)

        node = root#复制一个节点位置
        n = len(res)
        for i in range(1,n):#右子树右节赋值，左节点为空
            node.left = None
            node.right = TreeNode(res[i])
            node = node.right
        # print(res)
```
