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
使用后序遍历，654321，然后6< --5, 4321,逐步连接。因为我们是需要把结果放在右子树。如果使用前序遍历，每遍历一个就修改，那么提取2到右子树时，右子树会改变。所以要首先遍历右子树。可以知道，后序遍历刚好就是先遍历右节点。

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
"""
还有一种方法就是，找右子树的左子树前驱节点。将右子树接到左子树的最右边（二叉搜索树的最大位置），然后root断开左子树，将左子树连接到右子树上去。逐节点操作即可。

**官方解释：**
注意到前序遍历访问各节点的顺序是根节点、左子树、右子树。如果一个节点的左子节点为空，则该节点不需要进行展开操作。如果一个节点的左子节点不为空，则该节点的左子树中的最后一个节点被访问之后，该节点的右子节点被访问。该节点的左子树中最后一个被访问的节点是左子树中的最右边的节点，也是该节点的前驱节点。因此，问题转化成寻找当前节点的前驱节点。

具体做法是，对于当前节点，如果其左子节点不为空，则在其左子树中找到最右边的节点，作为前驱节点，将当前节点的右子节点赋给前驱节点的右子节点，然后将当前节点的左子节点赋给当前节点的右子节点，并将当前节点的左子节点设为空。对当前节点处理结束后，继续处理链表中的下一个节点，直到所有节点都处理结束。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/solution/er-cha-shu-zhan-kai-wei-lian-biao-by-leetcode-solu/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
```python
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def solve(root):
            head = root
            if head.left:#如果左子树存在
                node = head.left
                while node.right:#找到左子树的最右节点
                    node = node.right
                node.right = head.right#将左子树的最右连接一个右子树
                new_right = head.left#断开左子树
                head.left = None
                head.right = new_right#将左子树移动到原来右子树的位置
        while root:
            solve(root)
            root = root.right
```
