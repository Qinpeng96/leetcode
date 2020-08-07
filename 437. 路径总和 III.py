"""
[437. 路径总和 III](https://leetcode-cn.com/problems/path-sum-iii/)
给定一个二叉树，它的每个结点都存放着一个整数值。

找出路径和等于给定数值的路径总数。

路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

示例：

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#
	      10
	     /  \
	    5   -3
	   / \    \
	  3   2   11
	 / \   \
	3  -2   1

返回 3。和等于 8 的路径有:
#
	1.  5 -> 3
	2.  5 -> 2 -> 1
	3.  -3 -> 11
***
没本事看的大佬们的评论，使用双重递归。
- 第一层的递归是找到树中的每一个节点
- 第二层递归是以这个节点出发到叶子节点，找到和为sum的个数。
第二层递归的时候，每次需要减去当前的节点值，才进行下一轮递归。

"""
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.cnt = 0

        def dfs(root, sum):#DFS找到每一个节点
            if not root:return 0
            solve(root, sum)#第二层递归，对每一个节点作为开始，找所有链路上满足条件的个数
            dfs(root.left,sum)
            dfs(root.right,sum)

        def solve(root, sum):
            if not root:return 
            sum -= root.val
            if sum == 0:#如果sum == 0说明刚好满足条件，次数加一，注意这里不能返回，要继续递归到空节点
                self.cnt += 1
            solve(root.left, sum)
            solve(root.right, sum)

        dfs(root, sum)
        return self.cnt

```
"""
根据[560. 和为K的子数组](https://leetcode-cn.com/problems/subarray-sum-equals-k/)这道题的思路，我们还可以建立一个前缀的哈希，方便我们的查找。
这里的递归思想就是，$$返回值 = 当前的前缀和与目标值之差在哈希中的个数 + 左子节点的个数 + 右子节点的个数$$
意思就是从算上root能得到的个数加上它的两个子节点能够得到个数总和。

**注意：在使用字典的时候，我们需要注意每次我们递归前都把当前的前缀和加入了字典，递归一轮完毕之后，我们需要减去上次加入的字典值。这是因为我们是自顶向下递归，
返回的时候是自底向上返回的。在返回的过程中我们之前保存的前缀值还在字典中，这回导致我们在返回到树的中间部分的时候，一查字典，结果底部的前缀树的值还在字典中，
所以我们在返回的时候需要删除本次加入的字典值**
"""
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        cnt = 0
        presum = 0
        dic = {0:1}
        def dfs(root, presum):
            cnt = 0
            if not root: return 0
            presum += root.val#前缀和累加
            if presum - sum in dic:#如果当前的值可以组成，则返回正确的个数
                cnt = dic[presum-sum]

            #当前的前缀和不在字典就加入字典，在的话个数加一
            if presum in dic:
                dic[presum] += 1
            else:
                dic[presum] = 1
            
            #开始递归
            left = dfs(root.left, presum)
            right = dfs(root.right, presum)
            
            #从底部开始回溯的时候，我们增加的字典值也应该要删除，不然会有之后的前缀字典在前面的前缀字典里出现
            dic[presum] -= 1
            return cnt + left + right
        return dfs(root, 0)

```
