"""
95. 不同的二叉搜索树 II
给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。



示例：

输入：3
输出：
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释：
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

"""

from typing import List
import functools
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if(n==0):
            return []
        def build_Trees(left,right):
            all_trees=[]#建立一个空的输出
            if(left>right):#左边大于右边，不存在返回None
                return [None]
            for i in range(left,right+1):#首先选择一个根节点作为起始，[left, right]闭区间
                left_trees=build_Trees(left,i-1)#递归左斌的树的所有可能
                right_trees=build_Trees(i+1,right)#递归右边的树的所有可能
                #由于左右两边的总的可能性 = 左边的可能取值数量 * 右边的可能取值数量
                for l in left_trees:#遍历每一个左边树中的元素
                    for r in right_trees:#遍历每一个右边树中的元素
                        cur_tree=TreeNode(i)#创建当前节点
                        cur_tree.left=l#将左边的树中的组合加入左节点
                        cur_tree.right=r#将右边树的组合加入右节点
                        all_trees.append(cur_tree)#最后将本次创立的节点保存在最后的输出中
            return all_trees
        res=build_Trees(1,n)
        return res

if __name__ == "__main__":
  s = Solution()
  print(s.generateTrees(1))


