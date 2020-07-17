"""
[589. N叉树的前序遍历](https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/)
给定一个 N 叉树，返回其节点值的前序遍历。

例如，给定一个 3叉树 :

 

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200717135423575.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)

 

返回其前序遍历: [1,3,5,6,2,4]。
说明: 递归法很简单，你可以使用迭代法完成此题吗?

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200717135451243.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)

1.前序遍历
在N叉树中，前序遍历指先访问根节点，然后逐个遍历以其子节点为根的子树。
例如，上述三叉树的前序遍历是: A->B->C->E->F->D->G.

2.后序遍历
在N叉树中，后序遍历指前先逐个遍历以根节点的子节点为根的子树，最后访问根节点。
例如，上述三叉树的后序遍历是: B->E->F->C->G->D->A.

3.层序遍历
N叉树的层序遍历与二叉树的一致。通常，当我们在树中进行广度优先搜索时，我们将按层序的顺序进行遍历。
例如，上述三叉树的层序遍历是: A->B->C->D->E->F->G.
***********
使用递归，前序遍历，每次不为空就加入res,再看其是否有子节点，有的话继续递归。
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []

        def solve(root):
            if not root: return Node
            res.append(root.val)
            if root.children:
                for chl in root.children:
                    solve(chl)
        solve(root)
        return res

```
