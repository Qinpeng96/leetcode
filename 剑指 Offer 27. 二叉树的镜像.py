"""
[剑指 Offer 27. 二叉树的镜像](https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/)
请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：
#
	     4
	   /   \
	  2     7
	 / \   / \
	1   3 6   9
镜像输出：
#
	     4
	   /   \
	  7     2
	 / \   / \
	9   6 3   1

 

示例 1：

输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]
 

限制：

0 <= 节点个数 <= 1000
***
使用DFS
- 左右节点都存在,两者交换
- -只有左节点,赋值给右节点,左节点置空
- 只有右节点,赋值给左节点,右节点置空
- 为空节点,返回
"""
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        head = root
        def dfs(head):
            if not head: return 
            if head.left and head.right:
                head.left, head.right = head.right, head.left
                dfs(head.left)
                dfs(head.right)
            elif head.left and not head.right:
                head.right = head.left
                head.left = None
                dfs(head.right)
            elif head.right and not head.left:
                head.left = head.right
                head.right = None
                dfs(head.left)
        dfs(head)
        return root


```
大佬总是这么秀:

```python
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root: return
        root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
        return root

作者：jyd
链接：https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/solution/mian-shi-ti-27-er-cha-shu-de-jing-xiang-di-gui-fu-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
