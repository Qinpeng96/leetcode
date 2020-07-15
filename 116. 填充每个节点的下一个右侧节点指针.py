"""
116. 填充每个节点的下一个右侧节点指针
给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

 
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
##下面是递归的方法
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def solve(r_left, r_right, pre_right):
            if not r_left or not r_right: #如果左右节点为空，直接返回
                return
            r_left.next = r_right#不为空则先连接从左到右
            if pre_right != None:#如果上一层的next不为空
                r_right.next = pre_right.left#将本层的右节点与上一层next的左节点相连
            #本层的连接已经完成，接下来就是需要递归，首先就判断子节点是否存在，不存在直接返回，
            #也可以直接递归，因为递归中第一行已经对是否存在进行了判断
        
            if not r_left.left:
                return
            else:
                solve(r_left.left, r_left.right, r_left.next)#注意这里的上一层next,为left的next
                solve(r_right.left, r_right.right,r_right.next)#这里上一层的next为right的next
        
        if not root:#首先判断是否为空，如果是接直接返回
            return root
        else:#如果不为空表示可以递归解决，其中root.next默认是为None
            solve(root.left, root.right, root.next)
            return root

#####简洁写法
def connect(self, root: 'Node') -> 'Node':
        if not root:
            return 
        if root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root

作者：powcai
链接：https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/solution/di-gui-he-die-dai-by-powcai-4/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

################################
#这是一种迭代的方法
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        pre = root
        while pre:
            cur = pre
            while cur:
                if cur.left: cur.left.next = cur.right
                if cur.right and cur.next: cur.right.next = cur.next.left
                cur = cur.next
            pre = pre.left
        return root

作者：powcai
链接：https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/solution/di-gui-he-die-dai-by-powcai-4/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。