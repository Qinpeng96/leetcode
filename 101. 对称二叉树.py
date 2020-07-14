"""
101. 对称二叉树
给定一个二叉树，检查它是否是镜像对称的。

 

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
 

进阶：

你可以运用递归和迭代两种方法解决这个问题吗？
****************************************************
递归的难点在于：找到可以递归的点 为什么很多人觉得递归一看就会，一写就废。 或者说是自己写无法写出来，关键就是你对递归理解的深不深。

对于此题： 递归的点怎么找？从拿到题的第一时间开始，思路如下：

1.怎么判断一棵树是不是对称二叉树？ 答案：如果所给根节点，为空，那么是对称。如果不为空的话，当他的左子树与右子树对称时，他对称

2.那么怎么知道左子树与右子树对不对称呢？在这我直接叫为左树和右树 答案：如果左树的左孩子与右树的右孩子对称，左树的右孩子与右树的左孩子对称，那么这个左树和右树就对称。

仔细读这句话，是不是有点绕？怎么感觉有一个功能A我想实现，但我去实现A的时候又要用到A实现后的功能呢？

当你思考到这里的时候，递归点已经出现了： 递归点：我在尝试判断左树与右树对称的条件时，发现其跟两树的孩子的对称情况有关系。

想到这里，你不必有太多疑问，上手去按思路写代码，函数A（左树，右树）功能是返回是否对称

def 函数A（左树，右树）： 左树节点值等于右树节点值 且 函数A（左树的左子树，右树的右子树），函数A（左树的右子树，右树的左子树）均为真 才返回真

实现完毕。。。




"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        def solve(l_root, r_root):
            if type(l_root) != type(r_root):#如果左右节点类型不一致，直接False
                return False
            elif l_root == None:#节点类型一致中，分null 和数值两种情况，当为null的时候，不需递归，直接返回
                return True
            elif l_root.val == r_root.val:#当两者的值相等的时候，可以递归，左节点的左子树与右节点的右子树
                return solve(l_root.left, r_root.right) and solve(l_root.right, r_root.left)
            else:
                return False
        if not root:#如果根节点为空，返回True
            return True
        else:#根节点不为空，需要递归判断
            return solve(root.left, root.right)

    
####别人的思路更加清晰的代码
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        def bfs(root1, root2):
            if not root1 and not root2: return True
            if not root1 or not root2: return False
            if root1.val != root2.val: return False
            return bfs(root1.left, root2.right) and bfs(root1.right, root2.left)
        return bfs(root.left, root.right)

作者：luo_luo
链接：https://leetcode-cn.com/problems/symmetric-tree/solution/dui-cheng-er-cha-shu-python3shen-du-you-xian-yu-ya/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


        
