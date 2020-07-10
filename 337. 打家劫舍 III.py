"""
337. 打家劫舍 III
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

示例 1:

输入: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

输出: 7 
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
示例 2:

输入: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

输出: 9
解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
"""
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # 显然，我们每一层节点需要保留两个值：
    # [当前节点不参与计算取得的最大收益，当前节点可以取得的最大收益（参与/不参与）]
    # 那么，这两个值的转移方程:
    # 当前节点不参与计算取得的最大收益: helper(root)[0] = helper(root.left)[1]+helper(root.right)[1]
    # 当前节点可以取得的最大收益: helper(root)[1] = max(root.val+helper(root.left)[0]+helper(root.right)[0], helper(root)[0])


class Solution:
    def rob(self, root: TreeNode) -> int:
        return self.helper(root)[1]
    
    # helper函数返回一个节点为根的最大值 = [当前节点不参与计算的最大收益，当前节点的最大收益(参与/不参与)]
    def helper(self, root):
        if root is None:
            return [0, 0]
        left_amount = self.helper(root.left)
        right_amount = self.helper(root.right)
        withoutRoot = left_amount[1] + right_amount[1]
        withRoot = root.val + left_amount[0] + right_amount[0]
        return [withoutRoot, max(withRoot, withoutRoot)]



作者：oliver8641
链接：https://leetcode-cn.com/problems/house-robber-iii/solution/dpdi-gui-qiu-jie-by-oliver8641/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


if __name__ == "__main__":
    s = Solution()
    print(s.rob([2]))
    # print(s.rob([2,7,9,3,1]))

