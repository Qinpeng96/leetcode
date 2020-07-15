 """
[117. 填充每个节点的下一个右侧节点指针 II](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/)
给定一个二叉树

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。
进阶：

你只能使用常量级额外空间。
使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
 

示例：

输入：root = [1,2,3,4,5,null,7]
输出：[1,#,2,3,#,4,5,7,#]
解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。
"""

###
#和上面一道题类似，只不过这里需要考虑跳连的情况，不是完美二叉树，需要对每个节点的子节点个数进行判断
#这里使用的是迭代的方法
###
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def is_valid(root):
            if not root: return #节点不存在
            if root.left: return root.left#节点左边存在，如果左右都存在还是优先返回左
            elif root.right:return root.right#之后节点右边存在，返回右
            else: return root#节点存在，但是没有子节点，返回本身

        if not root:#如果节点为空，直接返回
            return 
        pre = root#设定初始的根节点
        while pre:#当根节点存在的时候继续，这个点是每一行的最左边的点
            cur = pre#对每一行的节点进行连接
            while cur:#当每一行的计算节点不为空时
                temp = is_valid(cur)#判断当前节点的状态，空，无子节点，有左子节点，有有子节点，有两个节点，这五种情况
                if temp == cur.left or temp == cur.right: #存在一个或者两个子节点时，可以进行连接
                    if cur.left and cur.right:#如果该节点下存在两个节点，那么首先连接左右节点，右节点再与后面的连接
                        cur.left.next = cur.right
                        pre_cur = cur#在子右节点连接后面的节点时，我们需要找到后面最开始出现的子节点
                        while cur.next and cur.next == is_valid(cur.next):#这一步就是跳过一些没有子节点的当前层节点
                            cur = cur.next
                        pre_cur.right.next = is_valid(cur.next)#直到找到最后的空null,或者是出现的子节点，进行连接
                    else:#只有一个子节点的时候，也是先找后面一个子节点出的地方
                        while cur.next and cur.next == is_valid(cur.next):
                            cur = cur.next
                        temp.next = is_valid(cur.next)#将前面的某个子节点与后面的节点连接
                cur = cur.next#节点连接过后
            #和上道题目一样，这里应该是确定每一层的起始位置，首先看本次节点是否有子节点，没有就找next,后面的一个节点有不有子节点
            pre = is_valid(pre) if is_valid(pre) == pre.left or is_valid(pre) == pre.right else is_valid(pre.next)
        return root

