"""
[124. 二叉树中的最大路径和](https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/)
给定一个非空二叉树，返回其最大路径和。

本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例 1:

输入: [1,2,3]

       1
      / \
     2   3

输出: 6
示例 2:

输入: [-10,9,20,null,null,15,7]

	   -10
	   / \
	  9  20
	    /  \
	   15   7

输出: 42
***
这个题目知道是要用递归去做，一般二叉树都是递归。但是这道题有一个坑：

我们在计算某一段的最大值的时候，例如示例一：是取得 2+1+3  = 6。但是我们在往更上层返回值的时候，由于本题要求的是点到点，
不能有岔路，但是如果返回一个有岔路的树，就不对。所以这里只能返回本节点和左右节点中的最大值。

上面这一点在我做这道题的时候想怎么去设置返回值，如果设置max(左，右) + root作为返回值，那么假如是示例一那样的形状，
需要左中右三个点的值，就不成立。但是返回三个点的值就违背了题目的意思。
最后看了题解才知道，只需要设定一个全局的最大值，每次更新这个最大值就可以了，返回的话就只返回max(左，右) + root。这里的root是必须要的。

有一个需要注意的地方就是，有的节点值是负数，我们在返回的时候，还需要控制一下负数的情况，负数在这里就是返回的0, 
因为和一个 0 取max，如果返回值和小于0，经过max后等于0，也就相当于不取这个值的意思。
"""


```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max = -float('inf')
        def solve(root):
            if not root:return 0
            left =  solve(root.left) #得到左子树的最大值
            right = solve(root.right) #得到右子树的最大值
            self.max = max(self.max, left + right + root.val)#记录当前的值，为一个左中右
            return max(0, max(left, right) + root.val)#需要经过根节点才能往上递归
        solve(root)
        return self.max
```
