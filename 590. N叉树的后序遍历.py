"""
[590. N叉树的后序遍历](https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/)
给定一个 N 叉树，返回其节点值的后序遍历。

例如，给定一个 3叉树 :

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200717142332277.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)
返回其后序遍历: [5,6,3,2,4,1].
说明: 递归法很简单，你可以使用迭代法完成此题吗?
***

后序遍历和前序遍历不同，前序遍历在每次遍历前就加入到res。
而后序遍历在每次遍历之后才依次加入到res。
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def solve(root):
            if not root: return None
            for chl in root.children:
                solve(chl)
            res.append(root.val)
        solve(root)
        return res

