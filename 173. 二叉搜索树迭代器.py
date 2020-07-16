"""
173. 二叉搜索树迭代器
实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。

调用 next() 将返回二叉搜索树中的下一个最小的数。
BSTIterator iterator = new BSTIterator(root);
iterator.next();    // 返回 3
iterator.next();    // 返回 7
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 9
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 15
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 20
iterator.hasNext(); // 返回 false

提示：

next() 和 hasNext() 操作的时间复杂度是 O(1)，并使用 O(h) 内存，其中 h 是树的高度。
你可以假设 next() 调用总是有效的，也就是说，当调用 next() 时，BST 中至少存在一个下一个最小的数。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-search-tree-iterator
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class BSTIterator:

    def __init__(self, root: TreeNode):#初始化，定义每次循环的序号，输出列表，并且执行中序遍历
        self.index = -1
        self.res = []
        self.__inorder(root)
        # self.len = len(self.res)

    def __inorder(self, root):#定义中序遍历，输出res在初始化的时候定义过了
        if not root: return 
        self.__inorder(root.left)
        self.res.append(root.val)False
        self.__inorder(root.right)

    def next(self) -> int:#调用next函数，返回对应的res列表值
        """
        @return the next smallest number
        """
        self.index += 1
        return self.res[self.index]


    def hasNext(self) -> bool:#如果此次index超过res的长度，返回False
        """
        @return whether we have a next smallest number
        """
        return self.index + 1 < len(self.res)
