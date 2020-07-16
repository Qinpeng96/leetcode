"""
450. 删除二叉搜索树中的节点
给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

一般来说，删除节点可分为两个步骤：

首先找到需要删除的节点；
如果找到了，删除它。
说明： 要求算法时间复杂度为 O(h)，h 为树的高度。

示例:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。

一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。

    5
   / \
  4   6
 /     \
2       7

另一个正确答案是 [5,2,6,null,4,null,7]。

    5
   / \
  2   6
   \   \
    4   7


这道题有几个比较巧妙地地方，首先我们删除一个节点，会有三种情况：

该节点只有左子树，右子树为空，如果删除该节点，只需重新连接其左子树即可
该节点只有右子树，左子树为空，如果删除该节点，只需要重连其右子树即可
该节点既有左子树，也有右子树。这种情况就有点复杂，我们需要进一步分析。
针对上面要删除地节点既有左子树也有右子树地情况，我们需要考虑到到底应该派谁来顶替这个删除的节点值。由于是二叉搜索树，
树的值是有规律可循的。通过比较后发现

要么选择左子树的最大值，要么选择右子树的最小值
因为只有这两个数才是最靠近待删除节点值，所以我们可以考虑将左子树的最大值用来顶替待删除的节点。这里还有一个地方需要注意：

题目里面说的是删除一个节点，但是我们不需要真正实际上的删除，只需要将左子树的最大值赋值给待删除的节点就行了，
而不需要实际物理上了删除后再连接的操作，只需要简单的赋值，再将左子树的最大值删除。

这里还有本题另一个巧妙的地方：我们需要删除左子树内的最大值节点，再回过头看下这个程序的名字，不就是删除二叉树内的一个值么？
所以这里再次递归调用删除值。

最后return root根节点，因为根节点每次都只有值在改变，其连接得子树变换得情况在上述得 1，2，3点内都讨论过了。
所以最后返回root就能逐层向上返回得到删除后得数
————————————————
版权声明：本文为CSDN博主「Qin酱」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_38650028/article/details/107391128
"""
##下面是递归的方法
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root: return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)#待删除的数在左子树
            # return root
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)#待删除的数在右子树
            # return root
        elif key == root.val:
            if not root.left: return root.right#只有右子树，直接加入右子树
            elif not root.right: return root.left#只有左子树，直接加入左子树 
            else: #待删除节点下的左右子树都有值，有点麻烦，新连接点为左子树最大或者右子树最小
                cur = root.left #本程序删除的是左边的最大值，然后将其作为连接点
                while cur.right: cur = cur.right#找到左子树的最大值
                root.val = cur.val #之前要删除的点我们不用真的删除，只需要将其赋值为新的连接点的值
                root.left = self.deleteNode(root.left, cur.val)#这里再将左子树内的最大值删除，递归调用
        return root


        