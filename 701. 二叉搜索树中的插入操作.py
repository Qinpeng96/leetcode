"""
[701. 二叉搜索树中的插入操作](https://leetcode-cn.com/problems/insert-into-a-binary-search-tree/)
给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 保证原始二叉搜索树中不存在新值。

注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回任意有效的结果。

例如, 

给定二叉搜索树:
#
	        4
	       / \
	      2   7
	     / \
	    1   3

和 插入的值: 5
你可以返回这个二叉搜索树:
#
	         4
	       /   \
	      2     7
	     / \   /
	    1   3 5
或者这个树也是有效的:
#
	         5
	       /   \
	      2     7
	     / \   
	    1   3
	         \
	          4

二叉搜索树中的另一个常见操作是插入一个新节点。有许多不同的方法去插入新节点，这篇文章中，我们只讨论一种使整体操作变化最小的经典方法。
 它的主要思想是为目标节点找出合适的叶节点位置，然后将该节点作为叶节点插入。 因此，搜索将成为插入的起始。

与搜索操作类似，对于每个节点，我们将：

根据节点值与目标节点值的关系，搜索左子树或右子树；
重复步骤 1 直到到达外部节点；
根据节点的值与目标节点的值的关系，将新节点添加为其左侧或右侧的子节点。
这样，我们就可以添加一个新的节点并依旧维持二叉搜索树的性质。


使用递归法是比较快速的：

 1. 递归就首先要确定什么时候返回，由于这道题是插入到合适的位置，所以应该才找到合适的位置后返回。
 2. 由于我们可以比较节点和待插入的值，所以可以通过递归很快找到待插入的点，这个时候点应该为空，此时我们就可以使用 
     if not root: return TreeNode(val)创建这个节点，并且返回连接到主树上。
 3. 由于函数的最后是一个return root  ,所以找到值之后就会一层层的逐上返回，直到初始的root=根节点。

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
    #如果此一次为空节点，直接返回这个新节点，如果是后来的递归中找到一个空的位置，说明我们找到了待加入的
    #节点需要插入的位置，于是逐层向上返回
        if not root: return TreeNode(val)       
        if root.val > val:#当前值大于待加入值，向当前值的左边寻找
            root.left = self.insertIntoBST(root.left, val)
        else:#当前值小于待加入的值，向右边寻找
            root.right = self.insertIntoBST(root.right, val)
        return root#最后return root 在递归的时候是连接上上一节点返回
""""
使用迭代法也差不多是同样的道理，但是注意，迭代的时候需要保存两个现场。

第一个就是初始的根节点 node = root

第二个就是找到待插入的地方只有，因为节点为空才会终止 while 循环，所以我们需要返回空节点的上一节点。看是插入左边还是右边，
因为while循环内为空表示找到位置可以弹出，但是不知道这个空节点是上一个节点的左子节点还是右子节点，所以需要保留一个上一层现场进行判断


"""
#迭代法
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root: return TreeNode(val)#以来就是空，直接返回新的节点
        node = root#这里保留一个初始的根节点现场
        while node:#寻要到一个待插入的位置（空节点）， 保留空节点的父节点
            pre = node
            if node.val > val:
                node = node.left
            else:
                node = node.right
        if pre.val > val:#找到空节点的父节点，判断是插入左边还是右边
            pre.left = TreeNode(val)
        else:
            pre.right = TreeNode(val)
        return root


