 """
889. 根据前序和后序遍历构造二叉树
返回与给定的前序和后序遍历匹配的任何二叉树。

 pre 和 post 遍历中的值是不同的正整数。


示例：

输入：pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
输出：[1,2,3,4,5,6,7]
 

提示：

1 <= pre.length == post.length <= 30
pre[] 和 post[] 都是 1, 2, ..., pre.length 的排列
每个输入保证至少有一个答案。如果有多个答案，可以返回其中一个。

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        def dfs(pre,post):
            if not pre:
                return None
            # 数组长度为1时，直接返回即可
            if len(pre)==1:
                return TreeNode(pre[0])
            # 根据前序数组的第一个元素，创建根节点     
            root = TreeNode(pre[0])
            # 根据前序数组第二个元素，确定后序数组左子树范围
            left_count = post.index(pre[1])+1
            # 递归执行前序数组左边、后序数组左边
            root.left = dfs(pre[1:left_count+1],post[:left_count])
            # 递归执行前序数组右边、后序数组右边
            root.right = dfs(pre[left_count+1:],post[left_count:-1])
            # 返回根节点
            return root
        return dfs(pre,post)

作者：wang_ni_ma
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/solution/tu-jie-889-gen-ju-qian-xu-he-hou-xu-bian-li-gou-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。