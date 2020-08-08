[剑指 Offer 26. 树的子结构](https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/)
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:
#
	     3
	    / \
	   4   5
	  / \
	 1   2
给定的树 B：
#
	   4 
	  /
	 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：

输入：A = [1,2,3], B = [3,1]
输出：false
示例 2：

输入：A = [3,4,5,1,2], B = [4,1]
输出：true
限制：

0 <= 节点个数 <= 1000
***
我自己的方法：
先遍历一个和B的头节点一样的节点，在对AB两个进行遍历。
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not B:return False
        def dfsFind(rootA, rootB):
            if not rootA and rootB: return False#A为空，B不为空
            if not rootB: return True#B为空
            #剩下的条件就是A，B都不空
            if rootA.val == rootB.val:#AB当前值相等
                if not rootB.left and not rootB.right:#B没有值 这条路遍历完成
                    return True
                #B这条路没有遍历完，B还有其他子节点，对子节点进行递归。
                if dfsFind(rootA.left, rootB.left) and dfsFind(rootA.right, rootB.right):
                    return True
            #A,B当前值不等,左右开弓，寻找可能
            return dfsFind(rootA.left,B) or dfsFind(rootA.right,B)

        return dfsFind(A, B)
```

下面是大佬的方法
recur(A, B) 函数：
终止条件：
#
	当节点 B 为空：说明树 B 已匹配完成（越过叶子节点），因此返回 true ；
	当节点 A 为空：说明已经越过树 A 叶子节点，即匹配失败，返回 false ；
	当节点 A 和 B 的值不同：说明匹配失败，返回 false ；
#
	返回值：
	判断 A 和 B 的左子节点是否相等，即 recur(A.left, B.left) ；
	判断 A 和 B 的右子节点是否相等，即 recur(A.right, B.right) ；
#

 isSubStructure(A, B) 函数：

	特例处理： 当 树 A 为空 或 树 B 为空 时，直接返回 false ；
	返回值： 若树 B是树 A的子结构，则必满足以下三种情况之一，因此用或 || 连接；
	以 节点 A 为根节点的子树 包含树 B ，对应 recur(A, B)；
	树 B 是 树 A 左子树 的子结构，对应 isSubStructure(A.left, B)；
	树 B 是 树 A 右子树 的子结构，对应 isSubStructure(A.right, B)；

```python
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A, B):
            if not B: return True
            if not A or A.val != B.val: return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        return bool(A and B) and (recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))

作者：jyd
链接：https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/solution/mian-shi-ti-26-shu-de-zi-jie-gou-xian-xu-bian-li-p/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```


其他大佬的思路：

首先要遍历A找出与B根节点一样值的节点R
然后判断树A中以R为根节点的子树是否包含和B一样的结构
```python
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        res = False
        if A is not None and B is not None:
            if A.val == B.val:
                res = self.helper(A,B)
            if not res:
                res = self.isSubStructure(A.left, B)
            if not res:
                res = self.isSubStructure(A.right, B)
        return res
    
    def helper(self, A, B):
        if B is None:
            return True
        if A is None:
            return False
        if A.val != B.val:
            return False
        return self.helper(A.left, B.left) and self.helper(A.right, B.right)

作者：bryceustc
链接：https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/solution/shu-de-zi-jie-gou-di-gui-bian-li-by-tang-ji-he-de-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
